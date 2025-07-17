import sqlite3

def init_db():
    conn = sqlite3.connect('slimtrack.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            email TEXT UNIQUE,
            password TEXT
        )
    ''')
    cursor.execute('''
        INSERT OR IGNORE INTO users (name, email, password)
        VALUES ('João', 'joao@email.com', 'senha123')
    ''')
    conn.commit()
    conn.close()
