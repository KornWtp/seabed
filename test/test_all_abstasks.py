import logging

from seateb import SEATEB
from sentence_transformers import SentenceTransformer


logging.basicConfig(level=logging.INFO)

model = SentenceTransformer("sentence-transformers/paraphrase-multilingual-mpnet-base-v2")
eval = SEATEB(
    tasks=[
        "ThaiSTSBenchmarkSTS",
        "IndoEMOT",
        "NewsPHNLI",
        "VietnameseXQuAD",
        "KhmerTED2020",
    ]
)
eval.run(model)