import React from 'react';
import './ChatMessage.css';

function ChatMessage({ role, content, isLoading }) {
  return (
    <div className={`message-container ${role}`}>
      <div className="message-avatar">
        {role === 'user' ? (
          <div className="avatar user-avatar">U</div>
        ) : (
          <div className="avatar assistant-avatar">
            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
              <path d="M21 16V8a2 2 0 0 0-1-1.73l-7-4a2 2 0 0 0-2 0l-7 4A2 2 0 0 0 3 8v8a2 2 0 0 0 1 1.73l7 4a2 2 0 0 0 2 0l7-4A2 2 0 0 0 21 16z"></path>
              <polyline points="3.27 6.96 12 12.01 20.73 6.96"></polyline>
              <line x1="12" y1="22.08" x2="12" y2="12"></line>
            </svg>
          </div>
        )}
      </div>
      <div className="message-content">
        <div className="message-role">{role === 'user' ? 'You' : 'CacheGPT'}</div>
        <div className={`message-text ${isLoading ? 'loading' : ''}`}>
          {isLoading ? (
            <div className="loading-dots">
              <span></span>
              <span></span>
              <span></span>
            </div>
          ) : (
            content
          )}
        </div>
      </div>
    </div>
  );
}

export default ChatMessage;
