# CacheGPT Implementation Guide

## 🎯 Learning Path

Complete the functions in this order for best learning experience:

### Phase 1: Foundation (Start Here!)
1. **rag_pipeline.py**
   - `get_embedding()` - Learn about sentence transformers
   - `cosine_similarity()` - Understand vector similarity
   - `chunk_document()` - Document processing basics

### Phase 2: Storage
2. **rag_pipeline.py** (continued)
   - `add_document_to_store()` - Redis storage patterns
   - `retrieve_relevant_context()` - Semantic search implementation
   - `get_all_documents()` - Basic Redis queries

### Phase 3: Caching Logic
3. **cache_tiers.py**
   - `determine_cache_tier()` - Threshold logic
   - `set_cache()` - Cache storage with TTL
   - `get_cache()` - Multi-tier cache lookup
   - `get_tier_statistics()` - Metrics calculation

### Phase 4: LLM Integration
4. **llm_wrapper.py**
   - `estimate_tokens()` - Token counting
   - `calculate_cost()` - Cost tracking
   - `build_rag_prompt()` - Context injection
   - `get_llm_response()` - Main orchestration function

### Phase 5: Metrics
5. **metrics_tracker.py**
   - `initialize_metrics()` - Setup
   - `update_query_metrics()` - Real-time tracking
   - `get_current_metrics()` - Frontend formatting

### Phase 6: API
6. **api.py**
   - Implement each endpoint one by one
   - Test with curl or Postman as you go

## 📚 Resources for Each Function

### Sentence Transformers
```python
# Example: How to use sentence-transformers
from sentence_transformers import SentenceTransformer
model = SentenceTransformer('all-MiniLM-L6-v2')
embedding = model.encode("Hello world")  # Returns numpy array
```

### Redis Operations
```python
# Store JSON in Redis
redis_client.set('key', json.dumps({'data': 'value'}))

# Get and parse JSON
data = json.loads(redis_client.get('key'))

# Set with TTL (time to live)
redis_client.setex('key', 3600, json.dumps(data))  # Expires in 1 hour

# Pattern matching
keys = redis_client.keys('cache:*')
```

### Cosine Similarity
```python
import numpy as np

# Formula: cos(θ) = (A · B) / (||A|| * ||B||)
def cosine_similarity(a, b):
    a = np.array(a)
    b = np.array(b)
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))
```

### OpenAI API
```python
from openai import OpenAI
client = OpenAI(api_key='your-key')

response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": "Hello!"}]
)

text = response.choices[0].message.content
tokens = response.usage.total_tokens
```

## 🧪 Testing Strategy

Test each function as you implement it:

```python
# Test in Python console or create test.py
from rag_pipeline import get_embedding, chunk_document

# Test embedding
text = "Hello world"
emb = get_embedding(text)
print(f"Embedding shape: {len(emb)}")  # Should be 384 for all-MiniLM-L6-v2

# Test chunking
doc = "word " * 100
chunks = chunk_document(doc, chunk_size=20, overlap=5)
print(f"Created {len(chunks)} chunks")
print(f"First chunk: {chunks[0]}")
```

## 🐛 Debugging Tips

1. **Redis Issues**
   - Check Redis is running: `redis-cli ping`
   - View stored keys: `redis-cli keys '*'`
   - Inspect key value: `redis-cli get "cache:tier1:123"`

2. **Embedding Issues**
   - Print embedding shape: `print(len(embedding))`
   - All embeddings should be same length (384 for all-MiniLM-L6-v2)

3. **Cache Not Working**
   - Add print statements to see similarity scores
   - Check if threshold is too high/low
   - Verify embeddings are being stored correctly

## 📝 Common Patterns You'll Use

### Reading file content
```python
# Text file
with open(filepath, 'r') as f:
    content = f.read()

# For PDF (you'll need PyPDF2)
import PyPDF2
with open(filepath, 'rb') as f:
    reader = PyPDF2.PdfReader(f)
    content = ''.join([page.extract_text() for page in reader.pages])
```

### Error handling
```python
try:
    # Your code
    result = some_function()
except Exception as e:
    print(f"Error: {e}")
    # Handle error appropriately
```

## 🎓 Learning Goals

By implementing each function, you'll learn:

- ✅ Vector embeddings and semantic similarity
- ✅ Redis for caching and storage
- ✅ Multi-tier caching strategies
- ✅ RAG (Retrieval Augmented Generation)
- ✅ LLM API integration
- ✅ Cost optimization techniques
- ✅ Metrics tracking and analytics
- ✅ API design with Flask
- ✅ Full-stack integration

## 💡 Getting Stuck?

If you get stuck on a function:
1. Read the TODO comments carefully
2. Check the resources section above
3. Print intermediate values to debug
4. Test with simple inputs first
5. Ask me for hints (not full solutions!)

Good luck! 🚀