import psycopg2
from Packages.Package_Input.Input import *
from Packages.Package_System.system import *
from dotenv import load_dotenv
import os


def start_conection():
    load_dotenv()
    user = os.getenv('PG_USER')
    password = os.getenv('PG_PASSWORD')

    conection = psycopg2.connect(user=user,
                                password=password,
                                host='127.0.0.1',
                                port='5432',
                                database='escuela')
    cursor = conection.cursor()
    return conection, cursor

def close_conection(conection, cursor):
    cursor.close()
    conection.close()

def id_exists(cursor, student_id:int) -> dict:
    sql = 'SELECT 1 FROM alumnos where id=%s'
    cursor.execute(sql, (student_id,))
    return cursor.fetchone()
