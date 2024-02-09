from psycopg2 import DatabaseError
from connect import create_connection
from random import randint, choice, sample
from faker import Faker

fake = Faker()

STUDENTS = randint(30, 50)
SUBJECTS_NUM = randint(5, 8)
LECTORS = randint(3, 5)
MARKS = randint(0, 20)

SUBJECTS_LST = ["Chemistry", "Physics", "History", "Literature", "Biology", "Mathematics",
                "Economy", "Computer Science"]
SUBJECTS = sample(SUBJECTS_LST, SUBJECTS_NUM)

SQL_TABLES = {
    "groups": """CREATE TABLE IF NOT EXISTS groups (
      group_char VARCHAR(1) PRIMARY KEY
    );""",
    "lectors": """CREATE TABLE IF NOT EXISTS lectors (
  id INT PRIMARY KEY,
  name VARCHAR(30)
);""",
    "students": """CREATE TABLE IF NOT EXISTS students (
      id INT PRIMARY KEY,
      name VARCHAR(30),
      group_char VARCHAR(1),
      FOREIGN KEY (group_char) REFERENCES groups (group_char)
            ON DELETE SET NULL
            ON UPDATE CASCADE
    );""",
    "subjects": """CREATE TABLE IF NOT EXISTS subjects (
      id INT PRIMARY KEY,
      subject VARCHAR(30),
      lectors_id INT,
      FOREIGN KEY (lectors_id) REFERENCES lectors (id)
            ON DELETE SET NULL
            ON UPDATE CASCADE
    );""",
    "student_marks": """CREATE TABLE IF NOT EXISTS student_marks (
      mark_id INT PRIMARY KEY,
      student_id INT,
      subject_id INT,
      mark INT,
      date DATE DEFAULT CURRENT_DATE,
      FOREIGN KEY (student_id) REFERENCES students (id)
            ON DELETE SET NULL
            ON UPDATE CASCADE,
      FOREIGN KEY (subject_id) REFERENCES subjects (id)
            ON DELETE SET NULL
            ON UPDATE CASCADE
    );"""
}


def student_marks_inserter():
    result = []
    id = 1
    for i in range(STUDENTS):
        for j in range(MARKS):
            student_id = randint(1, STUDENTS)
            subject_id = randint(1, SUBJECTS_NUM)

            result.append(f"INSERT INTO student_marks (mark_id, student_id, subject_id, mark, date) "
                          f"VALUES ({id}, {student_id}, {subject_id}, "
                          f"{randint(1, 100)}, '{fake.date_between(start_date='-1y', end_date='today')}')")
            id += 1
    return result


SQL_INSERT = {
    "groups": ["INSERT INTO groups (group_char) VALUES ('A'), ('B'), ('C')"],
    "lectors": [f"INSERT INTO lectors (id, name) VALUES ({i + 1}, '{fake.name()}')" for i in range(LECTORS)],
    "students": [f"INSERT INTO students (id, name, group_char) "
                 f"VALUES ({i + 1}, '{fake.name()}', '{choice(['A', 'B', 'C'])}')"
                 for i in range(STUDENTS)],
    "subjects": [f"INSERT INTO subjects (id, subject, lectors_id) "
                 f"VALUES ({i + 1}, '{subject}', {choice(range(1, LECTORS))})"
                 for i, subject in enumerate(sample(SUBJECTS_LST, SUBJECTS_NUM))],
    "student_marks": student_marks_inserter()
}


def create_sql_requests(sql):
    with create_connection() as conn:
        if conn is not None:
            try:
                c = conn.cursor()
                for value in sql:
                    if isinstance(value, str):
                        c.execute(value)
                    else:
                        for s in value:
                            c.execute(s)
            except DatabaseError as er:
                print(er)
        else:
            print("Can't create database connection")


if __name__ == '__main__':
    # create tables
    create_sql_requests(SQL_TABLES.values())

    # insert data
    create_sql_requests(SQL_INSERT["groups"])
    create_sql_requests(SQL_INSERT["lectors"])
    create_sql_requests(SQL_INSERT["students"])
    create_sql_requests(SQL_INSERT["subjects"])
    create_sql_requests(SQL_INSERT["student_marks"])
