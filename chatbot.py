import openai
from dotenv import dotenv_values

config = dotenv_values(".env")
openai.api_key = config["OPENAI_API_KEY"]

response = openai.ChatCompletion.create(
    model="gpt-4",
    messages=[{"role": "user", "content": "What is the best color on earth according to different countries?"}],
)

while True:
    try:
    except KeyboardInterrupt:
        print("Exiting....")
        break
print(response)
