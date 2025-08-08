"""
Abstract base class for problem-solving agents.
"""

from abc import ABC, abstractmethod
from typing import Optional, List

from opik import Opik
from opik.evaluation import evaluate

from beach_challenge_problem.metrics import RelativeErrorMetric, WithinBoundsMetric


class GenericAgent(ABC):
    """
    Abstract base class for problem-solving agents.
    """

    @abstractmethod
    def get_answer(self, problem: str) -> float:
        """
        Solves the problem and returns the numeric answer.

        Args:
            problem: The problem statement as a string

        Returns:
            The numeric answer as a float
        """
        pass
    
    @abstractmethod
    def get_params(self) -> dict:
        """
        Returns the parameters of the agent.

        Returns:
            A dictionary containing the agent's parameters
        """
        pass

    def evaluate(
        self,
        dataset_name: str,
        dataset_item_ids: Optional[str | List[str]] = None,
    ):
        """
        Evaluates the agent on the given dataset using Opik.

        Args:
            dataset_name: Name of the dataset to evaluate on
            dataset_item_ids: Optional list of specific dataset item IDs to evaluate

        Returns:
            The evaluation results from Opik
        """
        # Load the dataset from Opik
        client = Opik()
        dataset = client.get_or_create_dataset(name=dataset_name)

        # Define the evaluation task
        def evaluation_task(x):
            return {
                'answer': self.get_answer(x['input']),
            }

        # Kick off the evaluation process
        evaluation = evaluate(
            dataset=dataset,
            task=evaluation_task,
            scoring_metrics=[
                RelativeErrorMetric(name='relative_error'),
                WithinBoundsMetric(tolerance=0.01, name='within_1_percent'),
            ],
            experiment_config={
                'agent_type': self.__class__.__name__,
                'agent_params': self.get_params(),
            },
            task_threads=1,
            dataset_item_ids=[dataset_item_ids] if isinstance(dataset_item_ids, str) else dataset_item_ids,
        )

        # Print and return the evaluation results
        # breakpoint()
        print(evaluation)
        return evaluation
