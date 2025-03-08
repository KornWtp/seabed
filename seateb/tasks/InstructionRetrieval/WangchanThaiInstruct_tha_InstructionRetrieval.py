from ...abstasks.AbsTaskInstructionRetrieval import AbsTaskInstructionRetrieval


class WangchanThaiInstruct_tha_InstructionRetrieval(AbsTaskInstructionRetrieval):
    @property
    def description(self):
        return {
            "name": "WangchanThaiInstruct_tha_InstructionRetrieval",
            "hf_hub_name": "kornwtp/wangchan-instruct-tha-instructionretrieval",
            "description": "",
            "reference": "",
            "category": "s2s",
            "type": "InstructionRetrieval",
            "eval_splits": ["test"],
            "eval_langs": ["tha"],
            "main_score": "ndcg@k",
        }