import os
import logging

import numpy as np
from seabed import SEABED
from seabed.results_to_dataframe import results_to_dataframe
from seabed.utils import get_instruction
from sentence_transformers import SentenceTransformer

logging.basicConfig(level=logging.INFO)



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
                                "source": f"Instruct: {instruction}\nQuery: {example['sentence1']}",
                                "target": f"Instruct: {instruction}\nQuery: {example['sentence2']}",
                            })
    elif task_type == "QARetrieval":
        data_split[0] = [f"Instruct: {instruction}\nQuery: {example}" for example in data_split[0]]
        updated_dataset = data_split
    elif task_type == "InstructionRetrieval":
        data_split[0] = [f"Instruct: {instruction}\nQuery: {example}" for example in data_split[0]]
        updated_dataset = data_split
    elif task_type == "Reranking":
        data_split[0] = [f"Instruct: {instruction}\nQuery: {example}" for example in data_split[0]]
        updated_dataset = data_split
    else:
        raise NotImplementedError
    
    return updated_dataset


def main():
    modelpath = "Qwen/Qwen3-Embedding-0.6B"
    model = SentenceTransformer(modelpath)
    model_name = modelpath.split("/")[-1].split("_")[-1]
    evaluation = SEABED(task_types=[
                                    "BitextMining", 
                                    "Classification", 
                                    "Clustering", 
                                    "InstructionRetrieval",
                                    "MultiLabelClassification", 
                                    "PairClassification", 
                                    "QARetrieval",
                                    "Reranking",
                                    "STS"
                                    ])
    results = evaluation.run(model, prompts=get_prompts, output_folder=f"results/{model_name}", batch_size=4)
    results_to_dataframe(results, output_path=f"results/{model_name}")

    print("--DONE--")

if __name__ == "__main__":
    main()
