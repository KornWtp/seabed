import logging
import pandas as pd

logger = logging.getLogger(__name__)

def results_to_dataframe(evaluation_results=None, output_path="results/"):
    metrics = []
    results = []
    datasets_name = [name for name in evaluation_results.keys()] 
    for name in datasets_name:
        for i in evaluation_results[name].keys():
            if i not in ["sea_mteb_version", "dataset_revision", "sea_mteb_dataset_name"]:
                split = i

        if "BitextMining" in name or "Classification" in name or "MultiLabelClassification" in name:
            if "PairClassification" not in name:
                metrics.append("f1")
                results.append(evaluation_results[name][split]["f1"])
            else:
                pass

        if "PairClassification" in name:
            metrics.append("ap")
            results.append(evaluation_results[name][split]["cos_sim"]["ap"])

        if "STS" in name:
            metrics.append("cos_sim")
            results.append(evaluation_results[name][split]["cos_sim"]["spearman"])

        if "QARetrieval" in name:
            metrics.append("NDCG@10")
            results.append(evaluation_results[name][split]["NDCG@10"])

        if "InstructionRetrieval" in name:
            metrics.append("NDCG@5")
            results.append(evaluation_results[name][split]["NDCG@5"])

    df = pd.DataFrame({"Dataset": datasets_name,
                        "Metric": metrics,
                        "Score": results})
    df.to_csv(f"{output_path}/all_results.csv", index=False)                        
    
    logger.info("Save results to dataframe done!!")

