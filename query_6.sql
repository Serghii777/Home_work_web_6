SELECT student_name
FROM Students
WHERE group_id = (SELECT group_id FROM Groups WHERE group_name = 'назва групи');