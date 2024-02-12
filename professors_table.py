import sqlite3

def create_professors_table():
    conn = sqlite3.connect('mydatabase.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS Professors (
                        professor_id INTEGER PRIMARY KEY,
                        professor_name TEXT
                    )''')
    conn.commit()
    conn.close()