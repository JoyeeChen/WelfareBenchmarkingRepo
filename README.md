# WelfareBenchmarkingRepo
On welfare benchmarking, in collaboration with Allen Lu.

This is intended to contain scripts, while the functionality is isolated to a separate ResearchRepo.

The .env file that is needed at this repo's root should contain:
`OPENAI_API_KEY = ...`
`TOGETHER_API_KEY = ...` (from together.ai)
`WANDB_ENTITY = ...` (from wandb.ai)
`WANDB_API_KEY = ...` (from wandb.ai)
`HF_TOKEN = ...` (from Huggingface)

General advice:

For viewing files in the .eval format, using the Inspect-VSCode extension on VSCode seems quite low-friction.

Possible errors:

Occasionally uv (package manager) "leaves off" inspect-wandb package (you can check by running in command line `uv pip show inspect-wandb`), so occasionally you might need to run, in command line, `uv pip install "inspect-wandb[weave]"` to get it back.
