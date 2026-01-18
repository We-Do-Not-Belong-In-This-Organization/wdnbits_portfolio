"""
Main Application Entry Point.

This script initializes the Flask application instance, registers all the 
blueprints (routes) from the source folder, and starts the local development server.
"""

from flask import Flask
from src.routes import register_routes

app = Flask(__name__)
# Register all route blueprints (Logic for queues, trees, etc.)
register_routes(app)

# Check all registered routes(Just to Test)
print("=== Registered Flask Routes ===")
for rule in app.url_map.iter_rules():   # <-- use 'app' here, not 'website'
    print(f"{rule} -> {', '.join(rule.methods)}")
print("===============================")

if __name__ == '__main__':
    # Start the Flask development server
    # debug=True allows the server to auto-reload when you make code changes
    app.run(debug=True)
