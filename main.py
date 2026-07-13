from website import app


if __name__ == "__main__":

    print("Starting MyAI Website...")
    print("Open your browser and go to:")
    print("http://127.0.0.1:5000")

    app.run(
        host="0.0.0.0",
        port=5000
    )