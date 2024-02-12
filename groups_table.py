import sqlite3

def create_groups_table():
    conn = sqlite3.connect('mydatabase.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS Groups (
                        group_id INTEGER PRIMARY KEY,
                        group_name TEXT
                    )''')
    conn.commit()
    conn.close()