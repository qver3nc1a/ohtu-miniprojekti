from src import db


def add_paper(author, title, journal, year, volume, number, pages):
    pass

def get_papers():
    sql = """SELECT id, author, title, journal, year, volume, number, pages
             FROM papers"""
    return db.query(sql)
