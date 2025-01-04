import logging
from collections import defaultdict
import pandas as pd

from ..evaluation.evaluators import QARetrievalEvaluator, MIRACLRetrievalEvaluator #, TyDiQARetrievalEvaluator, MLQARetrievalEvaluator
from .AbsTask import AbsTask


class AbsTaskQARetrieval(AbsTask):
    """
    Abstract class for QARetrievalTasks

    The similarity between the query and document is computed, and the results are ranked. 
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def evaluate(self, model, split="test", **kwargs):
        if not self.data_loaded:
            self.load_data()
        

        data_split = self.dataset[split]
        if "xquad" in self.description["hf_hub_name"] or "indicqa" in self.description["hf_hub_name"] or "ViQuAD" in self.description["hf_hub_name"]:
            doc_context_id, doc_context, question_id, questions = self.xquad_preprocess(data_split)
            
            evaluator = QARetrievalEvaluator(
                question_id, questions, doc_context_id, doc_context, **kwargs
            )
            scores = evaluator.compute_metrics(model)
        elif "miracl" in self.description["hf_hub_name"] or "mldr" in self.description["hf_hub_name"]:
            all_text, all_answers, all_query = self.miracl_preprocess(data_split)

            evaluator = MIRACLRetrievalEvaluator(
                all_text, all_answers, all_query, **kwargs
            )
            scores = evaluator.compute_metrics(model)
        elif "tydiqa" in self.description["hf_hub_name"]:
            question_id, questions, doc_context_id, doc_context = self.tydiqa_preprocess(data_split)

            evaluator = QARetrievalEvaluator(
                question_id, questions, doc_context_id, doc_context, **kwargs
            )
            scores = evaluator.compute_metrics(model)
        elif "mlqa" in self.description["hf_hub_name"]:
            question_id, questions, doc_context_id, doc_context = self.mlqa_preprocess(data_split)

            evaluator = QARetrievalEvaluator(
                question_id, questions, doc_context_id, doc_context, **kwargs
            )
            scores = evaluator.compute_metrics(model)
        else:
            raise NotImplementedError

        return scores

    def preprocess(self, data):
        all_doc = set(data["context"])
        all_doc = {c:i for i, c in enumerate(all_doc)}

        question_contextid_context = []
        for item in data:
            question = item["question"]
            doc = item["context"]
            question_contextid_context.append([all_doc[doc], question])
            
        df_question = pd.DataFrame(question_contextid_context, columns =["doc_id", "question"])
        df_document = pd.DataFrame(zip(list(all_doc.values()), list(all_doc.keys())), columns =["doc_id", "document"])
        
        doc_context_id = df_document["doc_id"].to_list() 
        doc_context = df_document["document"].to_list()
        question_id = df_question["doc_id"].to_list()
        questions = df_question["question"].to_list()

        return question_id, questions, doc_context_id, doc_context
    
    def xquad_preprocess(self, data):
        all_doc = set(data["context"])
        all_doc = {c:i for i, c in enumerate(all_doc)}

        question_contextid_context = []
        for item in data:
            question = item["question"]
            doc = item["context"]
            question_contextid_context.append([all_doc[doc], question])
            
        df_question = pd.DataFrame(question_contextid_context, columns =["doc_id", "question"])
        df_document = pd.DataFrame(zip(list(all_doc.values()), list(all_doc.keys())), columns =["doc_id", "document"])
        
        doc_context_id = df_document["doc_id"].to_list() 
        doc_context = df_document["document"].to_list()
        question_id = df_question["doc_id"].to_list()
        questions = df_question["question"].to_list()

        return doc_context_id, doc_context, question_id, questions

    def miracl_preprocess(self, data):
        all_query = []
        all_answers = []
        all_text = []
        
        for item in data: 
            query_id = item["query_id"]
            query = item["query"]
            positive_passages = item["positive_passages"]
            negative_passages = item["negative_passages"]
            
            all_query.append(query)
            all_answers.append([x["text"] for x in positive_passages])
        
            all_text += [x["text"] for x in positive_passages]
            all_text += [x["text"] for x in negative_passages]
        all_text = list(set(all_text))  
        
        return all_text, all_answers, all_query

    def tydiqa_preprocess(self, data):
        all_doc = set(data["passage_text"])
        all_doc = {c:i for i, c in enumerate(all_doc)}

        question_contextid_context = []
        for item in data:
            question = item["question_text"]
            doc = item["passage_text"]
            question_contextid_context.append([all_doc[doc], question])
            
        df_question = pd.DataFrame(question_contextid_context, columns =["doc_id", "question"])
        df_document = pd.DataFrame(zip(list(all_doc.values()), list(all_doc.keys())), columns =["doc_id", "document"])

        doc_context_id = df_document["doc_id"].to_list() 
        doc_context = df_document["document"].to_list()
        question_id = df_question["doc_id"].to_list()
        questions = df_question["question"].to_list()

        return question_id, questions, doc_context_id, doc_context

    def mlqa_preprocess(self, data):
        document_id = 0
        context_id = 0
        titleid_title_context = []
        question_contextid_context = []
        titleid_title_allcontext = []
        for item in data["data"][0]:
            title = item['title']
            context_all = ''
            for context_question in item['paragraphs']:
                context = context_question['context']
                context = context.replace('\ufeff','')
                context_all += context + '\n'
                titleid_title_context.append([document_id, title, context_id, context])
                for q_as in context_question['qas']:
                    question = q_as['question']
                    question_contextid_context.append([document_id, context_id, question])
                context_id += 1
            titleid_title_allcontext.append([document_id, title, context_all])
            document_id += 1

        df_document = pd.DataFrame(titleid_title_allcontext, columns =['doc_id','title','document'])
        df_question = pd.DataFrame(question_contextid_context, columns =['doc_id','paragraph_id','question'])

        doc_context_id = df_document["doc_id"].to_list() 
        doc_context = df_document["document"].to_list()
        question_id = df_question["doc_id"].to_list()
        questions = df_question["question"].to_list()

        return question_id, questions, doc_context_id, doc_context


