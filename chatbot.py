import openai
from dotenv import dotenv_values
import argparse

config = dotenv_values(".env")
openai.api_key = config["OPENAI_API_KEY"]


def main():
    messages = []
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
