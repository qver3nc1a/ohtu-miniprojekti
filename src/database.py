import sqlite3


def get_connection():
    connection = sqlite3.connect("database.db")
    return connection


def create_tables():
    connect = get_connection()

    connect.execute("""
        CREATE TABLE IF NOT EXISTS papers (
            id INTEGER PRIMARY KEY,
            key TEXT NOT NULL,
            author TEXT NOT NULL,
            title TEXT NOT NULL,
            journal TEXT,
            year INTEGER,
            volume TEXT,
            number TEXT,
            pages TEXT
        );
    """)

    connect.execute("""
        CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY,
            key TEXT NOT NULL,
            author TEXT NOT NULL,
            title TEXT NOT NULL,
            publisher TEXT,
            year INTEGER,
            address TEXT
        );
    """)

    connect.execute("""
            CREATE TABLE IF NOT EXISTS conferences (
                id INTEGER PRIMARY KEY,
                author TEXT NOT NULL,
                title TEXT NOT NULL,
                booktitle TEXT,
                year INTEGER,
                month TEXT,
                editor TEXT,
                volume TEXT,
                number TEXT,
                series TEXT,
                pages TEXT,
                organization TEXT,
                note TEXT,
                publisher TEXT,
                address TEXT
            );
        """)

    connect.commit()
    connect.close()