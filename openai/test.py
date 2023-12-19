import openai
import json
from dotenv import load_dotenv
load_dotenv()


def find_product(sql_query):
    results = [
        {"name": "pen", "color": "blue", "price": 1.89},
        {"name": "pen", "color": "red", "price": 0.89}
    ]

    return results


functions = [
    {
        "name": "find_product",
        "description": "Get a list of products from a sql query",
        "parameters": {
            "type": "object",
            "properties": {
                "sql_query": {
                    "type": "string",
                    "description": "A SQL query"
                }
            },
            "required": ["sql_query"]
        }
    }
]

user_question = "I need the top 2 products where the price is less than 2.00"
messages = [
    {"role": "user", "content": user_question}
]

response = openai.chat.completions.create(
    model="gpt-3.5-turbo-0613",
    messages=messages,
    functions=functions
)

response_message = response.choices[0].message
messages.append(response_message)

print(f"All: {response}")
print("------------------------------------")
print(f"Message: {response_message}")
print("====================================")

function_args = json.loads(
    response_message.function_call.arguments
)

products = find_product(function_args.get("sql_query"))

messages.append(
    {
        "role": "function",
        "name": "find_product",
        "content": json.dumps(products)
    }
)

response = openai.chat.completions.create(
    model="gpt-3.5-turbo-0613",
    messages=messages
)

print(f"All: {response.choices[0].message.content}")



