import logging
from collections import defaultdict
import pandas as pd

from ..evaluation.evaluators import QARetrievalEvaluator
from .AbsTask import AbsTask


class AbsTaskQARetrieval(AbsTask):
    """
    Abstract class for QARetrievalTasks

    The similarity between the query and document is computed, and the results are ranked. 
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def evaluate(self, model, prompts, split="test", **kwargs):
        if not self.data_loaded:
            self.load_data()
        

        data_split = self.dataset[split]
        if "xquad" in self.description["hf_hub_name"] or "indicqa" in self.description["hf_hub_name"] or "ViQuAD" in self.description["hf_hub_name"]:
            queries = data_split["question"]
            documents = list(set(data_split["context"]))
            doc2idx = {d: i for i, d in enumerate(documents)}

            # Map index of query to set of relevant context documents
            relevant_docs = {idx: set([doc2idx[data["context"]]]) for idx, data in enumerate(data_split)}
        elif "tydiqa" in self.description["hf_hub_name"]:
            queries = data_split["question_text"]
            documents = list(set(data_split["passage_text"]))
            doc2idx = {d: i for i, d in enumerate(documents)}

            # Map index of query to set of relevant context documents
            relevant_docs = {idx: set([doc2idx[data["passage_text"]]]) for idx, data in enumerate(data_split)}
        elif "miracl" in self.description["hf_hub_name"] or "mldr" in self.description["hf_hub_name"]:
            queries, answers, documents = [], [], []
            for data in data_split:
                query = data["query"]
                positive_passages = [d["text"] for d in data["positive_passages"]]
                negative_passages = [d["text"] for d in data["negative_passages"]]

                queries.append(query)
                answers.append(positive_passages)

                documents += positive_passages
                documents += negative_passages

            documents = list(set(documents))

            # Map index of query to set of relevant context documents
            relevant_docs = {idx: set(documents.index(a) for a in answer) for idx, answer in enumerate(answers)}
        elif "mlqa" in self.description["hf_hub_name"]:
            queries, answers, documents = [], [], []
            for item in data_split["data"][0]:
                for context_question in item['paragraphs']:
                    context = context_question['context']
                    context = context.replace('\ufeff','')
                    for q_as in context_question['qas']:
                        documents.append(context)
                        answers.append(context)
                        queries.append(q_as['question'])

            documents = list(set(documents))
            
            # Map index of query to set of relevant context documents
            relevant_docs = {idx: set([documents.index(answer)]) for idx, answer in enumerate(answers)}
        else:
            raise NotImplementedError

        
        if prompts is not None:
            queries, documents = prompts(self.description['type'], self.description['name'], [queries, documents])

        # Assign IDs to queries and context documents
        queries = dict(enumerate(queries))
        corpus = dict(enumerate(documents))

        evaluator = QARetrievalEvaluator(queries, corpus, relevant_docs)
        scores = evaluator.compute_metrices(model)

        return scores
