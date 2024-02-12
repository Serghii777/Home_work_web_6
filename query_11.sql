SELECT AVG(Grades.grade) AS average_grade
FROM Grades
JOIN Students ON Grades.student_id = Students.student_id
JOIN Subjects ON Grades.subject_id = Subjects.subject_id
JOIN Professors ON Subjects.professor_id = Professors.professor_id
WHERE Students.student_name = '<ім"я студента>'
AND Professors.professor_name = '<ім"я викладача>';