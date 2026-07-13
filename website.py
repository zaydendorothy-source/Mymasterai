from flask import Flask, render_template, request
import json
import os

from ai import AI
from memory import Memory
from websearch import WebSearch
from file_reader import FileReader


app = Flask(__name__)

ai = AI()
memory = Memory()
web = WebSearch()
reader = FileReader()


CHAT_FILE = "chat_history.json"


def load_chat():
    if os.path.exists(CHAT_FILE):
        try:
            with open(CHAT_FILE, "r", encoding="utf-8") as file:
                return json.load(file)
        except:
            return []
    return []


def save_chat(history):
    with open(CHAT_FILE, "w", encoding="utf-8") as file:
        json.dump(history, file, indent=4)


chat_history = load_chat()


@app.route("/", methods=["GET", "POST"])
def home():

    if request.method == "POST":

        message = request.form.get("message", "")

        chat_history.append({
            "role": "user",
            "text": message
        })


        answer = ai.ask(
            message,
            memory.list()
        )


        chat_history.append({
            "role": "ai",
            "text": answer
        })


        save_chat(chat_history)


    return render_template(
        "index.html",
        history=chat_history
    )


@app.route("/clear", methods=["POST"])
def clear_chat():

    global chat_history

    chat_history = []

    save_chat(chat_history)

    return render_template(
        "index.html",
        history=chat_history
    )


if __name__ == "__main__":

    app.run(
        host="0.0.0.0",
        port=5000
    )