import sqlite3

conn = sqlite3.connect('database.db')

conn.execute('CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY,name TEXT,email TEXT )')

conn.close()

