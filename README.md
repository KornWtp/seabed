# SEA-BED: SouthEast-Asia emBEDding benchmark

## Installation

```bash
git clone https://github.com/KornWtp/seabed.git
cd seabed
pip install .
```

## Usage

* Using a python script:

````python
from seabed import SEABED
from seabed.results_to_dataframe import results_to_dataframe
from sentence_transformers import SentenceTransformer

# Define the sentence-transformers model name
model_name = "sentence-transformers/paraphrase-multilingual-mpnet-base-v2"

model = SentenceTransformer(model_name)
evaluation = SEABED(task_types=["STS", "PairClassification"]) # STS, Classification, PairClassification, QARetrieval, BitextMining, MultiLabelClassification
results = evaluation.run(model, output_folder=f"results/{model_name}", batch_size=32)
results_to_dataframe(results, output_path=f"results/{model_name}")


````

* Using CLI

```bash
seabed --available_tasks

seabed -m sentence-transformers/paraphrase-multilingual-mpnet-base-v2 \
       -t NewsPHNLI_fil_PairClassification \
       --output_folder seabed_output \
       --batch_size 32 \
       --verbosity 3
```

### Task selection

Tasks can be selected by providing the list of datasets, but also

* by their task (e.g. "STS" or "BitextMining")

```python
evaluation = SEABED(task_types=['STS', 'BitextMining']) # Only select STS and BitextMining tasks
```

* by their categories e.g. "s2s" (sentence to sentence) or "p2p" (paragraph to paragraph)

```python
evaluation = SEABED(task_categories=['s2s']) # Only select sentence2sentence tasks
```

* by their languages

```python
evaluation = SEABED(task_langs=["tha", "ind"]) # Only select tasks which support "tha" or "ind" (ISO 639-3 Code)
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
evaluation = SEABED(tasks=["STSBenchmark_tha_STS"])
evaluation.run(model)
```