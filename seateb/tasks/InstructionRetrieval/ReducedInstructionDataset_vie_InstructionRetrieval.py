from ...abstasks.AbsTaskInstructionRetrieval import AbsTaskInstructionRetrieval


class ReducedInstructionDataset_vie_InstructionRetrieval(AbsTaskInstructionRetrieval):
    @property
    def description(self):
        return {
            "name": "ReducedInstructionDataset_vie_InstructionRetrieval",
            "hf_hub_name": "kornwtp/reduced-instruction-dataset-vie-instructionretrieval",
            "description": "",
            "reference": "",
            "category": "s2s",
            "type": "InstructionRetrieval",
            "eval_splits": ["train"],
            "eval_langs": ["vie"],
            "main_score": "ndcg@k",
        }