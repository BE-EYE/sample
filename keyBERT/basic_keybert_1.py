from sklearn.metrics.pairwise import cosine_similarity
from sentence_transformers import SentenceTransformer


def basic_keybert(doc_embedding, candidate_embeddings, candidates):
    top_n = 5
    distances = cosine_similarity(doc_embedding, candidate_embeddings)
    keywords = [candidates[index] for index in distances.argsort()[0][-top_n:]]
    print(keywords)
