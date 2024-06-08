import re


def parse_prompts(text):
    prompts = re.split(r"Prompt", text)[1:]
    return prompts
