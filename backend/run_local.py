#!/usr/bin/env python3
"""
Local development script for running the Wealth Advisor backend
This script sets the port to 8000 for local development
"""

import os
import uvicorn
from main import app

if __name__ == "__main__":
    # Set port to 8000 for local development
    os.environ["PORT"] = "8000"
    
    print("🚀 Starting Wealth Advisor Backend (Local Development)")
    print("📍 Port: 8000")
    print("🌐 URL: http://localhost:8000")
    print("📚 API Docs: http://localhost:8000/docs")
    print("🔍 Health Check: http://localhost:8000/health")
    print("=" * 50)
    
    uvicorn.run(
        app, 
        host="0.0.0.0", 
        port=8000,
        reload=True,  # Enable auto-reload for development
        log_level="info"
    )
