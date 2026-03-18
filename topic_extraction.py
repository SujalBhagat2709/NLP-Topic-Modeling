import numpy as np

words = ["machine","learning","ai","deep","network"]

topic_weights = np.random.rand(5)

topics = list(zip(words, topic_weights))

print(topics)