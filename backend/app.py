from flask import Flask, request, jsonify
import openai
import os
from dotenv import load_dotenv, find_dotenv
from pathlib import Path

load_dotenv(".env.local")
print(os.getenv("OPENAI_API_KEY"))

# client = OpenAI()
app = Flask(__name__)


@app.route("/transcript", methods=["POST"])
def transcript():
    """Send the original transcript."""
    print("transcript entering")
    data = request.get_json()  # Get JSON data from the request
    print("printing", data)
    return {"message": "Success"}


@app.route("/question", methods=["POST"])
def question():
    """Send the question to the OpenAI API."""
    print("hello")
    data = request.get_json()  # Get JSON data from the request
    print("printing", data)
    return jsonify({"message": "Success"})


if __name__ == "__main__":
    app.run(debug=True, port=5000)
