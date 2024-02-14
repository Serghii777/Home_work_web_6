import sys
import sqlite3
import logging
from faker import Faker

from students_table import create_students_table
from groups_table import create_groups_table
from professors_table import create_professors_table
from subjects_table import create_subjects_table
from grades_table import create_grades_table

# Налаштування логування
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

def generate_fake_data(conn, amount_students, amount_groups, amount_professors, amount_subjects, max_grades_per_student):
    fake_data = Faker()

    # Заповнення таблиці груп
    for _ in range(amount_groups):
        cursor = conn.cursor()
        cursor.execute("INSERT INTO Groups (group_name) VALUES (?)", (fake_data.word(),))
        conn.commit()

    # Заповнення таблиці викладачів
    for _ in range(amount_professors):
        cursor = conn.cursor()
        cursor.execute("INSERT INTO Professors (professor_name) VALUES (?)", (fake_data.name(),))
        conn.commit()

    # Заповнення таблиці студентів
    for i in range(1, amount_students + 1):
        cursor = conn.cursor()
        cursor.execute("INSERT INTO Students (student_name, group_id) VALUES (?, ?)", (fake_data.name(), fake_data.random_int(min=1, max=amount_groups)))
        conn.commit()

    # Заповнення таблиці предметів
    subjects = ['Mathematics', 'Physics', 'Chemistry', 'Biology', 'History', 'Literature', 'Computer Science']
    for _ in range(amount_subjects):
        cursor = conn.cursor()
        cursor.execute("INSERT INTO Subjects (subject_name, professor_id) VALUES (?, ?)", (fake_data.random_element(elements=subjects), fake_data.random_int(min=1, max=amount_professors)))
        conn.commit()

    # Заповнення таблиці оцінок
    for student_id in range(1, amount_students + 1):
        for subject_id in range(1, amount_subjects + 1):
            for _ in range(fake_data.random_int(min=1, max=max_grades_per_student)):
                cursor = conn.cursor()
                cursor.execute("INSERT INTO Grades (student_id, subject_id, grade, date_received) VALUES (?, ?, ?, ?)",
                               (student_id, subject_id, fake_data.random_int(min=60, max=100), fake_data.date_this_year()))
                conn.commit()

def main(query_file):
    with sqlite3.connect("mydatabase.db") as conn:
        try:
            create_students_table()
            create_groups_table()
            create_professors_table()
            create_subjects_table()
            create_grades_table()
        except Exception as e:
            logger.error("An error occurred while creating tables: %s", e)
            sys.exit(1)

        # Виклик функції для заповнення таблиць випадковими даними
        try:
            generate_fake_data(conn, 50, 3, 5, 8, 20)
        except Exception as e:
            logger.error("An error occurred while generating fake data: %s", e)
            sys.exit(1)

        # Виконання SQL-запиту з файлу
        try:
            with open(query_file, 'r') as file:
                sql_query = file.read()
                cursor = conn.cursor()
                cursor.execute(sql_query)
                results = cursor.fetchall()
                print(results)
        except Exception as e:
            logger.error("An error occurred while executing SQL query: %s", e)
            sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python main.py query_file_number.sql")
        sys.exit(1)
    else:
        query_file = sys.argv[1]
        main(query_file)