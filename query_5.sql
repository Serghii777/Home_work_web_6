SELECT subject_name
FROM Subjects
WHERE professor_id = (SELECT professor_id FROM Professors WHERE professor_name = 'ім"я викладача');