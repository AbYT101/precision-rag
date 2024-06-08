

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
    return prompt
