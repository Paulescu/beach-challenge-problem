.PHONY: fix

evaluation-dataset:
	uv run python scripts/generate_evaluation_dataset.py --n_problems 10 --dataset_name beach_challenge_problem_dataset

evaluate-claude:
	uv run scripts/evaluate_agent.py --model anthropic/claude-sonnet-4-20250514 --dataset beach_challenge_problem_dataset

evaluate-deepseek:
	uv run scripts/evaluate_agent.py --model openai-generic/deepseek-r1:7b --dataset beach_challenge_problem_dataset --item_ids 01988960-c83a-75a3-b89b-6ba9a1b4fdf7

fix:
	uv run ruff check --fix
	uv run ruff format
