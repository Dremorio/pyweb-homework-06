SELECT st.name, su.subject
FROM students st JOIN student_marks sm ON st.id = sm.student_id
JOIN subjects su ON sm.subject_id = su.id
WHERE st.id = 2
GROUP BY st.name, su.subject;