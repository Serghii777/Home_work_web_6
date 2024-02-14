SELECT Students.student_name
FROM Grades
JOIN Students ON Grades.student_id = Students.student_id
JOIN Subjects ON Grades.subject_id = Subjects.subject_id
WHERE Subjects.subject_name = "History"
GROUP BY Students.student_id
ORDER BY AVG(Grades.grade) DESC
LIMIT 1;