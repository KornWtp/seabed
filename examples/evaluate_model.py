import logging

from sea_mteb import SEAMTEB
from sentence_transformers import SentenceTransformer


logging.basicConfig(level=logging.INFO)


model_name = "sentence-transformers/paraphrase-multilingual-mpnet-base-v2"
model = SentenceTransformer(model_name)
evaluation = SEAMTEB(task_types=["QARetrieval", 
                                    "TextClassification", 
                                    "STS", 
                                    "PairClassification", 
                                    "BitextMining", 
                                    "MultiLabelTextClassification", 
                                    "InstructionRetreival"])
evaluation.run(model, output_folder=f"results/{model_name}", , batch_size=16)

print("--DONE--")