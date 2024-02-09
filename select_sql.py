from connect import create_connection


def data_selector(data_select_sql):
    with create_connection() as conn:
        result = "Can't create database connection"
        if conn is not None:
            c = conn.cursor()
            c.execute(data_select_sql)
            result = c.fetchall()
            return result
        return result


def select(number):
    file = f"query_{str(number)}.sql"
    with open(file, 'r') as f:
        sql = f.read()
        print(data_selector(sql))


if __name__ == '__main__':
    select(1)