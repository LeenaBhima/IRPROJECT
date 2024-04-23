import os
import pickle
from flask import Flask, request, jsonify
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
import re

app = Flask(__name__)

# Load the pre-built index
with open("index.pickle", "rb") as f:
    index_data = pickle.load(f)

index = index_data["index"]
document_names = index_data["document_names"]
tfidf_matrix = index_data["tfidf_matrix"]

# Function to validate the incoming query
def validate_query(query):
    if not isinstance(query, str):
        return False, "Query must be a string."
    if len(query.strip()) == 0:
        return False, "Query cannot be empty."
    if not re.match(r"^[\w\s.,'!?-]+$", query):
        return False, "Query contains invalid characters."
    return True, ""

# Route to process text-based queries
@app.route("/query", methods=["POST"])
def process_query():
    data = request.get_json()

    # Check if the query is provided in the expected format
    if "query" not in data:
        return jsonify({"error": "Missing 'query' field in request."}), 400

    query = data["query"]
    is_valid, error_msg = validate_query(query)

    if not is_valid:
        return jsonify({"error": error_msg}), 400

    # Convert query into TF-IDF vector
    query_vector = index_data["tfidf_vectorizer"].transform([query])

    # Calculate cosine similarity with the indexed documents
    cosine_similarities = cosine_similarity(query_vector, tfidf_matrix).flatten()

    # Get the Top-K documents based on cosine similarity
    K = 5  # You can change this to any number for the Top-K results
    top_k_indices = np.argsort(-cosine_similarities)[:K]
    top_k_results = [{"document": document_names[i], "similarity": cosine_similarities[i]} for i in top_k_indices]

    return jsonify({"top_5_results": top_k_results}), 200

if __name__ == "__main__":
    app.run(debug=True)
