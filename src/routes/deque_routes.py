from flask import Blueprint, render_template, request, redirect, url_for
from src.logic.deques import Deque

deque_bp = Blueprint('deque', __name__)
deque_line = Deque()


@deque_bp.route('/deque')
def deque_page():
    from_page = request.args.get('from_page', '')
    return render_template('works/deque.html', deque_items=deque_line.display(), from_page=from_page)


@deque_bp.route('/enqueue_front', methods=['POST'])
def enqueue_front():
    item = request.form.get('user_enqueue')
    from_page = request.form.get('from_page')

    if item:
        deque_line.enqueue_front(item)

    return redirect(url_for('deque.deque_page', from_page=from_page))


@deque_bp.route('/dequeue_rear', methods=['POST'])
def dequeue_rear():
    from_page = request.form.get('from_page')

    if not deque_line.is_empty():
        deque_line.dequeue_rear()

    return redirect(url_for('deque.deque_page', from_page=from_page))


@deque_bp.route('/enqueue_rear', methods=['POST'])
def enqueue_rear():
    item = request.form.get('user_enqueue')
    from_page = request.form.get('from_page')

    if item:
        deque_line.enqueue_rear(item)

    return redirect(url_for('deque.deque_page', from_page=from_page))


@deque_bp.route('/dequeue_front', methods=['POST'])
def dequeue_front():
    from_page = request.form.get('from_page')

    if not deque_line.is_empty():
        deque_line.dequeue_front()

    return redirect(url_for('deque.deque_page', from_page=from_page))


@deque_bp.route('/clear_dob_queue', methods=['POST'])
def clear_dob_queue():
    from_page = request.form.get('from_page')

    deque_line.clear()

    return redirect(url_for('deque.deque_page', from_page=from_page))

