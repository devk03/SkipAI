import re
import random

# sample_transcript = "WEBVTT\n\n00:00:08.760 --> 00:00:10.280\nHello, good morning.\n\n00:00:10.280 --> 00:00:12.540\nThanks for coming to class,\n\n00:00:12.540 --> 00:00:13.820\nor for watching it,\n\n00:00:13.820 --> 00:00:16.440\nthose of you out in TV land.\n\n00:00:16.440 --> 00:00:18.020\nOh my god, I had office hours.\n\n00:00:18.020 --> 00:00:20.380\nI don't really have office\nhours, but I will meet you\n\n00:00:20.380 --> 00:00:22.940\nanytime, any place.\nIf you just send me an email, we\n\n00:00:22.940 --> 00:00:24.900\ncan meet anytime, any place.\n\n00:00:24.900 --> 00:00:30.320\nSo I met someone last week at a\ncoffee\n\n00:00:30.320 --> 00:00:31.320\nshop.\n\n00:00:33.020 --> 00:00:37.520\nAnd they were asking the people\nthat work at the coffee shop,\n\n00:00:38.260 --> 00:00:42.020\nis Professor Honeyman here? I\nmean I'm sitting there like five\n\n00:00:42.020 --> 00:00:45.180\nfeet away from this person.\n\n00:00:45.180 --> 00:00:47.480\nSo when they sat down I said,\n\n00:00:47.480 --> 00:00:49.340\nare you watching lectures,\n\n"


def parse_transcript(transcript: str):
    """Parse the transcript and return a list of parsed blocks, grouped by 5."""
    # Split the transcript into blocks based on double newlines
    blocks = re.split(r"\n\n", transcript)

    # Remove the first element if it's the "WEBVTT" header or empty
    if blocks[0].startswith("WEBVTT") or not blocks[0].strip():
        blocks = blocks[1:]

    # Group the blocks into chunks of 5
    chunk_size = 5
    grouped_blocks = [
        blocks[i : i + chunk_size] for i in range(0, len(blocks), chunk_size)
    ]

    # Concatenate the blocks within each chunk, separated by double newlines
    concatenated_chunks = ["\n\n".join(chunk) for chunk in grouped_blocks]

    return concatenated_chunks


# Code to generate the timestamp ids
def extract_first_timestamp(text: str):
    """Extract the first timestamp from the text."""
    timestamp_pattern = r"\d{2}:\d{2}:\d{2}\.\d{3}"
    match = re.search(timestamp_pattern, text)
    if match:
        return match.group(0)  # Return the first matched timestamp
    else:
        return "No timestamp found"


def generate_timestamp_ids(blocks: str):
    """Generate a list of timestamp IDs from the blocks."""
    id_list = []
    meta_data = []
    id_counter = 0
    for block in blocks:
        meta_data.append(
            {"timestamp": extract_first_timestamp(block), "source": "caen lecture"}
        )
        # Generate a unique number for each block
        id_list.append(str(id_counter))
        id_counter += 1

    return id_list, meta_data
