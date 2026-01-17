from .main_routes import main_bp
from .queue_routes import queue_bp
from .deque_routes import deque_bp
from .btree_routes import btree_bp
from .bstree_routes import bstree_bp
from .graph_routes import graph_bp


def register_routes(app):
    """Registers all application blueprints with the main Flask app.

    This function connects the individual route modules (queue, deque, trees, etc.)
    to the central application instance so the URLs work correctly.

    Parameters:
        app (Flask): The main Flask application instance.

    Returns:
        None
    """
    app.register_blueprint(main_bp)
    app.register_blueprint(queue_bp)
    app.register_blueprint(deque_bp)
    app.register_blueprint(btree_bp)
    app.register_blueprint(bstree_bp)
    app.register_blueprint(graph_bp)
