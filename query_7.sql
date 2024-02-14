SELECT Students.student_name, Grades.grade
FROM Grades
JOIN Students ON Grades.student_id = Students.student_id
JOIN Subjects ON Grades.subject_id = Subjects.subject_id
JOIN Groups ON Students.group_id = Groups.group_id
WHERE Groups.group_id = 1 AND Subjects.subject_name = 'History';