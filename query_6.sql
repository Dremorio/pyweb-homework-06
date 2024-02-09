SELECT g.group_char, s.name AS student
FROM groups g JOIN students s on s.group_char = g.group_char
WHERE g.group_char = 'A';