SELECT su.subject, st.name AS student, l.name AS lector
FROM subjects su JOIN student_marks sm ON sm.subject_id = su.id
JOIN lectors l ON l.id = su.lectors_id
JOIN students st ON st.id = sm.student_id
WHERE st.id = 4 AND l.id = 1
GROUP BY su.subject, st.name, l.name;