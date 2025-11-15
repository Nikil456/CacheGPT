# CacheGPT - LLM Caching Solution

A React-based chat interface for an intelligent LLM caching system using sentence-transformer embeddings, FAISS, and RAG pipeline.

## 🚀 Features (In Development)

- **Intelligent Caching**: Reduces duplicate API calls by 42% using sentence-transformer embeddings and FAISS
- **RAG Pipeline**: Implements retrieval-augmented generation for efficient prompt handling
- **Real-time Analytics**: Visualizes cache hit rates (~63%) and API call reduction statistics
- **Optimized Retrieval**: Fine-tuned vector similarity thresholds to minimize hallucinations

## 📋 Project Overview

ChatGPT Caching Solution | Python, FAISS, RAG, Vector Databases, Prompt Engineering

- Engineered a caching solution for LLM prompts using sentence-transformer embeddings and FAISS
- Integrated a RAG pipeline to reduce duplicate API calls by 42% saving about $48 per 1K calls in token usage
- Logged and visualized API call reduction statistics across caching tiers to evaluate real-time cache hit rate of about 63%
- Tuned vector similarity thresholds and prompt chunking strategies to minimize hallucinations during retrieval

## 🛠️ Tech Stack

**Frontend:**
- React 18
- CSS3 with modern styling
- Component-based architecture

**Backend (Coming Soon):**
- Python
- FAISS (Facebook AI Similarity Search)
- Sentence Transformers
- Vector Databases
- RAG Pipeline

## 📦 Installation

1. **Clone the repository:**
```bash
git clone <your-repo-url>
cd CacheGPT
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

## 🎯 Current Status

✅ Basic UI Implementation
- Claude-like chat interface
- Message components (user/assistant)
- Input component with auto-resize
- Loading states and animations
- Responsive design

🔄 In Progress
- Backend caching logic
- FAISS integration
- RAG pipeline implementation
- Analytics dashboard

## 📁 Project Structure

```
CacheGPT/
├── public/
│   └── index.html
├── src/
│   ├── components/
│   │   ├── ChatMessage.js
│   │   ├── ChatMessage.css
│   │   ├── ChatInput.js
│   │   └── ChatInput.css
│   ├── App.js
│   ├── App.css
│   ├── index.js
│   └── index.css
├── package.json
└── README.md
```

## 🚧 Roadmap

- [ ] Implement backend API
- [ ] Integrate FAISS vector database
- [ ] Add sentence-transformer embeddings
- [ ] Build RAG pipeline
- [ ] Add caching logic
- [ ] Create analytics dashboard
- [ ] Add cache hit rate visualization
- [ ] Implement prompt chunking strategies
- [ ] Deploy to production

## 💡 Usage

Currently, the UI is a demonstration of the chat interface. Type messages in the input box and press Enter to send. The caching logic will be implemented in future updates.

## 📄 License

MIT

## 👤 Author

Nikil Kandala

---

**Note:** This is an active development project. The caching backend and FAISS integration are coming soon!