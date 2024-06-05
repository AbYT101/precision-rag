
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.vectorstores import Weaviate
from langchain_openai import OpenAIEmbeddings
import weaviate
from langchain_experimental.text_splitter import SemanticChunker
from langchain_openai.embeddings import OpenAIEmbeddings


def retrieve_chunks(data, openai_api_key):
    text_splitter = SemanticChunker(OpenAIEmbeddings())
    docs = text_splitter.create_documents([data])
    print(docs[0].page_content)

    client = weaviate.Client(embedded_options=weaviate.EmbeddedOptions())
    embeddings = OpenAIEmbeddings(api_key=openai_api_key)
    vectorstore = Weaviate.from_documents(documents=docs, embedding=embeddings, client=client)
    retriever = vectorstore.as_retriever()
    
    return retriever
