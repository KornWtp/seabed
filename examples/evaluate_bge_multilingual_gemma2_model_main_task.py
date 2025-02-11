import logging

import numpy as np
import torch
from seateb import SEATEB
from seateb.utils import get_instruction
from sentence_transformers import SentenceTransformer

logging.basicConfig(level=logging.INFO)


class BGEWrapper:
    def __init__(self, modelpath="BAAI/bge-multilingual-gemma2"):
        self.model = SentenceTransformer(modelpath, model_kwargs={"torch_dtype": torch.float16})

    def encode(self, sentences, batch_size=32, **kwargs):
        """ Returns a list of embeddings for the given sentences.
        Args:
            sentences (`List[str]`): List of sentences to encode
            batch_size (`int`): Batch size for the encoding

        Returns:
            `List[np.ndarray]` or `List[tensor]`: List of embeddings for the given sentences
        """
        length_sorted_idx = np.argsort([len(sen) for sen in sentences])
        sentences_sorted = [sentences[idx] for idx in length_sorted_idx]

        embeddings_sorted = self.model.encode(sentences_sorted, batch_size=batch_size)
        
        embeddings = [None] * len(sentences)
        for idx, emb in zip(length_sorted_idx, embeddings_sorted):
            embeddings[idx] = emb
        
        return embeddings


def get_prompts(task_type, task_name, data_split):
    instruction = get_instruction(task_type, task_name)
    if task_type == "STS":
        updated_dataset = data_split.map(
                            lambda example: {
                                "sentence1": f"<instruct>{instruction}\n<query> {example['sentence1']}",
                                "sentence2": f"<instruct>{instruction}\n<query> {example['sentence2']}",
                            })
    elif task_type == "PairClassification":
        updated_dataset = data_split.map(
                            lambda example: {
                                "sentence1": f"<instruct>{instruction}\n<query> {example['sentence1']}",
                                "sentence2": f"<instruct>{instruction}\n<query> {example['sentence2']}",
                            })                      
    elif task_type == "TextClassification":
        updated_dataset = [f"<instruct>{instruction}\n<query> {example}" for example in data_split]
    elif task_type == "MultiLabelTextClassification":
        updated_dataset = [f"<instruct>{instruction}\n<query> {example}" for example in data_split]
    elif task_type == "BitextMining":
        updated_dataset = data_split.map(
                            lambda example: {
                                "source": f"<instruct>{instruction}\n<query> {example['source']}",
                                "target": f"<instruct>{instruction}\n<query> {example['target']}",
                            })
    elif task_type == "QARetrieval":
        data_split[0] = [f"<instruct>{instruction}\n<query> {example}" for example in data_split[0]]
        updated_dataset = data_split
    else:
        raise NotImplementedError
    
    return updated_dataset


def main():
    modelpath = "BAAI/bge-multilingual-gemma2"
    model = BGEWrapper(modelpath)
    model_name = modelpath.split("/")[-1].split("_")[-1]
    evaluation = SEATEB(task_types=["BitextMining", "MultiLabelTextClassification"])
    evaluation.run(model, prompts=get_prompts, output_folder=f"results/{model_name}", batch_size=8)

    print("--DONE--")

if __name__ == "__main__":
    main()
