import openai
from dotenv import load_dotenv
load_dotenv()


prompt = """
    Give a JSON output with 5 names of animals. The output must be accepted
    by json.loads. Do not add anything before or after the json text.
"""


def chat_completion(prompt, model="gpt-3.5-turbo"):
    res = openai.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": prompt}]
    )
    print(res.choices[0].message.content)


chat_completion(prompt)