from flask import Flask
import openai
import os
from dotenv import load_dotenv

load_dotenv()
# client = OpenAI()
app = Flask(__name__)


@app.route("/transcript")
def transcript():
    """Send the original transcript."""
    return {"message": "Success"}


@app.route("/question")
def hello_world():
    """Send the question to the OpenAI API."""
    return {"message": "Success"}


if __name__ == "__main__":
    app.run()
