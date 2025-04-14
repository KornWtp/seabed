import logging

import numpy as np
from sea_mteb import SEAMTEB
from FlagEmbedding import BGEM3FlagModel

logging.basicConfig(level=logging.INFO)


class BGEWrapper:
    def __init__(self, modelpath="BAAI/bge-m3"):
        self.model = BGEM3FlagModel(modelpath,  use_fp16=True)

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

        embeddings_sorted = self.model.encode(
            sentences_sorted, batch_size=batch_size, max_length=128
        )['dense_vecs']
        
        embeddings = [None] * len(sentences)
        for idx, emb in zip(length_sorted_idx, embeddings_sorted):
            embeddings[idx] = emb

        return embeddings


def main():
    modelpath = "BAAI/bge-m3"
    model = BGEWrapper(modelpath)
    model_name = modelpath.split("/")[-1].split("_")[-1]
    evaluation = SEAMTEB(task_types=["QARetrieval", 
                                    "TextClassification", 
                                    "STS", 
                                    "PairClassification", 
                                    "BitextMining", 
                                    "MultiLabelTextClassification", 
                                    "InstructionRetreival"])
    evaluation.run(model, output_folder=f"results/{model_name}", batch_size=16)

    print("--DONE--")

if __name__ == "__main__":
    main()