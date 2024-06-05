import requests
from langchain.document_loaders import TextLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Weaviate
import weaviate
from weaviate.embedded import EmbeddedOption
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Load Data 
url = ""
res = requests.get(url)
with open("data.txt", "w") as f:
    f.write(res.text)

loader = TextLoader('./data.txt')
documents = loader.load()

# Chunk data
text_splitter = CharacterTextSplitter(chunk_size=500, chunk_overlap=50)
chunks = text_splitter.split_documents(documents)

# Embed and store the chunks
weaviate_url = os.getenv('WEAVIATE_INSTANCE_URL')
weaviate_pwd = os.getenv('WEAVIATE_PASSWORD')
weaviate_usr = os.getenv('WEAVIATE_USERNAME')

client = weaviate.Client(
  embedded_options = EmbeddedOptions(),
  url= weaviate_url,
  auth={'username': weaviate_usr, 'password': weaviate_pwd }
)

vectorstore = Weaviate.from_documents(
    client = client,    
    documents = chunks,
    embedding = OpenAIEmbeddings(),
    by_text = False
)
