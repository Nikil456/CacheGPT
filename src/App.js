import React, { useState } from 'react';
import './App.css';
import ChatMessage from './components/ChatMessage';
import ChatInput from './components/ChatInput';
import MetricsPanel from './components/MetricsPanel';

function App() {
  const [messages, setMessages] = useState([
    {
      id: 1,
      role: 'assistant',
      content: 'Hello! I\'m CacheGPT, an LLM with intelligent caching. Ask me anything!'
    }
  ]);
  const [isLoading, setIsLoading] = useState(false);

  // Metrics state (placeholder data based on project description)
  const [metrics] = useState({
    cacheHitRate: 63,
    apiCallReduction: 42,
    costSavings: 48,
    totalQueries: 1247,
    cachedQueries: 785,
    newQueries: 462,
    documentCount: 12,
    similarityThreshold: 0.85,
    cacheTiers: [
      { name: 'Tier 1 (Exact)', hitRate: 85 },
      { name: 'Tier 2 (High Similarity)', hitRate: 68 },
      { name: 'Tier 3 (Similar)', hitRate: 45 }
    ]
  });

  const handleSendMessage = (content) => {
    // Add user message
    const userMessage = {
      id: Date.now(),
      role: 'user',
      content: content
    };
    
    setMessages(prev => [...prev, userMessage]);
    setIsLoading(true);

    // Simulate assistant response (placeholder for future implementation)
    setTimeout(() => {
      const assistantMessage = {
        id: Date.now() + 1,
        role: 'assistant',
        content: 'This is a placeholder response. The caching logic will be implemented later.'
      };
      setMessages(prev => [...prev, assistantMessage]);
      setIsLoading(false);
    }, 1000);
  };

  return (
    <div className="app">
      <MetricsPanel metrics={metrics} />
      
      <div className="main-content">
        <header className="app-header">
          <h1>CacheGPT</h1>
          <span className="subtitle">Intelligent LLM with Caching</span>
        </header>
        
        <div className="chat-container">
          <div className="messages-wrapper">
            {messages.map(message => (
              <ChatMessage 
                key={message.id}
                role={message.role}
                content={message.content}
              />
            ))}
            {isLoading && (
              <ChatMessage 
                role="assistant"
                content="Thinking..."
                isLoading={true}
              />
            )}
          </div>
          
          <ChatInput 
            onSendMessage={handleSendMessage}
            disabled={isLoading}
          />
        </div>
      </div>
    </div>
  );
}

export default App;
