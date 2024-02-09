SELECT st.name AS student, sm.mark AS mark,
su.subject AS subject, g.group_char AS group,
MAX(sm.date) AS latest_date
FROM students st JOIN student_marks sm ON sm.student_id = st.id
JOIN subjects su ON su.id = sm.subject_id
JOIN groups g ON g.group_char = st.group_char
WHERE su.id = 2 AND g.group_char = 'A'
GROUP BY st.name, su.subject, sm.mark, g.group_char
ORDER BY subject;