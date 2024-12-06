from flask_marshmallow import Marshmallow
from models import User, Book, BorrowRequest, BorrowHistory

ma = Marshmallow()

class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User

class BookSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Book

class BorrowRequestSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = BorrowRequest

class BorrowHistorySchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = BorrowHistory

