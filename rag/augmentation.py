
from langchain.prompts import ChatPromptTemplate
from langchain_community.chat_models import ChatOpenAI

def augmentation(question, context):
    prompt = f""" 
    You are an expert LLM prompt writing service.
    Users can input a description of their objective or task and specify a few scenarios along with their expected outputs. 
    You take their prompt as input and output a better prompt based on your prompt writing expertise and the knowledge on the context. 
    You must write 3 top prompts that can achieve their desired objective and expected outputs.
    Question: {question} 
    Context: {context} 
    Answer:
    """
    # prompt = ChatPromptTemplate.from_template(template)
    # llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0, api_key=openai_api_key)

    return prompt
