import json
import threading

from llm import ask_llm
from prompt_builder import build_prompt
from reminder import run_scheduler


def load_character():

    with open("characters/monday.json", "r", encoding="utf-8") as f:
        return json.load(f)


def chatbot():

    character = load_character()

    print(f"{character['name']} Tutor 시작")
    print("종료하려면 exit 입력\n")

    while True:

        user_input = input("You: ")

        if user_input.lower() == "exit":
            break

        prompt = build_prompt(character, user_input)

        response = ask_llm(prompt)

        print(f"{character['name']}: {response}\n")


if __name__ == "__main__":

    scheduler_thread = threading.Thread(target=run_scheduler)
    scheduler_thread.daemon = True
    scheduler_thread.start()

    chatbot()