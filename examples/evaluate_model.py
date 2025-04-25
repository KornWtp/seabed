import logging

from seabed import SEABED
from seabed.results_to_dataframe import results_to_dataframe
from sentence_transformers import SentenceTransformer


logging.basicConfig(level=logging.INFO)


model_name = "sentence-transformers/paraphrase-multilingual-mpnet-base-v2"
model = SentenceTransformer(model_name)
evaluation = SEABED(task_types=["QARetrieval", 
                                    "TextClassification", 
                                    "STS", 
                                    "PairClassification", 
                                    "BitextMining", 
                                    "MultiLabelTextClassification", 
                                    "InstructionRetreival"])
results = evaluation.run(model, output_folder=f"results/{model_name}", batch_size=32)
results_to_dataframe(results, output_path=f"results/{model_name}")

print("--DONE--")