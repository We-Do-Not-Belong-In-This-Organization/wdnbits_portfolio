from flask import Blueprint, render_template, request, redirect, url_for, jsonify
from src.logic.queues import Queue

queue_bp = Blueprint('queue', __name__)
queue_line = Queue()


@queue_bp.route('/queue')
def queue_page():
    from_page = request.args.get('from_page', '')
    return render_template('works/queue.html', queue_line=queue_line.display(), from_page=from_page)


@queue_bp.route('/enqueue', methods=['POST'])
def enqueue():
    data = request.get_json()
    item = data.get('item')

    if item:
        queue_line.enqueue(item)

    return jsonify(queue=queue_line.display())


@queue_bp.route('/dequeue', methods=['POST'])
def dequeue():
    queue_line.dequeue()

    return jsonify(queue=queue_line.display())


@queue_bp.route('/clear_queue', methods=['POST'])
def clear_queue():
    queue_line.clear()
    
    return jsonify(queue=queue_line.display())
