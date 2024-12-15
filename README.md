# SEA-Sentence-Embedding

## Installation

```bash
pip install seateb
```

## Usage

* Using a python script:

````python
from seateb import SEATEB
from sentence_transformers import SentenceTransformer

# Define the sentence-transformers model name
model_name = "kornwtp/simcse-model-phayathaibert"

model = SentenceTransformer(model_name)
evaluation = SEATEB(tasks=["ThaiSTSBenchmark"]) # STS, PairClassification, CrossLingualRetrieval
results = evaluation.run(model, output_folder=f"results/{model_name}")


````