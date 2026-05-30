import os
import random
from dotenv import load_dotenv
from google import genai
from rich.console import Console
from rich.markdown import Markdown
from rich.panel import Panel
from rich.prompt import Prompt

console = Console()

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


def run_quiz(client):
    console.print(Panel.fit("[bold yellow]✏️ Git Quiz Mode[/bold yellow]\nI will ask you a question. Answer it, or type [bold red]'exit'[/bold red] to return to chat.", title="Quiz Mode", border_style="yellow"))
    
    quiz_chat = client.chats.create(
        model="gemini-2.5-flash",
        config={
            "system_instruction": "You are a Git quiz master. Generate a single beginner-to-intermediate level multiple choice or scenario question about Git/GitHub. Present the question and choice options clearly. Do not show the correct answer or explanation yet. Wait for the user's response."
        }
    )
    
    while True:
        with console.status("[bold yellow]Generating a question...[/bold yellow]"):
            try:
                question = quiz_chat.send_message("Generate a new quiz question.")
                question_text = question.text
            except Exception as e:
                console.print(f"\n[bold red]❌ Error generating question: {e}[/bold red]\n")
                break
        
        console.print("\n", Panel(Markdown(question_text), title="[bold yellow]Question[/bold yellow]", border_style="yellow"))
        
        user_answer = Prompt.ask("\n[bold green]Your Answer[/bold green]").strip()
        
        if user_answer.lower() in ("exit", "quit"):
            console.print("[bold yellow]Leaving Quiz Mode. Back to Git Tutor chat![/bold yellow]\n")
            break
            
        if not user_answer:
            continue
            
        with console.status("[bold cyan]Evaluating your answer...[/bold cyan]"):
            try:
                evaluation = quiz_chat.send_message(f"Here is my answer: {user_answer}. Please evaluate it. Tell me if it's correct or incorrect, explain why, and state the correct answer clearly.")
                evaluation_text = evaluation.text
            except Exception as e:
                console.print(f"\n[bold red]❌ Error evaluating answer: {e}[/bold red]\n")
                break
                
        console.print("\n", Panel(Markdown(evaluation_text), title="[bold cyan]Evaluation[/bold cyan]", border_style="cyan"))
        
        play_again = Prompt.ask("\nDo you want to try another question? (y/n)", choices=["y", "n"], default="y")
        if play_again.lower() != "y":
            console.print("[bold yellow]Leaving Quiz Mode. Back to Git Tutor chat![/bold yellow]\n")
            break


def main():
    console.print(Panel.fit("[bold blue]🤖 Git Tutor — Powered by Gemini[/bold blue]\nAsk me anything about Git! Type [bold yellow]'/quiz'[/bold yellow] to test your knowledge or [bold red]'exit'[/bold red] to quit.", title="Welcome", border_style="blue"))

    # Create chat session
    chat = client.chats.create(
        model="gemini-2.5-flash",
        config={
            "system_instruction": SYSTEM_PROMPT
        }
    )

    while True:
        user_input = Prompt.ask("\n[bold green]You[/bold green]").strip()

        if user_input.lower() in ("exit", "quit"):
            goodbyes = [
                "👋 Bye! Keep committing! 🚀",
                "✌️ Happy branching! May your merges always be clean.",
                "🎯 See ya! Don't forget to push your changes! 📤",
                "😄 Goodbye! Remember: commit early, commit often!",
                "🌟 Adios! Git gud out there! 😎",
                "📚 Later! Keep rebasing wisely and writing legendary commit messages.",
                "🧩 Bye for now! Keep your branches tidy and your commits meaningful."
            ]
            console.print(f"\n[bold magenta]{random.choice(goodbyes)}[/bold magenta]\n")
            break

        if user_input.lower() in ("/quiz", "quiz"):
            run_quiz(client)
            continue

        if not user_input:
            continue

        try:
            response = ask_gemini(chat, user_input)
            console.print("\n", Panel(Markdown(response), title="[bold cyan]Git Tutor[/bold cyan]", border_style="cyan"))

        except Exception as e:
            console.print(f"\n[bold red]❌ Error: {e}[/bold red]\n")


if __name__ == "__main__":
    main()