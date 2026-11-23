from src import db
from src.database import get_connection


def add_book(author, title, publisher, year):
    connect = get_connection()
    connect.execute(
        "INSERT INTO books (author, title, publisher, year) VALUES (?, ?, ?, ?)",
        (author, title, publisher, year)
    )
    connect.commit()
    connect.close()


def get_books():
    sql = """SELECT id, author, title, publisher, year
             FROM books"""
    return db.query(sql)