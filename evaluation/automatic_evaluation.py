from datasets import Dataset
from ragas import evaluate
from ragas.metrics import (
    faithfulness,
    answer_relevancy,
    context_recall,
    context_precision,
)
import sys
import os

# Get the parent directory of the current script
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)

# Add the parent directory to the system path
sys.path.insert(0, parent_dir)



from evaluation.test_generator import test_generator


def evaluate_query(question, context, prompts):
    test_cases = test_generator(context)
    result = evaluate(
        test_cases.to_dataset(),
        metrics=[
            context_precision,
            context_recall,
        ],
    )
    return result
