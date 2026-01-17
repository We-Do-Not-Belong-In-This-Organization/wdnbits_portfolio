from flask import Blueprint, render_template, request, redirect, url_for, jsonify
from src.logic.deques import Deque

deque_bp = Blueprint('deque', __name__)
deque_line = Deque()


@deque_bp.route('/deque')
def deque_page():
    """Renders the main Deque interface.

    Query Parameters:
        from_page (str, optional): Navigation origin tracker.

    Returns:
        Rendered HTML template with the current deque items.
    """
    from_page = request.args.get('from_page', '')
    return render_template('works/deque.html', deque_items=deque_line.display(), from_page=from_page)


@deque_bp.route('/enqueue_front', methods=['POST'])
def enqueue_front():
    """Adds an item to the front of the deque.

    Expects JSON Payload:
        { "item": any }

    Returns:
        JSON: The updated list of items in the deque.
    """
    data = request.get_json()
    item = data.get('item')

    if item:
        deque_line.enqueue_front(item)

    return jsonify(queue=deque_line.display())


@deque_bp.route('/dequeue_rear', methods=['POST'])
def dequeue_rear():
    """Removes an item from the rear (end) of the deque.

    Returns:
        JSON: The updated list of items in the deque.
    """
    if not deque_line.is_empty():
        deque_line.dequeue_rear()

    return jsonify(queue=deque_line.display())


@deque_bp.route('/enqueue_rear', methods=['POST'])
def enqueue_rear():
    """Adds an item to the rear (end) of the deque.

    Expects JSON Payload:
        { "item": any }

    Returns:
        JSON: The updated list of items in the deque.
    """
    data = request.get_json()
    item = data.get('item')

    if item:
        deque_line.enqueue_rear(item)

    return jsonify(queue=deque_line.display())


@deque_bp.route('/dequeue_front', methods=['POST'])
def dequeue_front():
    """Removes an item from the front of the deque.

    Returns:
        JSON: The updated list of items in the deque.
    """
    if not deque_line.is_empty():
        deque_line.dequeue_front()

    return jsonify(queue=deque_line.display())


@deque_bp.route('/clear_dob_queue', methods=['POST'])
def clear_dob_queue():
    """Clears all items from the deque.

    Returns:
        JSON: An empty list.
    """
    deque_line.clear()

    return jsonify(queue=deque_line.display())

