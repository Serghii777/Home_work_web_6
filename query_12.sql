SELECT Students.student_name, Grades.grade
FROM Grades
JOIN Students ON Grades.student_id = Students.student_id
JOIN Subjects ON Grades.subject_id = Subjects.subject_id
JOIN Groups ON Students.group_id = Groups.group_id
WHERE Groups.group_name = '<назва групи>'
AND Subjects.subject_name = '<назва предмета>'
AND Grades.date_received = (
    SELECT MAX(date_received)
    FROM Grades
    JOIN Subjects ON Grades.subject_id = Subjects.subject_id
    WHERE Subjects.subject_name = '<назва предмета>'
);