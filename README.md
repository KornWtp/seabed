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

### Using a custom prompts

Evaluation requires a get_prompts function that takes task_type, task_name, and data_split, and rewrites the dataset with task-aware prompt strings. The "Your prompt" prefix is a placeholder that you can customize (e.g., "task: sentence similarity | query: ...", "query: ...", "document: ..."), prepended to each input depending on the task type.

```python
def get_prompts(task_type, task_name, data_split):
    if task_type == "STS":
        updated_dataset = data_split.map(
                            lambda example: {
                                "sentence1": "Your prompt: " + example['sentence1'],
                                "sentence2": "Your prompt: " + example['sentence2'],
                            })
    elif task_type == "PairClassification":
        updated_dataset = data_split.map(
                            lambda example: {
                                "sentence1": "Your prompt: " + example['sentence1'],
                                "sentence2": "Your prompt: " + example['sentence2'],
                            })                      
    elif task_type == "Classification":
        updated_dataset = ["Your prompt: " + example for example in data_split]
    elif task_type == "Clustering":
        updated_dataset = ["Your prompt:: " + example for example in data_split]    
    elif task_type == "MultiLabelClassification":
        updated_dataset = ["Your prompt: " + example for example in data_split]
    elif task_type == "BitextMining":
        updated_dataset = data_split.map(
                            lambda example: {
                                "source": "Your prompt: " + example['source'],
                                "target": "Your prompt: " + example['target'],
                            })
    elif task_type == "QARetrieval":
        data_split[0] = ["Your prompt: " + example for example in data_split[0]]
        data_split[1] = ["Your prompt: " + example for example in data_split[1]]
        updated_dataset = data_split
    elif task_type == "InstructionRetrieval":
        data_split[0] = ["task: search result | query: " + example for example in data_split[0]]
        data_split[1] = ["title: none | text: " + example for example in data_split[1]]
        updated_dataset = data_split
    elif task_type == "Reranking":
        data_split[0] = ["Your prompt: " + example for example in data_split[0]]
        data_split[1] = ["Your prompt: " + example for example in data_split[1]]
        updated_dataset = data_split
    else:
        raise NotImplementedError
    
    return updated_dataset

```


## Citation

Please cite our paper if you use SEA-BED in your work:

```bibtex
@inproceedings{ponwitayarat-etal-2026-sea,
    title = "{SEA}-{BED}: How Do Embedding Models Represent {S}outheast {A}sian Languages?",
    author = "Ponwitayarat, Wuttikorn  and
      Limkonchotiwat, Peerat  and
      Ng, Raymond  and
      Montalan, Jann Railey  and
      Aung, Thura  and
      Ngui, Jian Gang  and
      Susanto, Yosephine  and
      Tjhi, William Chandra  and
      Tasawong, Panuthep  and
      Cambria, Erik  and
      Chuangsuwanich, Ekapol  and
      Nutanong, Sarana",
    editor = "Liakata, Maria  and
      Moreira, Viviane P.  and
      Zhang, Jiajun  and
      Jurgens, David",
    booktitle = "Proceedings of the 64th Annual Meeting of the {A}ssociation for {C}omputational {L}inguistics (Volume 1: Long Papers)",
    month = jul,
    year = "2026",
    address = "San Diego, California, United States",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2026.acl-long.397/",
    doi = "10.18653/v1/2026.acl-long.397",
    pages = "8788--8822",
    ISBN = "979-8-89176-390-6",
    abstract = "Multilingual text embeddings are often assumed to encode meaning in a perspective-independent semantic space, yielding stable similarity judgments across tasks and languages. Our results show that this assumption does not hold in practice. We introduce SEA-BED, a large-scale benchmark covering 10 Southeast Asian (SEA) languages and diverse embedding tasks, designed to systematically examine how embedding performance varies across tasks, languages, and language-task combinations. Across extensive evaluations, we observe that no single model performs uniformly well across SEA languages; task difficulty differs markedly within languages, and success on one task does not reliably generalize to others. Language-task analyses further reveal highly non-uniform performance landscapes, where performance varies across different language-task combinations. These findings call for closer attention to performance measurements that provide an expansive view across languages and tasks to uncover inconsistencies in semantic representation. Based on these observations, we provide insights for future model development, including data, algorithmic, and architectural considerations."
}
```
The evaluator then calls:

```python
evaluation.run(model, prompts=get_prompts)
```
