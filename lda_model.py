from sklearn.feature_extraction.text import CountVectorizer
from sklearn.decomposition import LatentDirichletAllocation

documents = [
"machine learning and artificial intelligence",
"deep learning and neural networks",
"natural language processing and text analysis"
]

vectorizer = CountVectorizer()

X = vectorizer.fit_transform(documents)

lda = LatentDirichletAllocation(n_components=2)

lda.fit(X)

print("Topics learned")