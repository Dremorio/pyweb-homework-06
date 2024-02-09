import psycopg2
from contextlib import contextmanager
from psycopg2 import Error


@contextmanager
def create_connection():
    connection = None
    try:
        connection = psycopg2.connect(user='postgres', password='password', host='localhost',
                                      port='5432', database='pyweb1')
        yield connection
        connection.commit()
    except Error as er:
        print(er)
        connection.rollback()
    finally:
        connection.close()