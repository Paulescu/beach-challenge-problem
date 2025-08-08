# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a research project focused on solving the "Beach Challenge Problem" - a complex math/physics word problem involving trigonometry, vector calculations, and multi-step reasoning. The project evaluates different LLM approaches (one-shot, multi-shot, agentic workflows) for solving mathematical reasoning tasks.

The core problem: Kai and Sofia start at the same beach point. Sofia swims toward a buoy 6km offshore at 30° angle (2 km/h with 0.5 km/h perpendicular current drift). Kai paddles along shore for 1 hour at 4 km/h, then turns toward Sofia's position at 3 km/h. After 2.5 total hours, find the distance between them.

Expected answer: ~3.863 km

## Architecture

### BAML Integration
- Uses BAML (Boundary ML) framework for LLM orchestration and structured output
- `baml_src/` contains BAML configuration files:
  - `solve_problem.baml`: Defines the main `SolveProblem` function and `ProblemSolution` data model
  - `clients.baml`: Configures various LLM clients (Anthropic Claude, OpenAI GPT-4o, fallback/retry policies)
  - `generators.baml`: Python code generation config
- `baml_client/` and `src/beach_challenge_problem/baml_client/` contain auto-generated Python client code (DO NOT EDIT)

### Python Structure
- `src/beach_challenge_problem/one_shoot_agent.py`: Main implementation file for single-LLM approach (currently incomplete)
- Uses Python 3.12+ with dependencies: baml-py==0.202.1, opik (for evaluation), pydantic

## Development Commands

### Package Management
```bash
# Install dependencies
uv install

# Install with dev dependencies (includes ruff)
uv install --extra dev

# Add new dependency
uv add package-name
```

### BAML Workflow
```bash
# Generate Python client from BAML files (after modifying .baml files)
# This will create baml_client/ in src/beach_challenge_problem/
uv run baml-cli generate

# Run BAML tests
baml test
```

### Code Quality
```bash
# Lint and format code (recommended)
make fix

# Manual commands
uv run ruff check --fix  # Fix linting issues
uv run ruff format       # Format code
```

### Python Execution
```bash
# Run the one-shot agent
uv run python -m src.beach_challenge_problem.one_shoot_agent

# Run with specific Python path
uv run python src/beach_challenge_problem/one_shoot_agent.py
```

## Key Implementation Notes

- The `ProblemSolution` model expects structured output with `reasoning` (string) and `answer` (float) fields
- Current BAML function uses Claude Sonnet 4 (claude-sonnet-4-20250514) as the primary model
- Test assertions expect answer between 3.862 and 3.864
- Environment variables needed: `ANTHROPIC_API_KEY`, `OPENAI_API_KEY` (for respective clients)
- Project uses Opik for evaluation and dataset management

## Development Workflow

1. Modify BAML files in `baml_src/` for LLM function definitions
2. Run `baml-cli generate` to update Python client code
3. Implement agent logic in `src/beach_challenge_problem/`
4. Test with `baml test` or run Python scripts directly
5. Evaluate results using Opik integration

## TODOs from README
- Build strong OneShootLLM solution using Claude Sonnet 4
- Add evaluation script
- Implement two-shot and many-shot LLM agents
- Add calculator integration for multi-shot approaches

## Documentation sources

## BAML
For any BAML question, use the official documentation that you can find here:
https://docs.boundaryml.com/home

## Opik
For Opik questions, use the official documentation that you can find here:
https://www.comet.com/docs/opik/
