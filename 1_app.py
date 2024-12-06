from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['JWT_SECRET_KEY'] = 'your_secret_key'

db = SQLAlchemy(app)
jwt = JWTManager(app)

from routes.librarian import librarian_bp
from routes.user import user_bp

app.register_blueprint(librarian_bp, url_prefix='/librarian')
app.register_blueprint(user_bp, url_prefix='/user')

if __name__ == "__main__":
    app.run(debug=True)
