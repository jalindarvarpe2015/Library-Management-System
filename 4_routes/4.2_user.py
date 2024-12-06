from flask import Blueprint, jsonify, request
from app import db
from models import Book, BorrowRequest, BorrowHistory

user_bp = Blueprint('user', __name__)

@user_bp.route('/books', methods=['GET'])
def list_books():
    books = Book.query.all()
    return jsonify([{'id': book.id, 'title': book.title, 'author': book.author} for book in books])

@user_bp.route('/borrow', methods=['POST'])
def borrow_book():
    data = request.json
    new_request = BorrowRequest(
        user_id=data['user_id'], book_id=data['book_id'],
        start_date=data['start_date'], end_date=data['end_date']
    )
    db.session.add(new_request)
    db.session.commit()
    return jsonify({'message': 'Borrow request submitted'}), 201

@user_bp.route('/history/<int:user_id>', methods=['GET'])
def user_history(user_id):
    history = BorrowHistory.query.filter_by(user_id=user_id).all()
    return jsonify([{'book_id': h.book_id, 'start_date': h.start_date} for h in history])
