"""
Evaluation metrics for the beach challenge problem.
"""

from typing import Any

from opik.evaluation.metrics import base_metric, score_result


class RelativeErrorMetric(base_metric.BaseMetric):
    """
    Computes the relative error between the agent answer and the ground truth.

    Relative error is calculated as: |predicted - actual| / |actual|
    """

    def __init__(self, name: str = "relative_error"):
        self.name = name

    def score(self, answer: dict, expected_output: dict, **ignored_kwargs: Any):
        """
        Compute the relative error between predicted and expected answers.

        Args:
            answer: Dictionary containing the agent's output with 'answer' key
            expected_output: Dictionary containing the ground truth with 'answer' key

        Returns:
            ScoreResult with the relative error
        """
        # breakpoint()

        predicted_answer = answer
        expected_answer = expected_output

        if expected_answer == 0:
            # Handle division by zero case
            relative_error = abs(predicted_answer) if predicted_answer != 0 else 0.0
            reason = f"Expected answer is 0. Absolute error: {relative_error}"
        else:
            relative_error = abs(predicted_answer - expected_answer) / abs(expected_answer)
            reason = f"Predicted: {predicted_answer}, Expected: {expected_answer}, Relative Error: {relative_error:.4f}"

        return score_result.ScoreResult(
            value=relative_error,
            name=self.name,
            reason=reason
        )


class WithinBoundsMetric(base_metric.BaseMetric):
    """
    Binary metric that returns 1 if the relative error is within tolerance, 0 otherwise.
    
    Returns 1 when |predicted - actual| / |actual| < tolerance, 0 otherwise.
    """

    def __init__(self, tolerance: float, name: str = "within_bounds"):
        self.tolerance = tolerance
        self.name = name

    def score(self, answer: dict, expected_output: dict, **ignored_kwargs: Any) -> score_result.ScoreResult:
        """
        Compute whether the relative error is within the specified tolerance.

        Args:
            answer: Dictionary containing the agent's output with 'answer' key
            expected_output: Dictionary containing the ground truth with 'answer' key

        Returns:
            ScoreResult with 1.0 if within bounds, 0.0 otherwise
        """
        predicted_answer = answer
        expected_answer = expected_output

        if expected_answer == 0 :
            # Handle division by zero case
            within_bounds = 1 if predicted_answer == 0 else 0
            reason = f"Expected answer is 0. Within bounds: {within_bounds == 1}"
        else:
            relative_error = abs(predicted_answer - expected_answer) / abs(expected_answer)
            within_bounds = 1 if relative_error < self.tolerance else 0
            reason = f"Predicted: {predicted_answer}, Expected: {expected_answer}, Relative Error: {relative_error:.4f}, Tolerance: {self.tolerance}, Within Bounds: {within_bounds == 1}"

        return score_result.ScoreResult(
            value=within_bounds * 1.0,  # Convert to float
            name=self.name,
            reason=reason
        )