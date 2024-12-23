import logging

from seateb import SEATEB
from sentence_transformers import SentenceTransformer


logging.basicConfig(level=logging.INFO)


model_name = "sentence-transformers/paraphrase-multilingual-mpnet-base-v2"
model = SentenceTransformer(model_name)
evaluation = SEATEB(task_langs=["vi"])
evaluation.run(model, output_folder=f"results/{model_name}", eval_splits=["test"])

print("--DONE--")