import sqlite3


def get_connection():
    connection = sqlite3.connect("database.db")
    return connection


def create_tables():
    connect = get_connection()

    connect.execute("""
        CREATE TABLE IF NOT EXISTS papers (
            id INTEGER PRIMARY KEY,
            author TEXT NOT NULL,
            title TEXT NOT NULL,
            journal TEXT,
            year INTEGER,
            volume TEXT,
            number TEXT,
            pages TEXT
        );
    """)

    connect.commit()
    connect.close()