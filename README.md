# Library-Management-System

Here’s a detailed end-to-end solution for the Library Management System Task using Python, Flask, and an SQL database. The solution includes creating APIs for both librarian and library users, designing the database schema, and incorporating the required functionality.

1. Database Schema Design
Tables:
Users: Store user details (id, email, password, role).
Books: Store book details (id, title, author, copies).
BorrowRequests: Store borrow requests (id, user_id, book_id, start_date, end_date, status).
BorrowHistory: Store borrowing history (id, user_id, book_id, start_date, end_date).


2. Setup
Install Dependencies:

pip install flask flask_sqlalchemy flask-marshmallow flask-jwt-extended


Project Structure:
bash
Copy code
LibrarySystem/
│
├── app.py              # Main application
├── models.py           # Database models
├── schemas.py          # Marshmallow schemas
├── routes/
│   ├── librarian.py    # Librarian APIs
│   └── user.py         # User APIs
└── database.db         # SQLite database