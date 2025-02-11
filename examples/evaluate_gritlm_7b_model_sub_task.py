import logging

import numpy as np
from seateb import SEATEB
from seateb.utils import get_instruction
from seateb.models import GritLM

logging.basicConfig(level=logging.INFO)


class GritLMWrapper:
    def __init__(self, modelpath="GritLM/GritLM-7B"):
        self.model = GritLM(modelpath, torch_dtype="auto")

    def encode(self, sentences, batch_size=32, **kwargs):
        """ Returns a list of embeddings for the given sentences.
        Args:
            sentences (`List[str]`): List of sentences to encode
            batch_size (`int`): Batch size for the encoding

        Returns:
            `List[np.ndarray]` or `List[tensor]`: List of embeddings for the given sentences
        """
        length_sorted_idx = np.argsort([len(sen) for sen in sentences])
        sentences_sorted = [sentences[idx] for idx in length_sorted_idx]

        embeddings_sorted = self.model.encode(sentences_sorted, batch_size=batch_size)
        
        embeddings = [None] * len(sentences)
        for idx, emb in zip(length_sorted_idx, embeddings_sorted):
            embeddings[idx] = emb
        
        return embeddings

def gritlm_instruction(instruction):
    return "<|user|>\n" + instruction + "\n<|embed|>\n" if instruction else "<|embed|>\n"

def get_prompts(task_type, task_name, data_split):
    instruction = get_instruction(task_type, task_name)
    if task_type == "STS":
        updated_dataset = data_split.map(
                            lambda example: {
                                "sentence1": gritlm_instruction(instruction) + example['sentence1'],
                                "sentence2": gritlm_instruction(instruction) + example['sentence2'],
                            })
    elif task_type == "PairClassification":
        updated_dataset = data_split.map(
                            lambda example: {
                                "sentence1": gritlm_instruction(instruction) + example['sentence1'],
                                "sentence2": gritlm_instruction(instruction) + example['sentence2'],
                            })                      
    elif task_type == "TextClassification":
        updated_dataset = [gritlm_instruction(instruction) + example for example in data_split]
    elif task_type == "MultiLabelTextClassification":
        updated_dataset = [gritlm_instruction(instruction) + example for example in data_split]
    elif task_type == "BitextMining":
        updated_dataset = data_split.map(
                            lambda example: {
                                "source": gritlm_instruction(instruction) + example['source'],
                                "target": gritlm_instruction(instruction) + example['target'],
                            })
    elif task_type == "QARetrieval":
        data_split[0] = [gritlm_instruction(instruction) + example for example in data_split[0]]
        data_split[1] = [gritlm_instruction("") + example for example in data_split[1]]
        updated_dataset = data_split
    else:
        raise NotImplementedError
    
    return updated_dataset

TASK_LIST = [
    "WangchanXSyntheticInstructThai120kQARetrieval",
    "ThaiTED2020BitextMining",
    "ThaiTatoebaBitextMining",
    "IndoSQuADNLIPairClassification",
    "IndoTyDIQANLIPairClassification",
    "IndoIDKMRCNLIPairClassification",
    "IndoMultilingualNLI26lang2mil7PairClassification",
    "IndoACIQuADQARetrieval",
    "IndoQASiNaQARetrieval",
    "IndoIDKMRCQARetrieval",
    "IndoQAQARetrieval",
    "IndoTED2020BitextMining",
    "IndoTatoebaBitextMining",
    "VietnameseMultilingualNLI26lang2mil7PairClassification",
    "VietnameseXQuADQARetrieval",
    "VietnameseMLQAQARetrieval",
    "ViQuAD2_0QARetrieval",
    "TagalogTED2020BitextMining",
    "TagalogTatoebaBitextMining",
    "MalayChatGPTOpenQAQARetrieval",
    "MalayTED2020BitextMining",
    "KhmerTED2020BitextMining",
    "TamilTED2020BitextMining",
    "TamilTatoebaBitextMining",
    "BurmeseTED2020BitextMining",
    "BurmeseTatoebaBitextMining",
]

def main():
    modelpath = "GritLM/GritLM-7B"
    model = GritLMWrapper(modelpath)
    model_name = modelpath.split("/")[-1].split("_")[-1]
    for task in TASK_LIST:
        evaluation = SEATEB(tasks=[task])
        evaluation.run(model, prompts=get_prompts, output_folder=f"results/{model_name}", batch_size=4)


    print("--DONE--")

if __name__ == "__main__":
    main()