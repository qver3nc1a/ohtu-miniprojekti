from flask import render_template
import db


def add_paper(author, title, journal, year, volume, number, pages):
    pass

def get_papers():
    sql = """SELECT id, author, title, journal, year, volume, number, paper
             FROM papers"""
    return db.query(sql)
