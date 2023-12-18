import faiss
import numpy as np
import json
import pandas as pd
from angle_emb import AnglE, Prompts
from sentence_transformers import SentenceTransformer


def encode_questions(questions):
    model = SentenceTransformer('BAAI/bge-large-en-v1.5')
    vecs  = model.encode(questions, normalize_embeddings=True, batch_size=512, show_progress_bar=True)

    return vecs

def create_faiss_hnsw_index(encoded_questions, m=32):
    dimension = encoded_questions.shape[1]
    quantizer = faiss.IndexFlatIP(dimension)
    index = faiss.IndexIVFFlat(quantizer, dimension, m, faiss.METRIC_INNER_PRODUCT)
    index.nprobe = 3
    index.verbose = True
    index.train(encoded_questions)
    index.add(encoded_questions)
    return index

def save_faiss_index(index, file_path):
    faiss.write_index(index, file_path)

if __name__ == "__main__":
    data = pd.read_csv("first_aid.tsv", delimiter="\t")
    questions = [item for item in data["pattern"]]
    encoded_questions = encode_questions(questions)
    index = create_faiss_hnsw_index(encoded_questions)
    save_faiss_index(index, 'questions_index.faiss')
