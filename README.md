# Southeast Asian Text Embedding Benchmark

## Installation

```bash
git clone https://github.com/KornWtp/seateb.git
cd seateb
pip install -e .
```

## Usage

* Using a python script:

````python
from seateb import SEATEB
from sentence_transformers import SentenceTransformer

# Define the sentence-transformers model name
model_name = "kornwtp/simcse-model-phayathaibert"

model = SentenceTransformer(model_name)
evaluation = SEATEB(task_types=["STS", "PairClassification"]) # STS, PairClassification, QARetrieval, CrossLingualRetrieval
results = evaluation.run(model, output_folder=f"results/{model_name}")


````