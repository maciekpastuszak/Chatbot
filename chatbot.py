import openai
from dotenv import dotenv_values
import argparse

config = dotenv_values(".env")
openai.api_key = config["OPENAI_API_KEY"]


def main():
    parser = argparse.ArgumentParser(
        description="Simple command line chatbot with GPT-4"
    )

    parser.add_argument(
        "--pesonality",
        type=str,
        help="A brief summary of the chatbot's personality",
        default="friendly and helpful",
    )

    args = parser.parse_args()
    args.personality

    initial_prompt = (
        f"You are a conversational chatbot. Your personality is: {args.personality}"
    )
    messages = [{"role": "system", "content": initial_prompt}]
    while True:
        try:
            user_input = input("You: ")
            messages.append({"role": "user", "content": user_input})
            res = openai.ChatCompletion.create(model="gpt-4", messages=messages)

            messages.appen(res["choices"][0]["message"].to_dict())
            print("Assistant: ", res["choices"][0]["message"]["content"])
            print("ALL MESSAGES", messages)

        except KeyboardInterrupt:
            print("Exiting....")
            break

    print(res)


if __name__ == "__main__":
    main()
