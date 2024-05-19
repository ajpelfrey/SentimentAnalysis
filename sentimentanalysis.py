from transformers import pipeline

# Load pre-trained sentiment-analysis model
classifier = pipeline('sentiment-analysis')

# Define some example texts
texts = [
    "I love this product! It's fantastic.",
    "This is good food, I enjoy it a lot.",
    "This is the worst experience I've ever had.",
    "The service was okay, nothing special."
]

# Classify the texts
for text in texts:
    result = classifier(text)[0]
    print(f"Text: {text}\nLabel: {result['label']}, Score: {result['score']:.4f}\n")
