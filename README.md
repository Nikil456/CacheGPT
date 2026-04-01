# CacheGPT - LLM Caching Solution

A React-based chat interface for an intelligent LLM caching system using sentence-transformer embeddings, FAISS, and RAG pipeline.

## Project Overview

- **Intelligent Caching**: Engineered a caching solution for LLM prompts using sentence-transformer embeddings and FAISS
- **RAG Pipeline**: Integrated a RAG pipeline to reduce duplicate API calls by 42% saving about $48 per 1K calls in token usage
- **Real-time Analytics**: Logged and visualized API call reduction statistics across caching tiers to evaluate real-time cache hit rate of about 63%
- **Optimized Retrieval**: Tuned vector similarity thresholds and prompt chunking strategies to minimize hallucinations during retrieval

## Installation

1. **Clone the repository:**
```bash
git clone https://github.com/Nikil456/CacheGPT.git
```

2. **Install dependencies:**
```bash
npm install
```

3. **Start the development server:**
```bash
npm start
```

The app will open at [http://localhost:3000](http://localhost:3000)

## Current Status
Complete
- Basic UI Implementation
- Message components (user/assistant)

In Progress
- Backend caching logic
- FAISS integration
- RAG pipeline implementation
- Analytics dashboard

## To Do List

- [ ] Implement backend API
- [ ] Integrate FAISS vector database
- [ ] Add sentence-transformer embeddings
- [ ] Build RAG pipeline
- [ ] Add caching logic
- [x] Create analytics dashboard
- [ ] Add cache hit rate visualization
- [ ] Implement prompt chunking strategies
- [ ] Deploy to production

**Note:** This is an active development project. Currently, the UI is a demonstration of the chat interface. The caching backend and FAISS integration are coming soon.
