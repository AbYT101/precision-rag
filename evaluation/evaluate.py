import sys
import os

# Get the parent directory of the current script
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)

# Add the parent directory to the system path
sys.path.insert(0, parent_dir)

from dotenv import load_dotenv


from data.load_data import load_data
from rag.retrieve import create_retriever, retrieve_chunks
from rag.augmentation import augmentation
from rag.generate import generate
from rag.parse_prompts import parse_prompts

from dotenv import load_dotenv

load_dotenv()

openai_api_key = os.getenv('OPENAI_API_KEY')

from datasets import Dataset

questions = [
    "What strategies can be used to get better results from large language models?",
    "What are some effective tactics for writing clear instructions in prompts?",
    "How can I ensure a model provides answers based on reference texts?",
    "What steps should I follow to split complex tasks for better performance?",
    "How can giving the model time to 'think' improve its reasoning accuracy?",
    "What is the benefit of using external tools with language models?",
    "How can systematic testing improve prompt performance?"
]

ground_truths = [
    ["Six strategies can help achieve better results: writing clear instructions, including reference text, splitting complex tasks, giving the model time to think, using external tools, and testing changes systematically."],
    ["To write clear instructions, include details in your query, ask the model to adopt a persona, use delimiters to clearly indicate distinct parts of the input, specify steps required to complete a task, provide examples, and specify the desired length of the output."],
    ["Instruct the model to answer using a reference text and to answer with citations from a reference text. This helps in reducing fabrications and improves the accuracy of the responses."],
    ["Break down the complex task into simpler subtasks. Use intent classification to identify the most relevant instructions, summarize or filter previous dialogue, and summarize long documents piecewise to construct a full summary recursively."],
    ["Instruct the model to work out its own solution before rushing to a conclusion. Use inner monologue or a sequence of queries to reveal the model's reasoning process, and ask the model if it missed anything on previous passes."],
    ["External tools can compensate for the model's weaknesses. Use embeddings-based search for knowledge retrieval, and code execution to perform accurate calculations or call external APIs. These tools can improve the reliability and efficiency of task completion."],
    ["Systematic testing involves evaluating model outputs against gold-standard answers. This helps in ensuring that prompt modifications lead to overall improved performance, and not just isolated better results."]
]

answers = []
contexts = []

data = load_data('./data/knowledge.txt')
documents = retrieve_chunks(data)
retriever = create_retriever(documents, openai_api_key)

# Inference
for query in questions:
    context = retriever.similarity_search(query)
    prompt = augmentation(query, context)
    generated_prompts = generate(prompt, openai_api_key)
    answers.append(generated_prompts)
    contexts.append([docs.page_content for docs in context])

# To dict
data = {
    "question": questions,
    "answer": answers,
    "contexts": contexts,
    "ground_truths": ground_truths
}

# Convert dict to dataset
dataset = Dataset.from_dict(data)

from ragas import evaluate
from ragas.metrics import (
    faithfulness,
    answer_relevancy,
    context_recall,
    context_precision,
)

result = evaluate(
    dataset = dataset,
    metrics=[
        context_precision,
        context_recall,
        faithfulness,
        answer_relevancy,
    ],
)
print("The evaluation result is", result)
df = result.to_pandas()