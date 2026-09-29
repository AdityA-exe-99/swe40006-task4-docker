from flask import Flask
import socket
import random
import datetime

app = Flask(__name__)

# a small set of game-development quotes/tips this app serves up randomly.
# ties this container into a "GameDev Toolkit" theme used across Task 4.
QUOTES = [
    "A game is a series of interesting decisions. - Sid Meier",
    "Fun is just another word for learning. - Raph Koster",
    "Playtest early, playtest often. Your first build is never the fun one.",
    "Good game feel comes from juice: sound, particles, screen shake, feedback.",
    "Ship something small before you ship something ambitious.",
    "A bug the player never sees might as well not exist, prioritise accordingly.",
    "Prototyping is cheaper than arguing about design on paper.",
    "The best level design teaches the player without a tutorial popup.",
]

# in-memory counter, resets whenever the container restarts.
# good enough to demonstrate container state without needing a database.
hit_count = 0


@app.route("/")
def home():
    global hit_count
    hit_count += 1

    hostname = socket.gethostname()
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    quote = random.choice(QUOTES)

    return f"""
    <html>
        <head><title>GameDev Quote Generator - Task 4.2</title></head>
        <body style="font-family: sans-serif; text-align: center; margin-top: 80px;">
            <h1>GameDev Quote Generator</h1>
            <p style="font-size: 1.2em; max-width: 600px; margin: 20px auto;">"{quote}"</p>
            <hr style="width: 300px;">
            <p>Served by container: <b>{hostname}</b></p>
            <p>Requests handled by this container: <b>{hit_count}</b></p>
            <p>Server time: {now}</p>
        </body>
    </html>
    """


@app.route("/health")
def health():
    return {"status": "ok", "hits": hit_count}


if __name__ == "__main__":
    # 0.0.0.0 is required so the container's port mapping actually works.
    # Binding to 127.0.0.1 would make the app unreachable from outside the
    # container, which is one of the known problems in the walkthrough.
    app.run(host="0.0.0.0", port=5000)
