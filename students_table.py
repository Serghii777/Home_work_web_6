import sqlite3

def create_students_table():
    conn = sqlite3.connect('mydatabase.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS Students (
                        student_id INTEGER PRIMARY KEY,
                        student_name TEXT,
                        group_id INTEGER,
                        FOREIGN KEY (group_id) REFERENCES Groups(group_id)
                    )''')
    conn.commit()
    conn.close()