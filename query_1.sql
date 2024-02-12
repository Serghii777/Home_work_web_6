SELECT Students.student_id, Students.student_name, AVG(Grades.grade) AS avg_grade
FROM Grades
JOIN Students ON Grades.student_id = Students.student_id
GROUP BY Students.student_id, Students.student_name
ORDER BY avg_grade DESC
LIMIT 5;