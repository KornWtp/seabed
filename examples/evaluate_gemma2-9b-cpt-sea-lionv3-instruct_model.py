import logging

import torch
import numpy as np
from seabed import SEABED
from seabed.results_to_dataframe import results_to_dataframe
from seabed.utils import get_instruction
from sentence_transformers import SentenceTransformer, models

logging.basicConfig(level=logging.INFO)

class ModelWrapper:
    def __init__(self, modelpath="aisingapore/gemma2-9b-cpt-sea-lionv3-instruct"):
        word_embedding_model = models.Transformer(modelpath, max_seq_length=8192)
        dimension = word_embedding_model.get_word_embedding_dimension()
        pooling_model = models.Pooling(dimension, pooling_mode_mean_tokens=True)
        self.model = SentenceTransformer(modules=[word_embedding_model, pooling_model])

    def encode(self, sentences, batch_size=32, device="cuda", **kwargs):
        """Encodes sentences into fixed-size embeddings.
        
        Args:
            sentences (`List[str]`): List of input sentences.
            batch_size (`int`): Batch size for processing.
            device (`str`): Device to run inference (default: "cuda").
        
        Returns:
            `np.ndarray`: Encoded sentence embeddings.
        """
        embeddings = self.model.encode(
            sentences,
            batch_size=batch_size,
            convert_to_numpy=True,
            show_progress_bar=True,
            device=device,
            **kwargs
        )
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
    modelpath = "aisingapore/gemma2-9b-cpt-sea-lionv3-instruct"
    model = ModelWrapper(modelpath)
    model_name = modelpath.split("/")[-1].split("_")[-1]
    evaluation = SEABED(task_types=["QARetrieval", 
                                    "TextClassification", 
                                    "STS", 
                                    "PairClassification", 
                                    "BitextMining", 
                                    "MultiLabelTextClassification", 
                                    "InstructionRetreival"])
    results = evaluation.run(model, prompts=get_prompts, output_folder=f"results/{model_name}", batch_size=16)
    results_to_dataframe(results, output_path=f"results/{model_name}")

    print("--DONE--")

if __name__ == "__main__":
    main()