from flask import Flask, request, jsonify
from flask_cors import CORS
from dotenv import load_dotenv, find_dotenv
from pathlib import Path
from utlities.parsing import parse_transcript, generate_timestamp_ids
import requests

"""Random enviroment variable stuff"""
# load_dotenv(".env.local")
# print(os.getenv("OPENAI_API_KEY"))
# client = OpenAI()


app = Flask(__name__)
CORS(app)


# ChromaDB call to add the transcript to the collection
def add_to_collection(documents, metadatas, ids):
    # Simulate a blocking I/O operation
    print("Thread: Adding the transcript to the collection...")
    collection.add(
        documents=documents,
        metadatas=metadatas,
        ids=ids,
    )


@app.route("/transcript", methods=["POST"])
def transcript():
    """Send the original transcript."""

    data = request.get_json()  # Get JSON data from the request
    transcript = data["transcript"]  # Extract the transcript from the data
    # Partition the transcript to vectorize
    concatenated_blocks = parse_transcript(transcript)
    # Add the partitioned transcript to the ChromaDB collection // There is no meta data
    id_list, meta_data = generate_timestamp_ids(concatenated_blocks)
    # Asynchronously add the transcript to the collection
    return jsonify({"message": "Success"})


# @app.route("/question", methods=["POST"])
# def question():
#     """Send the question to the OpenAI API."""
#     data = request.get_json()  # Get JSON data from the request
#     question = data["question"]
#     results = collection.query(query_texts=[question], n_results=3)
#     print(results)
#     return jsonify({"message": "Success"})


@app.route("/fetchLecture", methods=["GET"])
def fetch_lecture():
    url = "https://leccap.engin.umich.edu/leccap/player/api/webvtt/?rk=bN2TOQ"
    cookies = {
        "PHPSESSID": "3el5k9sh8hb0s0qvebd5eo3dou",
        "AWSALB": "your_AWSALB_value_here",
        "AWSALBCORS": "your_AWSALBCORS_value_here",
        "__cf_bm": "your___cf_bm_value_here",
    }

    response = requests.get(url, cookies=cookies)
    if response.status_code == 200:
        return response.text


if __name__ == "__main__":
    app.run(debug=True, port=5000)
