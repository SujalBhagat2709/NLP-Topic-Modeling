import matplotlib.pyplot as plt

topics = ["AI","ML","NLP"]

weights = [0.4,0.35,0.25]

plt.bar(topics,weights)

plt.title("Topic Distribution")

plt.show()