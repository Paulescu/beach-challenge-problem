"""
CLI script to evaluate agents on datasets using Opik.
"""

import fire
from typing import Optional, List

from beach_challenge_problem.agents import OneShootAgent


def evaluate_one_shoot_agent(
    model: str,
    dataset: str,
    item_ids: Optional[List[str]] = None,
    base_url: str = "http://localhost:11434/v1"
):
    """
    Evaluate OneShootAgent on a dataset.
    
    Args:
        model: Model identifier (e.g., anthropic/claude-sonnet-4-20250514)
        dataset: Name of the dataset to evaluate on
        item_ids: Optional list of specific dataset item IDs to evaluate
        base_url: Base URL for the model API
    
    Returns:
        The evaluation results from Opik
    
    Examples:
        # Evaluate on entire dataset
        python evaluate_agent.py --model anthropic/claude-sonnet-4-20250514 --dataset beach_challenge_test
        
        # Evaluate specific items
        python evaluate_agent.py --model anthropic/claude-sonnet-4-20250514 --dataset beach_challenge_test --item_ids item_1,item_2
    """
    print(f"Evaluating OneShootAgent with model: {model}")
    print(f"Dataset: {dataset}")
    print(f"Base URL: {base_url}")
    
    if item_ids:
        print(f"Evaluating specific items: {item_ids}")
    
    # Create and evaluate the agent
    agent = OneShootAgent(model=model, base_url=base_url)
    evaluation_result = agent.evaluate(
        dataset_name=dataset,
        dataset_item_ids=item_ids
    )
    
    print("Evaluation completed successfully!")
    return evaluation_result


if __name__ == "__main__":
    fire.Fire(evaluate_one_shoot_agent)