import os
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

class DocumentIndexer:
    def __init__(self, folder_path):
        self.folder_path = folder_path
        self.documents = self.load_documents()
        self.vectorizer = TfidfVectorizer(stop_words='english', token_pattern=r"(?u)\b\w+\b")
        self.tfidf_matrix = self.calculate_tfidf_matrix()
        self.index = self.build_index()

    def load_documents(self):
        documents = []
        for filename in os.listdir(self.folder_path):
            with open(os.path.join(self.folder_path, filename), 'rb') as file:
                document_content = file.read().decode('utf-8', errors='ignore')
                documents.append((filename, document_content))  # Store filename along with content
        return documents

    def calculate_tfidf_matrix(self):
        return self.vectorizer.fit_transform([doc[1] for doc in self.documents])

    def build_index(self):
        index = {}
        terms = self.vectorizer.get_feature_names_out()
        for filename, content in self.documents:
            document_index = {}
            tfidf_scores = self.tfidf_matrix[self.documents.index((filename, content))].toarray()[0]  # Get TF-IDF scores for the current document
            for j, term in enumerate(terms):
                tfidf_score = tfidf_scores[j]
                if tfidf_score > 0:
                    document_index[term] = tfidf_score
            index[filename] = document_index
        return index

    def save_to_pickle(self, output_file):
        with open(output_file, 'wb') as f:
            pickle.dump({
                'index': self.index,
                'document_names': [doc[0] for doc in self.documents],
                'tfidf_matrix': self.tfidf_matrix,
                'cosine_similarity': self.calculate_cosine_similarity(),
                'tfidf_vectorizer': self.vectorizer
            }, f)

    def print_tfidf_scores(self):
        terms = self.vectorizer.get_feature_names_out()
        for doc_name, doc_index in self.index.items():
            print(f"Document: {doc_name}")
            for term in terms:
                if term in doc_index:
                    print(f"\tTerm: {term}, TF-IDF Score: {doc_index[term]}")

    def calculate_cosine_similarity(self):
        cosine_similarities = cosine_similarity(self.tfidf_matrix, self.tfidf_matrix)
        return cosine_similarities

    def print_top_similar_documents(self):
        cosine_similarities = self.calculate_cosine_similarity()
        doc_names = list(self.index.keys())
        for i, doc_name in enumerate(doc_names):
            print(f"Document: {doc_name}")
            similar_docs_indices = np.argsort(cosine_similarities[i])[-4:-1][::-1]  # Excluding self
            for j, idx in enumerate(similar_docs_indices):
                if idx != i:
                    similar_doc_name = doc_names[idx]
                    similarity_score = cosine_similarities[i, idx]
                    print(f"\tSimilar Document {j+1}: {similar_doc_name}, Cosine Similarity: {similarity_score:.4f}")

# Usage
indexer = DocumentIndexer('output')  # Assuming 'output' is the folder containing HTML files
indexer.print_tfidf_scores()
print("\n")
indexer.print_top_similar_documents()
indexer.save_to_pickle('index.pickle')  # Save index to a pickle file
