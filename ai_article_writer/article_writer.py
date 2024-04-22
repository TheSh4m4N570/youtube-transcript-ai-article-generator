import os
import openai
from .prompts import system_bot
from openai import OpenAI
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def generate_article(text: str) -> str:
    """
    Generate an article using OpenAI's language model.

    :param text: The text prompt to generate the article.
    :return: The generated article.
    """
    response = openai.chat.completions.create(
        model="gpt-3.5-turbo-0125",
        messages=[
            {"role": "system", "content": system_bot},
            {"role": "user", "content": text},
        ]
    )

    return response.choices[0].message.content
