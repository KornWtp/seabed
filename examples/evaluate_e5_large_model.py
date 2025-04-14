import logging

import numpy as np
from sea_mteb import SEAMTEB
from sentence_transformers import SentenceTransformer

logging.basicConfig(level=logging.INFO)


class E5LargeWrapper:
    def __init__(self, modelpath="intfloat/multilingual-e5-large"):
        self.model = SentenceTransformer(modelpath)

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

        embeddings_sorted = self.model.encode(sentences_sorted, batch_size=batch_size, max_length=128)
        
        embeddings = [None] * len(sentences)
        for idx, emb in zip(length_sorted_idx, embeddings_sorted):
            embeddings[idx] = emb
        
        return embeddings


def get_prompts(task_type, task_name, data_split):
    if task_type == "STS" or task_type == "PairClassification":
        updated_dataset = data_split.map(
                            lambda example: {
                                "sentence1": f"query: {example['sentence1']}",
                                "sentence2": f"query: {example['sentence2']}",
                            })
    elif task_type == "TextClassification" or task_type == "MultiLabelTextClassification":
        updated_dataset = [f"query: {example}" for example in data_split]
    elif task_type == "BitextMining":
        updated_dataset = data_split.map(
                            lambda example: {
                                "source": f"query: {example['source']}",
                                "target": f"query: {example['target']}",
                            })
    elif task_type == "QARetrieval":
        data_split[0] = [f"query: {example}" for example in data_split[0]]
        data_split[1] = [f"passage: {example}" for example in data_split[1]]
        updated_dataset = data_split
    else:
        raise NotImplementedError
    
    return updated_dataset

def main():
    modelpath = "intfloat/multilingual-e5-large"
    model = E5LargeWrapper(modelpath)
    model_name = modelpath.split("/")[-1].split("_")[-1]
    evaluation = SEAMTEB(task_types=["QARetrieval", 
                                    "TextClassification", 
                                    "STS", 
                                    "PairClassification", 
                                    "BitextMining", 
                                    "MultiLabelTextClassification", 
                                    "InstructionRetreival"])
    evaluation.run(model, prompts=get_prompts, output_folder=f"results/{model_name}", batch_size=16)

    print("--DONE--")

if __name__ == "__main__":
    main()