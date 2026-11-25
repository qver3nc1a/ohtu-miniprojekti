from src import db
from src.database import get_connection

def add_paper(key, author, title, journal, year, volume, number, pages):
    connect = get_connection()
    connect.execute(
        "INSERT INTO papers (key, author, title, journal, year, volume, number, pages) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
        (key, author, title, journal, year, volume, number, pages)
    )
    connect.commit()
    connect.close()

def get_papers():
    sql = """SELECT id, key, author, title, journal, year, volume, number, pages
             FROM papers"""
    return db.query(sql)
