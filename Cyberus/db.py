def DBconnect(DB = "database.db"):
    import sqlite3
    return sqlite3.connect(DB, check_same_thread=False)

def DBcreate(connection):
    cursor = connection.cursor()
    query = '''CREATE TABLE IF NOT EXISTS users(
    id INTEGER UNIQUE PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL
    )
    '''
    cursor.execute(query)
    connection.commit()

def add_users(connection, username, password):
    cursor = connection.cursor()
    query = '''INSERT OR IGNORE INTO users (username, password) VALUES (? , ?)
    '''
    cursor.execute(query,(username, password))
    connection.commit()

def get_users(connection, username):
    cursor = connection.cursor()
    query = f'''SELECT * FROM users WHERE username = '{username}'
    '''
    cursor.execute(query)
