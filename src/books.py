from src import db
from src.database import get_connection


def add_book(key, author, title, publisher, year, address):
    connect = get_connection()
    connect.execute(
        "INSERT INTO books (key, author, title, publisher, year, address) VALUES (?, ?, ?, ?, ?, ?)",
        (key, author, title, publisher, year, address)
    )
    connect.commit()
    connect.close()


def get_books():
    sql = """SELECT id, key, author, title, publisher, year, address
             FROM books"""
    return db.query(sql)