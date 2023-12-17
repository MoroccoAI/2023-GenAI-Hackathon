from flask import Flask, request, jsonify
import faiss
import json
from sentence_transformers import SentenceTransformer
from angle_emb import AnglE, Prompts
import pandas as pd
import numpy as np

app = Flask(__name__)

# Load the FAISS index and data
def load_faiss_index(file_path):
    return faiss.read_index(file_path)


index = load_faiss_index('questions_index.faiss')
data = pd.read_csv("first_aid.tsv", delimiter="\t")
model = SentenceTransformer('BAAI/bge-large-en-v1.5')


# Encode query
def encode_question(question):
    vec = model.encode(question, normalize_embeddings=True)
    return vec

# Search for similar questions
def search_similar_questions(query, k=10):
    encoded_query = encode_question(query).reshape(1, -1)
    distances, indices = index.search(encoded_query, k)
    

    hits = [{'corpus_id': id, 'score': score} for id, score in zip(indices[0], distances[0])]
    hits = sorted(hits, key=lambda x: x['score'], reverse=True)

    # Print out the hits
    print("Hits (sorted by score):")
    for hit in hits:
        print(hit)

    results = []
    for hit in hits:
        idx = hit['corpus_id']
        results.append({
            "question": data.iloc[idx]['pattern'],
            "answer": data.iloc[idx]['responses'],
            "similarity": float(hit['score'])  # Using the similarity score
        })
    return results

# Define the route
@app.route('/query', methods=['POST'])
def query():
    user_query = request.json.get('query')
    similar_questions = search_similar_questions(user_query)
    return jsonify(similar_questions)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8888, debug=True)


