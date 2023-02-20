from sklearn.feature_extraction.text import CountVectorizer
from sentence_transformers import SentenceTransformer

from basic_keybert_1 import basic_keybert
from max_sum_similarity_2 import max_sum_sim
from maximal_marginal_relevance_3 import mmr
from korean_stopwords import korean_stopwords
from doc import doc

if __name__ == "__main__":
    # 1개의 단일 단어 추출
    n_gram_range = (1, 1)
    # stop_words = "english"
    stop_words = korean_stopwords

    count = CountVectorizer(ngram_range=n_gram_range, stop_words=stop_words).fit([doc])
    candidates = count.get_feature_names_out()

    print("trigram 개수 :", len(candidates))
    print("trigram 다섯개만 출력 :", candidates[:5])

    model = SentenceTransformer("distilbert-base-nli-mean-tokens")
    doc_embedding = model.encode([doc])
    candidate_embeddings = model.encode(candidates)

    basic_keybert(doc_embedding, candidate_embeddings, candidates)

    max_sum_sim(
        doc_embedding,
        candidate_embeddings,
        candidates,
        top_n=5,
        nr_candidates=10,
        candidates=candidates,
    )

    mmr(doc_embedding, candidate_embeddings, candidates, top_n=5, diversity=0.2)
