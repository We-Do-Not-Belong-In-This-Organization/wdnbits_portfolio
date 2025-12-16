from flask import Blueprint, render_template, request, redirect, url_for
from src.logic.queues import Queue

queue_bp = Blueprint('queue', __name__)
queue_line = Queue()


@queue_bp.route('/queue')
def queue_page():
    from_page = request.args.get('from_page', '')
    return render_template('works/queue.html', queue_line=queue_line.display(), from_page=from_page)


@queue_bp.route('/enqueue', methods=['POST'])
def enqueue():
    item = request.form.get('user_enqueue')
    from_page = request.form.get('from_page')

    if item:
        queue_line.enqueue(item)

    return redirect(url_for('queue.queue_page', from_page=from_page))


@queue_bp.route('/dequeue', methods=['POST'])
def dequeue():
    from_page = request.form.get('from_page')

    queue_line.dequeue()

    return redirect(url_for('queue.queue_page', from_page=from_page))


@queue_bp.route('/clear_queue', methods=['POST'])
def clear_queue():
    from_page = request.form.get('from_page')

    queue_line.clear()

    return redirect(url_for('queue.queue_page', from_page=from_page))
