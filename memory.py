import os
from pinecone import Pinecone

# Initialize Pinecone
pc = Pinecone(api_key="Your_Api_key")  # Replace YOUR_API_KEY with actual key
index = pc.Index("visa-guide-index")

def add_to_memory(user_input, agent_response):
    record_id = f"id-{user_input[:8]}"  # First 8 chars for ID
    dummy_vector = [0.001] * 768  # Small non-zero values
    index.upsert(vectors=[(record_id, dummy_vector, {'text': f"User: {user_input} | Agent: {agent_response}"})])
    print("Data added to Pinecone.")

def search_memory(query):
    dummy_query_vector = [0.001] * 768  # Must not be all zeros
    result = index.query(vector=dummy_query_vector, top_k=1, include_metadata=True)
    if result['matches']:
        return result['matches'][0]['metadata']['text']
    return "No relevant memory found."

