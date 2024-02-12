import sqlite3

def create_subjects_table():
    conn = sqlite3.connect('mydatabase.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS Subjects (
                        subject_id INTEGER PRIMARY KEY,
                        subject_name TEXT,
                        professor_id INTEGER,
                        FOREIGN KEY (professor_id) REFERENCES Professors(professor_id)
                    )''')
    conn.commit()
    conn.close()