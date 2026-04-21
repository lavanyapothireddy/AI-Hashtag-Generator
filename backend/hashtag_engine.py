from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_hashtags_ai(text: str):
    prompt = f"""
    Generate 10 high-quality Instagram hashtags for this text:
    "{text}"

    Rules:
    - Return ONLY hashtags
    - No explanation
    - Include AI, domain-specific and trending hashtags
    - Format: #TagName
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    content = response.choices[0].message.content

    hashtags = [
        tag.strip()
        for tag in content.split()
        if tag.startswith("#")
    ]

    return hashtags[:12]
