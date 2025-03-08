from ...abstasks.AbsTaskInstructionRetrieval import AbsTaskInstructionRetrieval


class Cendol_ind_InstructionRetrieval(AbsTaskInstructionRetrieval):
    @property
    def description(self):
        return {
            "name": "Cendol_ind_InstructionRetrieval",
            "hf_hub_name": "kornwtp/cendol-ind-instructionretrieval",
            "description": "",
            "reference": "",
            "category": "s2s",
            "type": "InstructionRetrieval",
            "eval_splits": ["train"],
            "eval_langs": ["ind"],
            "main_score": "ndcg@k",
        }