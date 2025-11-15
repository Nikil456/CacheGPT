import React from 'react';
import './MetricsPanel.css';

function MetricsPanel({ metrics }) {
  return (
    <div className="metrics-panel">
      <div className="metrics-header">
        <h2>Cache Metrics</h2>
        <span className="live-indicator">
          <span className="pulse"></span>
          Live
        </span>
      </div>

      <div className="metrics-content">
        {/* Cache Hit Rate */}
        <div className="metric-card">
          <div className="metric-label">Cache Hit Rate</div>
          <div className="metric-value primary">{metrics.cacheHitRate}%</div>
          <div className="metric-bar">
            <div 
              className="metric-bar-fill"
              style={{ width: `${metrics.cacheHitRate}%` }}
            ></div>
          </div>
        </div>

        {/* API Call Reduction */}
        <div className="metric-card">
          <div className="metric-label">API Call Reduction</div>
          <div className="metric-value success">{metrics.apiCallReduction}%</div>
          <div className="metric-description">
            Duplicate calls eliminated
          </div>
        </div>

        {/* Cost Savings */}
        <div className="metric-card">
          <div className="metric-label">Cost Savings</div>
          <div className="metric-value highlight">${metrics.costSavings}</div>
          <div className="metric-description">
            Per 1K API calls
          </div>
        </div>

        {/* Total Queries */}
        <div className="metric-card">
          <div className="metric-label">Total Queries</div>
          <div className="metric-value">{metrics.totalQueries.toLocaleString()}</div>
          <div className="metric-stat-row">
            <span className="stat-item">
              <span className="stat-dot cached"></span>
              Cached: {metrics.cachedQueries}
            </span>
            <span className="stat-item">
              <span className="stat-dot new"></span>
              New: {metrics.newQueries}
            </span>
          </div>
        </div>

        {/* Document Store */}
        <div className="metric-card">
          <div className="metric-label">Document Store</div>
          <div className="metric-value">{metrics.documentCount}</div>
          <div className="metric-description">
            Documents in RAG pipeline
          </div>
        </div>

        {/* Vector Similarity Threshold */}
        <div className="metric-card">
          <div className="metric-label">Similarity Threshold</div>
          <div className="metric-value">{metrics.similarityThreshold}</div>
          <div className="metric-description">
            Vector matching threshold
          </div>
        </div>

        {/* Caching Tiers */}
        <div className="metric-card">
          <div className="metric-label">Cache Tier Performance</div>
          <div className="tier-stats">
            {metrics.cacheTiers.map((tier, index) => (
              <div key={index} className="tier-item">
                <div className="tier-info">
                  <span className="tier-name">{tier.name}</span>
                  <span className="tier-value">{tier.hitRate}%</span>
                </div>
                <div className="tier-bar">
                  <div 
                    className="tier-bar-fill"
                    style={{ width: `${tier.hitRate}%` }}
                  ></div>
                </div>
              </div>
            ))}
          </div>
        </div>

        {/* Embedding Model Info */}
        <div className="metric-card info-card">
          <div className="info-row">
            <span className="info-label">Embedding Model</span>
            <span className="info-value">sentence-transformer</span>
          </div>
          <div className="info-row">
            <span className="info-label">Vector DB</span>
            <span className="info-value">FAISS</span>
          </div>
          <div className="info-row">
            <span className="info-label">RAG Pipeline</span>
            <span className="info-value status-active">Active</span>
          </div>
        </div>
      </div>
    </div>
  );
}

export default MetricsPanel;
