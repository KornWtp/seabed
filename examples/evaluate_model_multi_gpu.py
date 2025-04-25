import logging

import numpy as np
import torch
from seabed import SEABED
from seabed.results_to_dataframe import results_to_dataframe
from seabed.utils import get_instruction
from sentence_transformers import SentenceTransformer

logging.basicConfig(level=logging.INFO)


class ModeltWrapper:
    def __init__(self, modelpath="sentence-transformers/paraphrase-multilingual-mpnet-base-v2"):
        self.model = SentenceTransformer(modelpath)
        if torch.cuda.device_count() > 1:
            logging.info(f"Using {torch.cuda.device_count()} GPUs")
            self.model = torch.nn.DataParallel(self.model)

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

        embeddings_sorted = self.model.module.encode(sentences_sorted, 
                                                     batch_size=batch_size, 
                                                     max_length=128, 
                                                     convert_to_numpy=True)
        
        embeddings = [None] * len(sentences)
        for idx, emb in zip(length_sorted_idx, embeddings_sorted):
            embeddings[idx] = emb
        
        return embeddings

def main():
    modelpath = "sentence-transformers/paraphrase-multilingual-mpnet-base-v2"
    model = ModeltWrapper(modelpath)
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


