import logging

import numpy as np
from seabed import SEABED
from seabed.results_to_dataframe import results_to_dataframe
from seabed.utils import get_instruction
from sentence_transformers import SentenceTransformer

logging.basicConfig(level=logging.INFO)


class E5LargeInstructWrapper:
    def __init__(self, modelpath="intfloat/e5-mistral-7b-instruct"):
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
    instruction = get_instruction(task_type, task_name)
    if task_type == "STS":
        updated_dataset = data_split.map(
                            lambda example: {
                                "sentence1": f"Instruct: {instruction}\nQuery: {example['sentence1']}",
                                "sentence2": f"Instruct: {instruction}\nQuery: {example['sentence2']}",
                            })
    elif task_type == "PairClassification":
        updated_dataset = data_split.map(
                            lambda example: {
                                "sentence1": f"Instruct: {instruction}\nQuery: {example['sentence1']}",
                                "sentence2": f"Instruct: {instruction}\nQuery: {example['sentence2']}",
                            })                      
    elif task_type == "Classification":
        updated_dataset = [f"Instruct: {instruction}\nQuery: {example}" for example in data_split]
    elif task_type == "Clustering":
        updated_dataset = [f"Instruct: {instruction}\nQuery: {example}" for example in data_split]
    elif task_type == "MultiLabelClassification":
        updated_dataset = [f"Instruct: {instruction}\nQuery: {example}" for example in data_split]
    elif task_type == "BitextMining":
        updated_dataset = data_split.map(
                            lambda example: {
                                "source": f"Instruct: {instruction}\nQuery: {example['source']}",
                                "target": f"Instruct: {instruction}\nQuery: {example['target']}",
                            })
    elif task_type == "QARetrieval":
        data_split[0] = [f"Instruct: {instruction}\nQuery: {example}" for example in data_split[0]]
        updated_dataset = data_split
    else:
        raise NotImplementedError
    
    return updated_dataset

def main():
    modelpath = "intfloat/e5-mistral-7b-instruct"
    model = E5LargeInstructWrapper(modelpath)
    model_name = modelpath.split("/")[-1].split("_")[-1]
    evaluation = SEABED(task_types=["BitextMining", 
                                    "Classification", 
                                    "Clustering", 
                                    "InstructionRetreival",
                                    "MultiLabelClassification", 
                                    "PairClassification", 
                                    "QARetrieval",
                                    "Reranking",
                                    "STS"])
    results = evaluation.run(model, prompts=get_prompts, output_folder=f"results/{model_name}", batch_size=16)
    results_to_dataframe(results, output_path=f"results/{model_name}")

    print("--DONE--")

if __name__ == "__main__":
    main()