from google import genai
import dotenv
import os

dotenv.load_dotenv()

api_key = os.getenv("API_KEY")

client = genai.Client(api_key=api_key)


while True:
    user_input = input("User: ")
    if user_input.lower() in ["exit", "quit"]:
        break

    response = client.models.generate_content(model = "gemini-3.6-flash", contents = user_input)

    print("AI: ",response.text)