from openai import OpenAI

def generate(prompt, openai_api_key):
    client = OpenAI(api_key=openai_api_key)
    resp = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt},
        ]
    )
    return resp.choices[0].message.content
