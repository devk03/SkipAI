from flask import Flask, request, jsonify
from concurrent.futures import ThreadPoolExecutor
import openai
import os
from dotenv import load_dotenv, find_dotenv
from pathlib import Path
from utlities.parsing import parse_transcript, generate_timestamp_ids
import chromadb


chroma_client = chromadb.Client()
collection = chroma_client.create_collection(name="transcript_blocks")
client = chromadb.PersistentClient(path="chroma.db")


"""Random enviroment variable stuff"""
# load_dotenv(".env.local")
# print(os.getenv("OPENAI_API_KEY"))
# client = OpenAI()


app = Flask(__name__)


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
    with ThreadPoolExecutor() as executor:
        future = executor.submit(
            add_to_collection, concatenated_blocks, meta_data, id_list
        )
        try:
            future.result()  # Wait for the result, raises exceptions if any
            return jsonify({"message": "Success"})
        except Exception as e:
            print(e)
            return (
                jsonify({"message": "Failed to add the transcript to the collection."}),
                500,
            )


@app.route("/question", methods=["POST"])
def question():
    """Send the question to the OpenAI API."""
    data = request.get_json()  # Get JSON data from the request
    question = data["question"]
    results = collection.query(query_texts=[question], n_results=3)
    print(results)
    return jsonify({"message": "Success"})


if __name__ == "__main__":
    app.run(debug=True, port=5000)
