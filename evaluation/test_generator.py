from ragas.testset.generator import TestsetGenerator
from ragas.testset.evolutions import simple, reasoning, multi_context
from langchain_openai import ChatOpenAI, OpenAIEmbeddings

import os
from dotenv import load_dotenv

load_dotenv()

openai_api_key = os.getenv('OPENAI_API_KEY')

def test_generator(docs):
    # generator with openai models
    generator_llm = ChatOpenAI(model="gpt-3.5-turbo", api_key=openai_api_key)
    critic_llm = ChatOpenAI(model="gpt-3.5-turbo", api_key=openai_api_key)
    embeddings = OpenAIEmbeddings()

    generator = TestsetGenerator.from_langchain(
        generator_llm,
        critic_llm,
        embeddings
    )

    # generate testset
    testset = generator.generate_with_langchain_docs(docs, test_size=5, distributions={simple: 0.5, reasoning: 0.25, multi_context: 0.25})
    print(testset)
    return testset