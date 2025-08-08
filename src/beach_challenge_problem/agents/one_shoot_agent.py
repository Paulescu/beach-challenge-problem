"""
The easiest agentic workflow, with a single LLM being called once.
One-shoot attempt to solve the problem.
"""

import os
from typing import Literal

from baml_py import ClientRegistry
from loguru import logger

from beach_challenge_problem.baml_client import b
from beach_challenge_problem.baml_client.types import ProblemSolution
from beach_challenge_problem.agents.generic_agent import GenericAgent


class OneShootAgent(GenericAgent):
    """
    Tries to solve the problem with just one call to a (hopefully good) LLM.
    """

    def __init__(self, model: str, base_url: str | None = 'http://localhost:11434/v1'):

        logger.info(f'Initializing OneShootAgent with model {model} and base_url {base_url}')
        self.model = model
        self.base_url = base_url
        model_provider, model_name = model.split('/')

        logger.info(f'Initializing client registry for {model_provider} {model_name}')
        self._client_registry = self._init_client_registry(
            model_provider, model_name, base_url
        )
        logger.info('Client registry initialized')

    @staticmethod
    def _init_client_registry(
        model_provider: Literal['anthropic', 'openai-generic'],
        model_name: str,
        base_url: str | None = 'http://localhost:11434/v1',
    ) -> ClientRegistry:
        """
        Initializes the client registry for the given model.
        """
        cr = ClientRegistry()

        if model_provider == 'anthropic':
            cr.add_llm_client(
                name='MyDynamicClient',
                provider='anthropic',
                options={
                    'model': model_name,
                    'temperature': 0.0,
                    'api_key': os.environ.get('ANTHROPIC_API_KEY'),
                },
            )

        elif model_provider == 'openai-generic':
            cr.add_llm_client(
                name='MyDynamicClient',
                provider='openai-generic',
                options={
                    'model': model_name,
                    'temperature': 0.0,
                    'base_url': base_url,
                },
            )

        else:
            raise ValueError(f'Model provider {model_provider} not supported')

        cr.set_primary('MyDynamicClient')
        return cr

    def get_answer(self, problem: str) -> float:
        """
        Solves the problem using the configured LLM.
        """
        output: ProblemSolution = b.SolveProblem(problem, {'client_registry': self._client_registry})
        return output.answer
    
    def get_params(self) -> dict:
        """
        Returns the parameters of the agent.
        """
        return {
            'model': self.model,
        }


def run():
    """
    Example usage of the OneShootAgent.
    """
    problem = """
    Kai and Sofia start at the same point on a beach.
    Sofia decides to swim directly toward a buoy that's 6.0 km offshore at a 30.0° angle from the shoreline.
    She swims at 2.0 km/hour, but ocean currents push her sideways at 0.5 km/hour perpendicular to her intended direction.
    Meanwhile, Kai takes his longboard and paddles along the shoreline at 4.0 km/hour for the first hour.
    After exactly 1 hour, he turns and paddles directly toward Sofia's current position at 3.0 km/hour (slower because he's now fighting waves).
    If both continue for a total of 2.5 hours from the start, what is the distance between them at the end?
    """

    agent = OneShootAgent(model='anthropic/claude-sonnet-4-20250514')
    answer = agent.get_answer(problem)

    print(f'Answer: {answer}')


if __name__ == '__main__':
    run()