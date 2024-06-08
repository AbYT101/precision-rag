import sys
import os

# Get the parent directory of the current script
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)

# Add the parent directory to the system path
sys.path.insert(0, parent_dir)

from dotenv import load_dotenv


from data.load_data import load_data
from retrieve import create_retriever, retrieve_chunks
from augmentation import augmentation
from generate import generate
from parse_prompts import parse_prompts
from evaluation.automatic_evaluation import evaluate_query

load_dotenv()

openai_api_key = os.getenv('OPENAI_API_KEY')

def run_rag(objective:str, scenarios:str, output:str):
    data = load_data('./data/knowledge.txt')
    documents = retrieve_chunks(data)
    retriever = create_retriever(documents, openai_api_key)
    query = "Objective: " + objective + " Scenario: " + scenarios + " Output: " + output
    context = retriever.similarity_search(query)
    prompt = augmentation(query, context)
    generated_prompts = generate(prompt, openai_api_key)
    parsed_prompts = parse_prompts(generated_prompts)
    score = evaluate_query(query, context, parsed_prompts)
    print(score)

    return generated_prompts

