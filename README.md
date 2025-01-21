# Southeast Asian Text Embedding Benchmark

## Installation

```bash
git clone https://github.com/KornWtp/seateb.git
cd seateb
pip install .
```

## Usage

* Using a python script:

````python
from seateb import SEATEB
from sentence_transformers import SentenceTransformer

# Define the sentence-transformers model name
model_name = "sentence-transformers/paraphrase-multilingual-mpnet-base-v2"

model = SentenceTransformer(model_name)
evaluation = SEATEB(task_types=["STS", "PairClassification"]) # STS, TextClassification, PairClassification, QARetrieval, BitextMining, MultiLabelTextClassification
results = evaluation.run(model, output_folder=f"results/{model_name}", batch_size=32)


````

* Using CLI

```bash
seateb --available_tasks

seateb -m sentence-transformers/paraphrase-multilingual-mpnet-base-v2 \
       -t NewsPHNLI KhmerSTSBenchmarkSTS \
       --output_folder seateb_output \
       --batch_size 32 \
       --verbosity 3
```

### Task selection

Tasks can be selected by providing the list of datasets, but also

* by their task (e.g. "STS" or "BitextMining")

```python
evaluation = SEATEB(task_types=['STS', 'BitextMining']) # Only select STS and BitextMining tasks
```

* by their categories e.g. "s2s" (sentence to sentence) or "p2p" (paragraph to paragraph)

```python
evaluation = SEATEB(task_categories=['s2s']) # Only select sentence2sentence tasks
```

* by their languages

```python
evaluation = SEATEB(task_langs=["th", "id"]) # Only select tasks which support "th" or "id" (ISO 639-1 Code)
```

### Using a custom model

Models should implement the following interface, implementing an `encode` function taking as inputs a list of sentences, and returning a list of embeddings (embeddings can be `np.array`, `torch.tensor`, etc.).

```python
class MyModel():
    def encode(self, sentences, batch_size=32, **kwargs):
        """ Returns a list of embeddings for the given sentences.
        Args:
            sentences (`List[str]`): List of sentences to encode
            batch_size (`int`): Batch size for the encoding

        Returns:
            `List[np.ndarray]` or `List[tensor]`: List of embeddings for the given sentences
        """
        pass

model = MyModel()
evaluation = SEATEB(tasks=["ThaiSTSBenchmarkSTS"])
evaluation.run(model)
```