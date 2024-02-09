SELECT l.name, su.subject
FROM subjects su JOIN lectors l ON su.lectors_id = l.id
WHERE l.id = 1;