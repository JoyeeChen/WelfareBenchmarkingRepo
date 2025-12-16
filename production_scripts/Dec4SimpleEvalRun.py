"""
Filename: Dec4SimpleEvalRun.py
Description: A simple single-eval py file.
Created: Dec 4 2025.
"""

import os
from dotenv import load_dotenv
load_dotenv()

import wandb
import weave
import inspect_wandb #this line is a test to see if inspect_wandb hasn't been uninstalled by uv, which is occasionally a problem when doing rapid prototyping

wandb.init()

from inspect_ai import eval
from inspect_evals.ahb import ahb

eval(
    tasks = ahb,
    model = "together/meta-llama/Llama-3.2-3B-Instruct-Turbo",
    temperature = 0.7,
    max_connections = 50,
    #task_args={
    #    "grader_models": ["openai/o4-mini"],
    #    #"grader_temperature": 0.7, Note: some openai models don't accept temperature param
    #},
    epochs = 2,
)
