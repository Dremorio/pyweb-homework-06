SELECT st.name, l.name,
AVG(sm.mark) AS avg_mark
FROM students st JOIN student_marks sm ON sm.student_id = st.id
JOIN subjects su ON sm.subject_id = su.id
JOIN lectors l ON l.id = su.lectors_id
GROUP BY st.name, l.name
ORDER BY l.name, st.name;