SELECT st.name, su.subject,
AVG(sm.mark) AS avg_mark
FROM students st JOIN student_marks sm ON st.id = sm.student_id
JOIN subjects su ON sm.subject_id = su.id
WHERE su.id = 2
GROUP BY st.name, su.subject
ORDER BY avg_mark DESC
LIMIT 1;