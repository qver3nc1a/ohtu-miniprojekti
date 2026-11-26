from src import db
from src.database import get_connection

def add_conference(author, title, booktitle, year, month, editor, volume, number, series, pages, organization, note, publisher, address):
    connect = get_connection()
    connect.execute(
        "INSERT INTO conferences (author, title, booktitle, year, month, editor, volume, number, series, pages, organization, note, publisher, address) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
        (author, title, booktitle, year, month, editor, volume, number, series, pages, organization, note, publisher, address)
    )
    connect.commit()
    connect.close()

def get_conferences():
    sql = """SELECT id, author, title, booktitle, year, month, editor, volume, number, series, pages, organization, note, publisher, address
             FROM conferences"""
    return db.query(sql)
