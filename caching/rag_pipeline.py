"""
RAG Pipeline Implementation
This module handles document processing, chunking, and retrieval for the RAG system.
"""

import redis
import json
from datetime import datetime
from sentence_transformers import SentenceTransformer
import numpy as np

# Initialize components
redis_client = redis.Redis(host='localhost', port=6379, db=0, decode_responses=True)
model = SentenceTransformer('all-MiniLM-L6-v2')


def get_embedding(text):
    """
    Generate embedding vector for given text using sentence-transformers.
    
    Args:
        text (str): Input text to embed
        
    Returns:
        list: Embedding vector as a list of floats
        
    TODO:
    - Use the model.encode() method to generate embeddings
    - Convert numpy array to list before returning
    - Handle empty text edge case
    """
    
    if not text:
        return []
    
    embedding = model.encode(text)
    embedding_vectors = embedding.tolist()

    return embedding_vectors


def chunk_document(text, chunk_size=500, overlap=50):
    """
    Split a document into overlapping chunks for better retrieval.
    
    Args:
        text (str): Full document text
        chunk_size (int): Number of words per chunk
        overlap (int): Number of overlapping words between chunks
        
    Returns:
        list: List of text chunks
        
    TODO:
    - Split text into words
    - Create chunks with specified size and overlap
    - Handle edge cases (text shorter than chunk_size)
    - Return list of chunk strings
    
    Example:
        text = "word1 word2 word3 word4 word5"
        chunk_size = 3, overlap = 1
        Result: ["word1 word2 word3", "word3 word4 word5"]
    """
    
    if text is None:
        return []
    
    text = text.strip()
    if not text:
        return []
    
    if chunk_size <= 0:
        raise ValueError("chunk size must be > 0")
    if overlap < 0:
        raise ValueError("overlap must be >= 0")
    if overlap >= chunk_size:
        raise ValueError("overlap must be smaller than chunk size")
    
    words = text.split()
    if len(words) <= chunk_size:
        return [" ".join(words)]
    
    chunks = []
    step = chunk_size - overlap

    for start in range(0, len(words), step):
        end = start + chunk_size
        chunkWords = words[start:end]
        if not chunkWords:
            break
        chunks.append(" ".join(chunkWords))
        if end >= len(words):
            break
    
    return chunks


def add_document_to_store(filename, content):
    """
    Process a document, chunk it, generate embeddings, and store in Redis.
    
    Args:
        filename (str): Name of the document
        content (str): Full text content of the document
        
    Returns:
        int: Number of chunks created
        
    TODO:
    - Call chunk_document() to split the content
    - For each chunk:
        * Generate embedding using get_embedding()
        * Create a unique Redis key like "doc:{filename}:chunk:{i}"
        * Store chunk data as JSON with fields:
            - filename
            - chunk_id
            - content
            - embedding
            - timestamp
    - Return the total number of chunks created
    """
    
    chunks = chunk_document(content)

    for i, chunk in enumerate(chunks):
        embedding = get_embedding(chunk)
        redisKey = f"doc:{filename}:chunk:{i}"
        
        chunkData = {
            "filename": filename,
            "chunk_id": i,
            "content": chunk,
            "embedding": embedding,
            "timestamp": datetime.utcnow().isoformat()
        }

        redis_client.set(redisKey, json.dumps(chunkData))

    return len(chunks)


def retrieve_relevant_context(query, top_k=3):
    """
    Find the most relevant document chunks for a given query using semantic search.
    
    Args:
        query (str): User's question/prompt
        top_k (int): Number of top chunks to return
        
    Returns:
        list: List of tuples (chunk_content, similarity_score)
        
    TODO:
    - Generate embedding for the query
    - Get all document chunks from Redis (keys matching "doc:*:chunk:*")
    - For each chunk:
        * Load the chunk data from Redis
        * Calculate cosine similarity with query embedding
        * Store (similarity, chunk_content) tuple
    - Sort by similarity (highest first)
    - Return top_k chunks with their similarity scores
    """
    
    queryEmbedding = get_embedding(query)
    if not queryEmbedding:
        return []
    
    scoredChunks = []

    for key in redis_client.scan_iter("doc:*:chunk:*"):
        rawChunk = redis_client.get(key)
        if not rawChunk:
            continue

        chunkData = json.loads(rawChunk)
        chunkEmbedding = chunkData.get("embedding", [])
        chunkContent = chunkData.get("content", "")

        similarity = cosine_similarity(queryEmbedding, chunkEmbedding)
        scoredChunks.append((chunkContent, similarity))

    scoredChunks.sort(key=lambda x:x[1], reverse=True)
    return scoredChunks[:top_k]


def cosine_similarity(vec1, vec2):
    """
    Calculate cosine similarity between two vectors.
    
    Args:
        vec1 (list): First embedding vector
        vec2 (list): Second embedding vector
        
    Returns:
        float: Similarity score between 0 and 1
        
    TODO:
    - Convert lists to numpy arrays
    - Calculate dot product of the two vectors
    - Calculate magnitude (norm) of each vector
    - Return: dot_product / (norm1 * norm2)
    
    Formula: cos(θ) = (A · B) / (||A|| * ||B||)
    """

    if vec1 is None or vec2 is None:
        return 0.0
    if len(vec1) == 0 or len(vec2) == 0:
        return 0.0
    if len(vec1) != len(vec2):
        raise ValueError("vectors must have the same length")
    
    vector1, vector2 = np.array(vec1, dtype=float), np.array(vec2, dtype=float)
    norm1, norm2 = np.linalg.norm(vector1), np.linalg.norm(vector2)
    if norm1 == 0.0 or norm2 == 0.0:
        return 0.0
    
    dot_product = np.dot(vector1, vector2)
    cosine_similarity =  dot_product / (norm1 * norm2)

    return cosine_similarity


def get_all_documents():
    """
    Get list of all documents in the store.
    
    Returns:
        list: List of document filenames
        
    TODO:
    - Get all keys matching "doc:*:chunk:0" (first chunk of each doc)
    - Extract unique filenames from the keys
    - Return list of filenames
    """
    
    filenames = set()

    for key in redis_client.scan_iter("doc:*:chunk:0"):
        parts = key.split(":")
        if len(parts) >= 4:
            filenames.add(parts[1])

    return sorted(filenames)


def delete_document(filename):
    """
    Remove a document and all its chunks from Redis.
    
    Args:
        filename (str): Name of document to delete
        
    Returns:
        int: Number of chunks deleted
        
    TODO:
    - Find all keys matching "doc:{filename}:chunk:*"
    - Delete all matching keys from Redis
    - Return count of deleted chunks
    """
    pass


def get_document_stats():
    """
    Get statistics about documents in the store.
    
    Returns:
        dict: Dictionary with stats:
            - total_documents: number of unique documents
            - total_chunks: total number of chunks
            - avg_chunks_per_doc: average chunks per document
            
    TODO:
    - Count unique documents
    - Count total chunks
    - Calculate average
    - Return stats dictionary
    """
    pass