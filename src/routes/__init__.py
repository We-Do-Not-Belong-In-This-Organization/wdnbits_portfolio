from .main_routes import main_bp
from .queue_routes import queue_bp
from .deque_routes import deque_bp
from .btree_routes import btree_bp
from .bstree_routes import bstree_bp


def register_routes(app):
    app.register_blueprint(main_bp)
    app.register_blueprint(queue_bp)
    app.register_blueprint(deque_bp)
    app.register_blueprint(btree_bp)
    app.register_blueprint(bstree_bp)
