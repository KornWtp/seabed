"""
entry point for the library
example call:
  pip install git+https://github.com/KornWtp/seateb.git
  seateb -m sentence-transformers/paraphrase-multilingual-mpnet-base-v2 \
       -t NewsPHNLI KhmerSTSBenchmarkSTS \
       --output_folder seateb_output \
       --verbosity 3
"""


import argparse
import logging

from seateb import SEATEB
from sentence_transformers import SentenceTransformer


logging.basicConfig(level=logging.WARNING)
logger = logging.getLogger(__name__)


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "-m",
        "--model",
        type=str,
        default=None,
        help="Model to use. Use pre-trained model name from https://huggingface.co/models",
    )
    parser.add_argument(
        "--task_types",
        nargs="+",
        type=str,
        default=None,
        help="List of task types (STS, TextClassification..) to be evaluated. If None, all tasks will be evaluated",
    )
    parser.add_argument(
        "--task_categories",
        nargs="+",
        type=str,
        default=None,
        help="List of task categories (s2s, p2p..) to be evaluated. If None, all tasks will be evaluated",
    )
    parser.add_argument(
        "-t",
        "--tasks",
        nargs="+",
        type=str,
        default=None,
        help="List of tasks to be evaluated. If specified, the other arguments are ignored.",
    )
    parser.add_argument("--device", type=int, default=None, help="Device to use for computation")
    parser.add_argument("--batch_size", type=int, default=32, help="Batch size for computation")
    parser.add_argument("--seed", type=int, default=42, help="Random seed for computation")
    parser.add_argument("--output_folder", type=str, default="results", help="Output directory for results")
    parser.add_argument("-v", "--verbosity", type=int, default=2, help="Verbosity level")

    ## display tasks
    parser.add_argument(
        "--available_tasks",
        action="store_true",
        default=False,
        help="Display the available tasks",
    )

    # TODO: check what prams are useful to add
    args = parser.parse_args()

    # set logging based on verbosity level
    if args.verbosity == 0:
        logging.getLogger("seateb").setLevel(logging.CRITICAL)
    elif args.verbosity == 1:
        logging.getLogger("seateb").setLevel(logging.WARNING)
    elif args.verbosity == 2:
        logging.getLogger("seateb").setLevel(logging.INFO)
    elif args.verbosity == 3:
        logging.getLogger("seateb").setLevel(logging.DEBUG)

    logger.info("Running with parameters: %s", args)

    if args.available_tasks:
        SEATEB.seateb_tasks()
        return
    del args.available_tasks

    if args.model is None:
        raise ValueError("Please specify a model using the -m or --model argument")
    # delete None values
    for key in [k for k in args.__dict__ if args.__dict__[k] is None]:
        del args.__dict__[key]

    model = SentenceTransformer(args.model, device=args.device if "device" in args else None)
    eval = SEATEB(**vars(args))
    del args.model
    eval.run(model, **vars(args))


if __name__ == "__main__":
    main()