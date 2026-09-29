from flask import Flask
import os
import random
import socket

app = Flask(__name__)

# read config from environment variables set at "docker run" time.
# these have sensible defaults so the app still works if they're not set.
APP_NAME = os.environ.get("APP_NAME", "Dice Duel")
DICE_SIDES = int(os.environ.get("DICE_SIDES", 6))


@app.route("/")
def home():
    hostname = socket.gethostname()

    # two dice rolled every time the page loads/refreshes
    roll_1 = random.randint(1, DICE_SIDES)
    roll_2 = random.randint(1, DICE_SIDES)
    total = roll_1 + roll_2

    if roll_1 > roll_2:
        result = "Player 1 wins this round!"
    elif roll_2 > roll_1:
        result = "Player 2 wins this round!"
    else:
        result = "It's a tie!"

    return f"""
    <html>
        <head><title>{APP_NAME} - Task 4.3</title></head>
        <body style="font-family: sans-serif; text-align: center; margin-top: 80px;">
            <h1>{APP_NAME}</h1>
            <p style="font-size: 1.1em;">Rolling two D{DICE_SIDES} dice...</p>
            <h2>Player 1: {roll_1} &nbsp;|&nbsp; Player 2: {roll_2}</h2>
            <p>Total: {total}</p>
            <p style="font-size: 1.3em;"><b>{result}</b></p>
            <p><a href="/">Roll again</a></p>
            <hr style="width: 300px;">
            <p>Container hostname: <b>{hostname}</b></p>
            <p>Dice sides (from DICE_SIDES env var): {DICE_SIDES}</p>
        </body>
    </html>
    """


@app.route("/health")
def health():
    return {"status": "ok"}


if __name__ == "__main__":
    # bind to 0.0.0.0 so the port mapping from "docker run -p" actually works
    app.run(host="0.0.0.0", port=8000)
