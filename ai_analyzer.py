import os
from openai import OpenAI
client = OpenAI()

def analyze_article(client_name, sector, article):
    prompt = f"""
    Client: {client_name}
    Sector: {sector}

    Article:
    {article['title']}
    {article['summary']}

    Return:
    - summary (2 sentences)
    - impact (1-5)
    - type (risk/growth/other)
    - why it matters
    """
    response = client.chat.completions.create(
        model="gpt-5",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content
