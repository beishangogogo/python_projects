from dotenv import load_dotenv
load_dotenv()
import openai


def summarize_video():
    with open("transcript.txt", "r") as f:
        transcript = f.read()

    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "Summarize the following text"},
            {"role": "assistant", "content": "Yes."},
            {"role": "user", "content": transcript}
        ]
    )

    print(response.choices[0].message.content)


if __name__ == "__main__":
    summarize_video()
