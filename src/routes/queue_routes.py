from flask import Blueprint, render_template, request, redirect, url_for, jsonify
from src.logic.queues import Queue

queue_bp = Blueprint('queue', __name__)
queue_line = Queue()


@queue_bp.route('/queue')
def queue_page():
    """Renders the main Queue interface.

    Query Parameters:
        from_page (str, optional): Navigation origin tracker.

    Returns:
        Rendered HTML template with the current queue items.
    """
    from_page = request.args.get('from_page', '')
    return render_template('works/queue.html', queue_line=queue_line.display(), from_page=from_page)


@queue_bp.route('/enqueue', methods=['POST'])
def enqueue():
    """Adds an item to the end of the queue.

    Expects JSON Payload:
        { "item": any }

    Returns:
        JSON: The updated list of items in the queue.
    """
    data = request.get_json()
    item = data.get('item')

    if item:
        queue_line.enqueue(item)

    return jsonify(queue=queue_line.display())


@queue_bp.route('/dequeue', methods=['POST'])
def dequeue():
    """Removes an item from the front of the queue.

    Returns:
        JSON: The updated list of items in the queue.
    """
    queue_line.dequeue()

    return jsonify(queue=queue_line.display())


@queue_bp.route('/clear_queue', methods=['POST'])
def clear_queue():
    """Clears all items from the queue.

    Returns:
        JSON: An empty list.
    """
    queue_line.clear()
    
    return jsonify(queue=queue_line.display())
