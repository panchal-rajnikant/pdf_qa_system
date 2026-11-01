from sentence_transformers import SentenceTransformer 
import numpy as np

model = SentenceTransformer("all-MiniLM-l6-v2")

text = [chunk["text"] from chunk in all_chunks]


embeddings = model.encode(texts)

print(embeddings.shape)

def cosine_similarity(a, b):
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

def retrieve(query, model, chunks, embedings, top_k=3):
    
    query_embedding = model.encode([query])[0]

    scores = []
    for index, embedding in enumerate(embeddings):
        score = cosine_similarity(query_embedding, embedding)

        scores.append((score, index))

    scores.sort(reverse= True)

    results = []

    for score, index in scores[:top_k]:

        results.append({
            "text": chunks[index]["text"],
            "score": float(score),
            "source": chunks[index]["source"]
        })

    return results