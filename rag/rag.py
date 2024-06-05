import os
from dotenv import load_dotenv
from data.load_data import load_data
from retrieve import retrieve_chunks
from augmentation import augmentation
from generate import generate

load_dotenv()

openai_api_key = os.getenv('OPENAI_API_KEY')

if not openai_api_key:
    raise ValueError("OPENAI_API_KEY environment variable not set")

def main():
    data = load_data('./data/knowledge.txt')
    retriever = retrieve_chunks(data, openai_api_key)
    prompt, llm = augmentation(data, openai_api_key)
    rag_chain = generate(retriever, prompt, llm)

    query = "Who can win the 2024 USA election? I want to know the prediction."
    response = rag_chain.invoke({"question": query})
    print(response)

if __name__ == "__main__":
    main()
