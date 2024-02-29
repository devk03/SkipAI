from flask import Flask
# from openai import OpenAI

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
