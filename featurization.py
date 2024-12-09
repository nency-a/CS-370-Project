from sentence_transformers import SentenceTransformer
import pymongo
import re
from qdrant_client import QdrantClient

def cleanData(data: dict):
    content = data["Content"]
    content = re.sub(r'http\S+', 'URL_PLACEHOLDER', content)   
    content = content.translate(str.maketrans('', '', string.punctuation))
    content = content.encode("ascii", "ignore").decode()
    content = re.sub(r'\s+', ' ', content).strip()  

    data["CleanedContent"] = content
    return data

def chunkData(data: dict):
    content = data["CleanedContent"]
    chunk_size = 500  # This needs to be revised
    chunks = [content[i:i + chunk_size] for i in range(0, len(content), chunk_size)]
    data["Chunks"] = chunks
    return data

def embedData(data: dict):
    model = SentenceTransformer('all-MiniLM-L6-v2')
    embeddings = [model.encode(chunk) for chunk in data["Chunks"]]
    data["Embeddings"] = embeddings
    return data

def loadToQdrant(data: dict):
    qdrant_client = QdrantClient(url="http://localhost:27017")
    vector_data = []
    for idx, embedding in enumerate(data["Embeddings"]):
        point = {
            'id': f"{data['_id']}_chunk_{idx}",
            'vector': embedding,
            'payload': {
                'url': data["URL"],
                'title': data["Title"],
                'content_chunk': data["Chunks"][idx]
            }
        }
        vector_data.append(point)
    
    qdrant_client.upsert(collection_name="articles", points=vector_data)
    return data

def main(link: str):
    data = crawlArticle(link) 
    cleaned_data = cleanData(data)
    chunked_data = chunkData(cleaned_data)
    embedded_data = embedData(chunked_data)
    loadToQdrant(embedded_data)

if __name__ == "__main__":
    main("https://www.ros.org/blog/getting-started/")
    main("https://docs.nav2.org/development_guides/devcontainer_docs/index.html")
