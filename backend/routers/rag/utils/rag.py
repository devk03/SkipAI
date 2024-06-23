import os
from dotenv import load_dotenv
import time

load_dotenv()
from langchain.text_splitter import CharacterTextSplitter
from langchain.schema import Document
from langchain_openai import OpenAIEmbeddings
from langchain_pinecone import PineconeVectorStore
from pinecone import ServerlessSpec
from pinecone.grpc import PineconeGRPC as Pinecone

# Initialize Pinecone and OpenAI embeddings
pc = Pinecone(api_key=os.environ.get("PINECONE_API_KEY"))
embeddings = OpenAIEmbeddings(
    model="text-embedding-3-small", openai_api_key=os.environ.get("OPENAI_API_KEY")
)


def chunkify(text: str):
    """Split the text into chunks based on the ##### delimiter."""
    chunks = text.split("#####")
    documents = [
        Document(page_content=chunk.strip()) for chunk in chunks if chunk.strip()
    ]
    return documents


def ensure_index_exists():
    """Check if the index exists, and create it if it doesn't."""
    index_name = "skip-ai"
    if index_name not in pc.list_indexes().names():
        pc.create_index(
            name=index_name,
            dimension=1536,
            metric="cosine",
            spec=ServerlessSpec(cloud="aws", region="us-east-1"),
        )
    return index_name


def embed_chunks(chunks: list, index_name: str):
    """Embed chunks and store them in Pinecone."""
    namespace = "ugrl6v"  # Unique key in the UMICH CAEN database
    PineconeVectorStore.from_documents(
        documents=chunks,
        index_name=index_name,
        embedding=embeddings,
        namespace=namespace,
    )
    time.sleep(1)
    return namespace


def query_pinecone(index_name: str, namespace: str):
    """Query the Pinecone index and print results."""
    index = pc.Index(index_name)
    results = []
    for ids in index.list(namespace=namespace):
        query = index.query(
            id=ids[0],
            namespace=namespace,
            top_k=1,
            include_values=True,
            include_metadata=True,
        )
        results.append(query)
    return results


def process_and_query_text(text: str):
    """Process text through the entire pipeline and query the results."""
    chunks = chunkify(text)
    indexName = ensure_index_exists()
    namespace = embed_chunks(chunks, indexName)
    print("Text processed and embedded successfully.")

    results = query_pinecone(indexName, namespace)
    print("Query results:")
    for result in results:
        print(result)


# Usage
if __name__ == "__main__":
    sample_text = "Your text here #####  More text here ##### Even more text"
    process_and_query_text(sample_text)
