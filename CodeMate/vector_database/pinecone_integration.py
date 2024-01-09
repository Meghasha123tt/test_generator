# pinecone_integration.py

import pinecone

class PineconeIntegration:
    def __init__(self, api_key, index_name):
        self.api_key = api_key
        self.index_name = index_name
        self.pinecone_client = self.initialize_pinecone()

    def initialize_pinecone(self):
        pinecone.init(api_key=self.api_key)
        return pinecone.Index(index_name=self.index_name)

    def store_embeddings(self, vectors, ids):
        # Store embeddings in Pinecone
        self.pinecone_client.upsert(items=zip(ids, vectors))

    def search_embeddings(self, query_vector, top_k=5):
        # Search for similar embeddings in Pinecone
        results = self.pinecone_client.query(queries=[query_vector], top_k=top_k)
        return results[0].matches

# Example usage
if __name__ == "__main__":
    # Replace 'YOUR_API_KEY' and 'YOUR_INDEX_NAME' with your Pinecone API key and index name
    pinecone_api_key = 'bfb0ebdf-1c02-480c-a4a1-755bd33bbff0'
    pinecone_index_name = 'gcp-starter'

    pinecone_integration = PineconeIntegration(api_key=pinecone_api_key, index_name=pinecone_index_name)

    # Example vectors and IDs
    sample_vectors = [[0.1, 0.2, 0.3], [0.4, 0.5, 0.6]]
    sample_ids = ["id1", "id2"]

    # Store embeddings
    pinecone_integration.store_embeddings(sample_vectors, sample_ids)

    # Example search
    query_vector = [0.2, 0.3, 0.4]
    search_results = pinecone_integration.search_embeddings(query_vector)

    print("Search Results:")
    for match in search_results:
        print(f"ID: {match.id}, Score: {match.score}")
