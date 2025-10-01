import os
import logging

import numpy as np
from seabed import SEABED
from seabed.results_to_dataframe import results_to_dataframe
from sentence_transformers import SentenceTransformer

logging.basicConfig(level=logging.INFO)



def get_prompts(task_type, task_name, data_split):
    if task_type == "STS":
        updated_dataset = data_split.map(
                            lambda example: {
                                "sentence1": "task: sentence similarity | query: " + example['sentence1'],
                                "sentence2": "task: sentence similarity | query: " + example['sentence2'],
                            })
    elif task_type == "PairClassification":
        updated_dataset = data_split.map(
                            lambda example: {
                                "sentence1": "task: sentence similarity | query: " + example['sentence1'],
                                "sentence2": "task: sentence similarity | query: " + example['sentence2'],
                            })                      
    elif task_type == "Classification":
        updated_dataset = ["task: classification | query: " + example for example in data_split]
    elif task_type == "Clustering":
        updated_dataset = ["task: clustering | query: " + example for example in data_split]    
    elif task_type == "MultiLabelClassification":
        updated_dataset = ["task: classification | query: " + example for example in data_split]
    elif task_type == "BitextMining":
        updated_dataset = data_split.map(
                            lambda example: {
                                "source": "task: search result | query: " + example['source'],
                                "target": "task: search result | query: " + example['target'],
                            })
    elif task_type == "QARetrieval":
        data_split[0] = ["task: search result | query: " + example for example in data_split[0]]
        data_split[1] = ["title: none | text: " + example for example in data_split[1]]
        updated_dataset = data_split
    elif task_type == "InstructionRetrieval":
        data_split[0] = ["task: search result | query: " + example for example in data_split[0]]
        data_split[1] = ["title: none | text: " + example for example in data_split[1]]
        updated_dataset = data_split
    elif task_type == "Reranking":
        data_split[0] = ["task: search result | query: " + example for example in data_split[0]]
        data_split[1] = ["title: none | text: " + example for example in data_split[1]]
        updated_dataset = data_split
    else:
        raise NotImplementedError
    
    return updated_dataset


def main():
    modelpath = "google/embeddinggemma-300m"
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
    results = evaluation.run(model, prompts=get_prompts, output_folder=f"results/{model_name}", batch_size=16)
    results_to_dataframe(results, output_path=f"results/{model_name}")

    print("--DONE--")

if __name__ == "__main__":
    main()
