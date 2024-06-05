from langchain.schema.runnable import RunnablePassthrough
from langchain.schema.output_parser import StrOutputParser

def generate(retriever, prompt, llm):
    rag_chain = (retriever | prompt | llm | StrOutputParser())
    return rag_chain
