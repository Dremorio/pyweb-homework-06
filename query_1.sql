SELECT s.id, s.name,
AVG(sm.mark) AS avg_mark
FROM students s JOIN student_marks sm ON s.id = sm.student_id
GROUP BY s.id, s.name
ORDER BY avg_mark DESC
LIMIT 5;