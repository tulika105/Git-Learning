import os
from dotenv import load_dotenv
from google import genai

# Load environment variables
load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    raise ValueError("❌ GEMINI_API_KEY not found. Please set it in your .env file.")

# Initialize client
client = genai.Client(api_key=API_KEY)

SYSTEM_PROMPT = """
You are a Git tutor. You ONLY answer questions related to Git and GitHub.

Keep your answers short, beginner-friendly, and always include the exact 
command when relevant.

If the user asks anything unrelated, politely say you can only help with Git.
"""

def ask_gemini(chat, user_message):
    response = chat.send_message(user_message)
    return response.text


def main():
    print("\n🤖 Git Tutor — Powered by Gemini")
    print("Ask me anything about Git! Type 'exit' to quit.\n")

    # Create chat session
    chat = client.chats.create(
        model="gemini-2.5-flash",
        config={
            "system_instruction": SYSTEM_PROMPT
        }
    )

    while True:
        user_input = input("You: ").strip()

        if user_input.lower() in ("exit", "quit"):
            print("\n Bye! Keep committing \n")
            break

        if not user_input:
            continue

        try:
            response = ask_gemini(chat, user_input)
            print(f"\nGit Tutor: {response}\n")

        except Exception as e:
            print(f"\n Error: {e}\n")


if __name__ == "__main__":
    main()