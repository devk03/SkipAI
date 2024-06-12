from fastapi import APIRouter, Request
from .utils.parsing import removeTimestamps
import requests

router = APIRouter()

@router.post("/lecture")
async def fetch_lecture(request: Request):
    # Parse the JSON body
    body = await request.json()

    # Get the specific PHPSESSID from the JSON body
    PHPSESSID = body.get("PHPSESSID")

    if not PHPSESSID:
        return {"error": "PHPSESSID not found in request body"}

    url = "https://leccap.engin.umich.edu/leccap/player/api/webvtt/?rk=ugrl6v"

    # Use the extracted PHPSESSID to make the request
    response = requests.get(url, cookies={"PHPSESSID": PHPSESSID})

    # Parse the content of all timestamps from the response
    rawTranscript = removeTimestamps(response.content.decode('utf-8'))
    print(rawTranscript)
    return {"content": rawTranscript}
