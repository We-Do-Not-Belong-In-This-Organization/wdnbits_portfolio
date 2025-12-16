from flask import Blueprint, render_template, request, redirect, url_for, jsonify
from src.logic.deques import Deque

deque_bp = Blueprint('deque', __name__)
deque_line = Deque()


@deque_bp.route('/deque')
def deque_page():
    from_page = request.args.get('from_page', '')
    return render_template('works/deque.html', deque_items=deque_line.display(), from_page=from_page)


@deque_bp.route('/enqueue_front', methods=['POST'])
def enqueue_front():
    data = request.get_json()
    item = data.get('item')

    if item:
        deque_line.enqueue_front(item)

    return jsonify(queue=deque_line.display())


@deque_bp.route('/dequeue_rear', methods=['POST'])
def dequeue_rear():
    if not deque_line.is_empty():
        deque_line.dequeue_rear()

    return jsonify(queue=deque_line.display())


@deque_bp.route('/enqueue_rear', methods=['POST'])
def enqueue_rear():
    data = request.get_json()
    item = data.get('item')

    if item:
        deque_line.enqueue_rear(item)

    return jsonify(queue=deque_line.display())


@deque_bp.route('/dequeue_front', methods=['POST'])
def dequeue_front():
    if not deque_line.is_empty():
        deque_line.dequeue_front()

    return jsonify(queue=deque_line.display())


@deque_bp.route('/clear_dob_queue', methods=['POST'])
def clear_dob_queue():
    deque_line.clear()

    return jsonify(queue=deque_line.display())

