import requests
from dotenv import load_dotenv
import os
import weaviate
from weaviate.embedded import EmbeddedOptions
from langchain_community.document_loaders import TextLoader
from langchain_community.vectorstores import Weaviate
from langchain.text_splitter import CharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain.prompts import ChatPromptTemplate
from langchain_community.chat_models import ChatOpenAI
from langchain.schema.runnable import RunnablePassthrough
from langchain.schema.output_parser import StrOutputParser

load_dotenv()

# Ensure your OpenAI API key is set in your environment variables
openai_api_key = os.getenv('OPENAI_API_KEY')

print('OpenAI api key:', openai_api_key)

if not openai_api_key:
    raise ValueError("OPENAI_API_KEY environment variable not set")

# Load Data
loader = TextLoader('./data/prompt.txt')
documents = loader.load()

# Chunk data
text_splitter = CharacterTextSplitter(chunk_size=500, chunk_overlap=50)
chunks = text_splitter.split_documents(documents)

# Initialize Weaviate client with embedded options using the v4 API
try:
    client = weaviate.Client(
        embedded_options=EmbeddedOptions()
    )

    # Check if the client is connected
    if client.is_ready():
        print("Weaviate is ready and running!")
    else:
        print("Failed to connect to Weaviate.")
    
    # Initialize OpenAI Embeddings with API key
    embeddings = OpenAIEmbeddings(api_key=openai_api_key)

    # Initialize LangChain Weaviate vector store
    vectorstore = Weaviate.from_documents(
        documents=chunks,
        embedding=embeddings,
        client=client
    )
    
    # Get retriever
    retriever = vectorstore.as_retriever()

    template = """ 
    You are an expert LLM prompt writing service.
    Users can input a description of their objective or task and specify a few scenarios along with their expected outputs. 
    You take their prompt as input and output a better prompt based on your prompt writing expertise and the knowledge on the context. 
    You must write 3 top prompts that can achieve their desired objective and expected outputs.
    Question: {question} 
    Context: {context} 
    Answer:
    """
    prompt = ChatPromptTemplate.from_template(template)

    llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0, api_key=openai_api_key)

    from langchain.schema.runnable import RunnablePassthrough
    from langchain.schema.output_parser import StrOutputParser

    # Creating a chain of operations
    rag_chain = (
        retriever | 
        prompt | 
        llm | 
        StrOutputParser()
    )

    # Query example
    query = "Who can win the 2024 USA election? I want to know the prediction"
    response = rag_chain.invoke({"question": query})
    print(response)

except ImportError as e:
    print(f"ImportError: {e}")
    print("Please check if 'EmbeddedOptions' is available in the 'weaviate.embedded' module.")
except AttributeError as e:
    print(f"AttributeError: {e}")
    print("Please check the Weaviate client initialization and usage.")
except Exception as e:
    print(f"An error occurred: {e}")
