import numpy as np
import itertools

from sklearn.metrics.pairwise import cosine_similarity


def max_sum_sim(
    doc_embedding, candidate_embeddings, words, top_n, nr_candidates, candidates
):
    # 문서와 각 키워드들 간의 유사도
    distances = cosine_similarity(doc_embedding, candidate_embeddings)

    # 각 키워드들 간의 유사도
    distances_candidates = cosine_similarity(candidate_embeddings, candidate_embeddings)

    # 코사인 유사도에 기반하여 키워드들 중 상위 top_n개의 단어를 pick.
    words_idx = list(distances.argsort()[0][-nr_candidates:])
    words_vals = [candidates[index] for index in words_idx]
    distances_candidates = distances_candidates[np.ix_(words_idx, words_idx)]

    # 각 키워드들 중에서 가장 덜 유사한 키워드들간의 조합을 계산
    min_sim = np.inf
    candidate = None
    for combination in itertools.combinations(range(len(words_idx)), top_n):
        sim = sum(
            [
                distances_candidates[i][j]
                for i in combination
                for j in combination
                if i != j
            ]
        )
        if sim < min_sim:
            candidate = combination
            min_sim = sim

    print([words_vals[idx] for idx in candidate])
