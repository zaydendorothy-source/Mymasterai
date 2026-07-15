from flask import Flask, render_template, request, redirect
from werkzeug.utils import secure_filename
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
UPLOAD_FOLDER = "uploads"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)


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
        deep = request.form.get("deep") == "on"

        image = request.files.get("image")

        if image and image.filename != "":
            filename = secure_filename(image.filename)
            image_path = os.path.join(UPLOAD_FOLDER, filename)
            image.save(image_path)

            message += f"\n\n[User uploaded image: {filename}]"

        chat_history.append({
            "role": "user",
            "text": message
        })

        answer = ai.ask(
            message,
            memory.list(),
            deep
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


@app.route("/new_chat", methods=["POST"])
def new_chat():

    global chat_history

    chat_history = []

    save_chat(chat_history)

    return redirect("/")


@app.route("/clear", methods=["POST"])
def clear_chat():

    global chat_history

    chat_history = []

    save_chat(chat_history)

    return redirect("/")


if __name__ == "__main__":

    app.run(
        host="0.0.0.0",
        port=5000
    )
