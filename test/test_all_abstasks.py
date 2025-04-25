import logging

from seabed import SEABED
from sentence_transformers import SentenceTransformer


logging.basicConfig(level=logging.INFO)

model = SentenceTransformer("sentence-transformers/paraphrase-multilingual-mpnet-base-v2")
eval = SEABED(
    tasks=[
        "STSBenchmarkSTS_tha_STS",
        "EMOT_ind_Classification",
        "NewsPHNLI_fil_PairClassification",
        "XQuAD_vie_QARetrieval",
        "TED2020_khm_BitextMining",
    ]
)
eval.run(model)