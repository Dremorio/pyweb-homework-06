SELECT su.subject, l.name,
AVG(sm.mark) AS avg_mark
FROM student_marks sm JOIN subjects su ON su.id = sm.subject_id
JOIN lectors l ON l.id = su.lectors_id
GROUP BY su.subject, l.name;