SELECT g.group_char, su.subject,
AVG(sm.mark) AS avg_mark
FROM students st JOIN student_marks sm ON st.id = sm.student_id
JOIN subjects su ON su.id = sm.subject_id
JOIN groups g ON st.group_char = g.group_char
WHERE su.id = 2
GROUP BY g.group_char, su.subject
ORDER BY g.group_char;