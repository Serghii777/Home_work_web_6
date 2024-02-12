SELECT Professors.professor_name, AVG(Grades.grade) AS average_grade
FROM Professors
JOIN Subjects ON Professors.professor_id = Subjects.professor_id
JOIN Grades ON Subjects.subject_id = Grades.subject_id
WHERE Professors.professor_name = '< ім"я викладача>'
GROUP BY Professors.professor_name;