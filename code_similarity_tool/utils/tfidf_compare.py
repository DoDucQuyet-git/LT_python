from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def calculate_tfidf_similarity(texts):
    """So sánh logic bằng TF-IDF."""
    try:
        # token_pattern giúp nhận diện cả từ 1 ký tự và tiếng Việt tốt hơn
        vectorizer = TfidfVectorizer(token_pattern=r"(?u)\b\w+\b")
        tfidf_matrix = vectorizer.fit_transform(texts)
        return cosine_similarity(tfidf_matrix)
    except ValueError:
        # Trường hợp file rỗng hoặc toàn stop words
        import numpy as np
        return np.zeros((len(texts), len(texts)))