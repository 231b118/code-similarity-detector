from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from core.preprocessing import clean_code

def compute_similarity(code1, code2):
    code1 = clean_code(code1)
    code2 = clean_code(code2)

    vectorizer = TfidfVectorizer()
    vectors = vectorizer.fit_transform([code1, code2])

    similarity = cosine_similarity(vectors[0], vectors[1])[0][0]

    return round(similarity * 100, 2)