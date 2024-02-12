import sqlite3

def create_grades_table():
    conn = sqlite3.connect('mydatabase.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS Grades (
                        grade_id INTEGER PRIMARY KEY,
                        student_id INTEGER,
                        subject_id INTEGER,
                        grade INTEGER,
                        date_received DATE,
                        FOREIGN KEY (student_id) REFERENCES Students(student_id),
                        FOREIGN KEY (subject_id) REFERENCES Subjects(subject_id)
                    )''')
    conn.commit()
    conn.close()