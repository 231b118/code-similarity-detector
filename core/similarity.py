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

from core.preprocessing import clean_code, get_ast_representation

def compute_ast_similarity(code1, code2):
    ast1 = get_ast_representation(code1)
    ast2 = get_ast_representation(code2)

    if not ast1 or not ast2:
        return 0.0

    vectorizer = TfidfVectorizer()
    vectors = vectorizer.fit_transform([ast1, ast2])

    similarity = cosine_similarity(vectors[0], vectors[1])[0][0]

    return round(similarity * 100, 2)