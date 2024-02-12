SELECT Groups.group_name, AVG(Grades.grade) AS average_grade
FROM Grades
JOIN Students ON Grades.student_id = Students.student_id
JOIN Groups ON Students.group_id = Groups.group_id
JOIN Subjects ON Grades.subject_id = Subjects.subject_id
WHERE Subjects.subject_name = 'назва певного предмета ['Mathematics', 'Physics', 'Chemistry', 'Biology', 'History', 'Literature', 'Computer Science']'
GROUP BY Groups.group_id;