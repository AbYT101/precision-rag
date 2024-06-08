from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Weaviate
from langchain_openai import OpenAIEmbeddings
import weaviate
import requests


class MyDocument:
    def __init__(self, page_content, metadata=None):
        self.page_content = page_content
        self.metadata = metadata if metadata else {}


def create_retriever(documents, openai_api_key):
    # Initialize client to None
    client = None

    # Check if Weaviate is running and connect if possible
    try:
        response = requests.get("http://localhost:8079/v1/.well-known/apollo-status")
        if response.status_code == 200:
            client = weaviate.Client("http://localhost:8079")
    except requests.exceptions.ConnectionError:
        pass

    # If client is still None, start embedded Weaviate
    if client is None:
        client = weaviate.Client(embedded_options=weaviate.EmbeddedOptions())

    print('whats wrong')
    embeddings = OpenAIEmbeddings(api_key=openai_api_key)
    vectorstore = Weaviate.from_documents(documents=documents, embedding=embeddings, client=client)
    return vectorstore

def retrieve_chunks(data):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000, chunk_overlap=200, length_function=len
    )
    text_chunks = text_splitter.split_text(data)
    documents = [MyDocument(page_content=chunk) for chunk in text_chunks]
    return documents