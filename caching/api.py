"""
Flask API Backend
Connects React frontend to caching system.
"""

from flask import Flask, request, jsonify
from flask_cors import CORS
from werkzeug.utils import secure_filename
import os

# Import your modules
from llm_wrapper import get_llm_response
from rag_pipeline import add_document_to_store, get_all_documents, delete_document, get_document_stats
from cache_tiers import get_tier_statistics, clear_all_cache, clear_tier
from metrics_tracker import get_current_metrics, update_query_metrics, reset_metrics

app = Flask(__name__)
CORS(app)

UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'doc', 'docx', 'md'}

os.makedirs(UPLOAD_FOLDER, exist_ok=True)


def allowed_file(filename):
    """Check if file extension is allowed."""
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/api/chat', methods=['POST'])
def chat():
    """
    Handle chat requests with caching and RAG.
    
    Expected JSON body:
        {
            "message": "user's question",
            "use_cache": true,
            "use_rag": true
        }
    
    Returns:
        {
            "response": "LLM answer",
            "cached": bool,
            "tier": "tier1/tier2/tier3",
            "similarity": 0.95,
            "cost": 0.002,
            "metrics": {...}
        }
    
    TODO:
    - Get message and options from request
    - Call get_llm_response() with options
    - Update metrics using update_query_metrics()
    - Get current metrics
    - Return response with metrics
    - Handle errors with try/except
    """
    pass


@app.route('/api/metrics', methods=['GET'])
def get_metrics():
    """
    Get current caching metrics.
    
    TODO:
    - Call get_current_metrics()
    - Return as JSON
    """
    pass


@app.route('/api/upload', methods=['POST'])
def upload_document():
    """
    Upload a document to the RAG document store.
    
    Expected: multipart/form-data with 'file' field
    
    Returns:
        {
            "success": bool,
            "message": str,
            "documentCount": int,
            "chunks_created": int
        }
    
    TODO:
    - Check if file is in request
    - Validate file extension
    - Save file securely
    - Read file content (handle different formats)
    - Call add_document_to_store()
    - Get updated document stats
    - Return success response
    - Handle errors
    """
    pass


@app.route('/api/documents', methods=['GET'])
def list_documents():
    """
    Get list of all documents in the store.
    
    TODO:
    - Call get_all_documents()
    - Get document stats
    - Return as JSON
    """
    pass


@app.route('/api/documents/<filename>', methods=['DELETE'])
def delete_document_endpoint(filename):
    """
    Delete a specific document.
    
    TODO:
    - Call delete_document(filename)
    - Return success/failure
    """
    pass


@app.route('/api/cache/clear', methods=['POST'])
def clear_cache():
    """
    Clear all cache entries.
    
    TODO:
    - Call clear_all_cache()
    - Return counts of cleared entries
    """
    pass


@app.route('/api/cache/clear/<tier>', methods=['POST'])
def clear_cache_tier(tier):
    """
    Clear a specific cache tier.
    
    TODO:
    - Validate tier name
    - Call clear_tier(tier)
    - Return count of cleared entries
    """
    pass


@app.route('/api/tier-stats', methods=['GET'])
def tier_statistics():
    """
    Get detailed statistics for each cache tier.
    
    TODO:
    - Call get_tier_statistics()
    - Return formatted stats
    """
    pass


@app.route('/api/health', methods=['GET'])
def health_check():
    """
    Health check endpoint.
    
    TODO:
    - Check Redis connection
    - Check if models are loaded
    - Return status
    """
    pass


if __name__ == '__main__':
    print("🚀 Starting CacheGPT API Server...")
    print("📊 Endpoints:")
    print("   POST   /api/chat              - Send message")
    print("   GET    /api/metrics           - Get metrics")
    print("   POST   /api/upload            - Upload document")
    print("   GET    /api/documents         - List documents")
    print("   DELETE /api/documents/<name>  - Delete document")
    print("   POST   /api/cache/clear       - Clear all cache")
    print("   POST   /api/cache/clear/<tier> - Clear tier")
    print("   GET    /api/tier-stats        - Tier statistics")
    print("   GET    /api/health            - Health check")
    print("\n🎯 Server running on http://localhost:5000")
    
    # TODO: Initialize metrics on startup
    # initialize_metrics()
    
    app.run(debug=True, port=5000, host='0.0.0.0')