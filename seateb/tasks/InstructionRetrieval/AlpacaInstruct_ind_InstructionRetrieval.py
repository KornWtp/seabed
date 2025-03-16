from ...abstasks.AbsTaskInstructionRetrieval import AbsTaskInstructionRetrieval


class AlpacaInstruct_ind_InstructionRetrieval(AbsTaskInstructionRetrieval):
    @property
    def description(self):
        return {
            "name": "AlpacaInstruct_ind_InstructionRetrieval",
            "hf_hub_name": "kornwtp/alpaca-instruct-ind-instructionretrieval",
            "description": "",
            "reference": "",
            "category": "s2s",
            "type": "InstructionRetrieval",
            "eval_splits": ["train"],
            "eval_langs": ["ind"],
            "main_score": "ndcg@k",
        }