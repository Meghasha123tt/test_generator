# google_sentence_encoder.py

import tensorflow as tf
import tensorflow_text as text

class GoogleSentenceEncoder:
    def __init__(self):
        self.model = self.load_model()

    def load_model(self):
        # Load the Universal Sentence Encoder model
        model = tf.saved_model.load("https://tfhub.dev/google/universal-sentence-encoder-multilingual/3")
        return model

    def generate_embeddings(self, sentences):
        # Generate embeddings for the given sentences
        embeddings = self.model(sentences)
        return embeddings.numpy()

# Example usage
if __name__ == "__main__":
    sentences = ["This is a sample sentence.", "Another example sentence."]
    
    encoder = GoogleSentenceEncoder()
    embeddings = encoder.generate_embeddings(sentences)

    print("Sentence Embeddings:")
    for i, embedding in enumerate(embeddings):
        print(f"Sentence {i + 1}: {embedding}")
