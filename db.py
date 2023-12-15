import sqlite3

DATABASE = 'database.db'

def get_db():
    conn = sqlite3.connect(DATABASE)
    return conn

def init_db():
    db = get_db()
    db.execute('CREATE TABLE IF NOT EXISTS items (id INTEGER PRIMARY KEY, name TEXT)')
    db.commit()

def add_item(name):
    db = get_db()
    db.execute('INSERT INTO items (name) VALUES (?)', (name,))
    db.commit()

def remove_item(item_id):
    db = get_db()
    db.execute('DELETE FROM items WHERE id = ?', (item_id,))
    db.commit()

def get_items():
    db = get_db()
    items = db.execute('SELECT * FROM items').fetchall()
    return items
