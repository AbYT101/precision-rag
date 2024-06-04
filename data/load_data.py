import requests
from langchain.document_loaders import TextLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Weaviate
import weaviate
from weaviate.embedded import EmbeddedOption


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
client = weaviate.Client(
  embedded_options = EmbeddedOptions(),
  url='YOUR_WEAVIATE_INSTANCE_URL',
  auth={'username': 'YOUR_USERNAME', 'password': 'YOUR_PASSWORD'}
)

vectorstore = Weaviate.from_documents(
    client = client,    
    documents = chunks,
    embedding = OpenAIEmbeddings(),
    by_text = False
)