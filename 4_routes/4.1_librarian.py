from flask import Blueprint, jsonify, request
from app import db
from models import User, BorrowRequest, BorrowHistory

librarian_bp = Blueprint('librarian', __name__)

@librarian_bp.route('/create-user', methods=['POST'])
def create_user():
    data = request.json
    new_user = User(email=data['email'], password=data['password'], role='user')
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'message': 'User created successfully'}), 201

@librarian_bp.route('/borrow-requests', methods=['GET'])
def view_borrow_requests():
    requests = BorrowRequest.query.all()
    return jsonify([{'id': req.id, 'status': req.status} for req in requests])

@librarian_bp.route('/approve-request/<int:request_id>', methods=['POST'])
def approve_request(request_id):
    req = BorrowRequest.query.get(request_id)
    if req:
        req.status = 'approved'
        db.session.commit()
        return jsonify({'message': 'Request approved'}), 200
    return jsonify({'error': 'Request not found'}), 404

@librarian_bp.route('/user-history/<int:user_id>', methods=['GET'])
def user_history(user_id):
    history = BorrowHistory.query.filter_by(user_id=user_id).all()
    return jsonify([{'book_id': h.book_id, 'start_date': h.start_date} for h in history])
