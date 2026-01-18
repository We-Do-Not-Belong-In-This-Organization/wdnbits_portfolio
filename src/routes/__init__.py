from .main_routes import main_bp
from .queue_routes import queue_bp
from .deque_routes import deque_bp
from .btree_routes import btree_bp
from .bstree_routes import bstree_bp
from .graph_routes import graph_bp
from .sorting_routes import sorting_bp  
from .bblsort_routes import bblsort_bp, selection_bp #Merge into bubble and selection sort routes, bout to rename it laturr

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
    app.register_blueprint(sorting_bp)      app.register_blueprint(bblsort_bp) #Added bp for Bubble sort
    app.register_blueprint(selection_bp) #Added bp for Selection sort