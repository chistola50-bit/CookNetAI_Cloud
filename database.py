import sqlite3

def init_db():
    conn = sqlite3.connect("cooknet.db")
    cur = conn.cursor()
    cur.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        username TEXT,
        full_name TEXT,
        bio TEXT,
        photo TEXT
    )
    """)
    cur.execute("""
    CREATE TABLE IF NOT EXISTS recipes (
        id INTEGER PRIMARY KEY,
        author_id INTEGER,
        title TEXT,
        description TEXT,
        photo TEXT,
        likes INTEGER DEFAULT 0,
        FOREIGN KEY(author_id) REFERENCES users(id)
    )
    """)
    cur.execute("""
    CREATE TABLE IF NOT EXISTS comments (
        id INTEGER PRIMARY KEY,
        recipe_id INTEGER,
        author_id INTEGER,
        text TEXT,
        FOREIGN KEY(recipe_id) REFERENCES recipes(id)
    )
    """)
    conn.commit()
    conn.close()
