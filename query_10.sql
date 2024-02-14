SELECT DISTINCT Subjects.subject_name
FROM Subjects
JOIN Grades ON Subjects.subject_id = Grades.subject_id
JOIN Students ON Grades.student_id = Students.student_id
JOIN Professors ON Subjects.professor_id = Professors.professor_id
WHERE Students.student_id = 2
AND Professors.professor_id = 2;