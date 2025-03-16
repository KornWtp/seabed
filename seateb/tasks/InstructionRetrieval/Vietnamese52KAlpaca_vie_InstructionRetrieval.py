from ...abstasks.AbsTaskInstructionRetrieval import AbsTaskInstructionRetrieval


class Vietnamese52KAlpaca_vie_InstructionRetrieval(AbsTaskInstructionRetrieval):
    @property
    def description(self):
        return {
            "name": "Vietnamese52KAlpaca_vie_InstructionRetrieval",
            "hf_hub_name": "kornwtp/vietnamese52k-alpaca-vie-instructionretrieval",
            "description": "",
            "reference": "",
            "category": "s2s",
            "type": "InstructionRetrieval",
            "eval_splits": ["train"],
            "eval_langs": ["vie"],
            "main_score": "ndcg@k",
        }