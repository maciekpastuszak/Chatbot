import openai
from dotenv import dotenv_values

config = dotenv_values(".env")
openai.api_key = config["OPENAI_API_KEY"]

while True:
    try:
        user_input = input("You: ")
        res = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {
                    "role": "user",
                    "content": user_input,
                }
            ],
        )
    except KeyboardInterrupt:
        print("Exiting....")
        break

print(res)
