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

def id_exists(cursor, id_alumno):
    sql = 'SELECT 1 FROM alumnos where id_alumno=%s'
    cursor.execute(sql, (id_alumno,))
    return cursor.fetchone()
# Fetch
def fetch_all():
    conection,cursor = start_conection()

    sql = 'SELECT * FROM alumnos' 
    cursor.execute(sql)
    register = cursor.fetchall()

    close_conection(conection,cursor)
    return register

def fetch_value(filter: int):
    match filter:
        case 1:
            filter = 'nombre=%s'
            search = "nombre"
            value = get_string(message=f"Ingrese el {search} del alumno: ",min_length=1).capitalize()

        case 2:
            filter = 'apellido=%s'
            search = "apellido"
            value = get_string(message=f"Ingrese el {search} del alumno: ",min_length=1).capitalize()

        case 3:
            filter = 'id_curso=%s'
            search = 'curso'
            value = course_id()

    conection,cursor = start_conection()
    sql = f'SELECT * FROM alumnos where {filter}'
    cursor.execute(sql,(value,))
    register = cursor.fetchall()
    close_conection(conection,cursor)
    return register


# INSERT
def new_student():
    conection,cursor = start_conection()


    name = get_string(message="Ingrese el nombre del alumno: ",min_length=1).capitalize()
    lastname = get_string(message=f"Ingrese el apellido de {name}: ",min_length=1).capitalize()
    course = course_id()
    if continue_loading():
        sql = 'INSERT INTO alumnos (nombre, apellido,id_curso, edad, dni, telefono_padre, telefono_madre, mail_madre, mail_padre, alergias) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
        print("Los siguientes valores son opcionales, presione enter para omitir un valor")
        age = get_int(message=f"Ingrese la edad de {name}: ",attempts=1,min=1,max=18)
        dni = get_int(message=f"Ingrese el dni de {name}: ",min=10000000,max=99999999)
        dad_number = get_int(message=f"Ingrese el teléfono del padre: ",attempts=1,min=10000000,max=99999999)
        dad_email = get_string(message=f"Ingrese el mail del padre: ")
        mom_number = get_int(message="Ingrese el teléfono de la madre: ",attempts=1,min=10000000,max=99999999)
        mom_email = get_string(message="Ingrese el mail de la madre: ")
        allergies = get_string(message="Escriba las alergias (Todas en la misma respuesta): ")
        info = (name,lastname,course,age,dni,dad_number,mom_number,mom_email,dad_email,allergies)

    else:
        sql = 'INSERT INTO alumnos (nombre, apellido, id_curso) VALUES (%s,%s,%s)'
        info = (name,lastname,course)

    cursor.execute(sql, info)
    conection.commit()
    
    print(f"Alumno {lastname} {name} cargado.")
    
    close_conection(conection,cursor)

    input("Presione una tecla para continuar...")
    clear_screen()

# UPDATE
def update_student():
    conection,cursor = start_conection()

    id_alumno = get_int(message="Ingrese el ID del alumno: ")
    id_alumno = str(id_alumno)
    if id_exists(cursor,id_alumno):
        sql = 'UPDATE alumnos SET nombre=%s,apellido=%s WHERE id_alumno=%s'
        name = get_string(message="Ingrese el nombre del alumno: ",min_length=1).capitalize()
        lastname = get_string(message="Ingrese el apellido del alumno: ",min_length=1).capitalize()
        info = (name,lastname,id_alumno)
        if continue_loading():
            sql = 'UPDATE alumnos SET nombre=%s,apellido=%s,id_curso=%s,edad=%s,dni=%s,telefono_padre=%s,telefono_madre=%s,mail_madre=%s,mail_padre=%s,alergias=%s WHERE id_alumno=%s'
            course = course_id()
            print("Los siguientes valores son opcionales, presione enter para omitir un valor")
            age = get_int(message=f"Ingrese la edad de {name}: ",attempts=1,min=1,max=18)
            dni = get_int(message=f"Ingrese el dni de {name}: ",min=10000000,max=99999999)
            dad_number = get_int(message=f"Ingrese el teléfono del padre: ",attempts=1,min=10000000,max=99999999)
            dad_email = get_string(message=f"Ingrese el mail del padre: ")
            mom_number = get_int(message="Ingrese el teléfono de la madre: ",attempts=1,min=10000000,max=99999999)
            mom_email = get_string(message="Ingrese el mail de la madre: ")
            allergies = get_string(message="Escriba las alergias (Todas en la misma respuesta): ")
            info = (name,lastname,course,age,dni,dad_number,mom_number,mom_email,dad_email,allergies)

        cursor.execute(sql,info)
        conection.commit()

        print(f"Alumno modificado: {lastname} {name}")
    else:
        print(f"No se encontró ningún alumno con el id {id_alumno}")
    close_conection(conection,cursor)

    input("Presione una tecla para continuar...")
    clear_screen()

# DELETE
def delete_student():
    conection,cursor = start_conection()

    sql = 'DELETE FROM alumnos WHERE id_alumno=%s'
    id_alumno = get_int(message="Ingrese el ID del alumno a eliminar: ")
    id_alumno = str(id_alumno)

    if id_exists(cursor, id_alumno):
        cursor.execute(sql,(id_alumno,))
        conection.commit()
        print(f"Alumno eliminado con exito")
    else:
        print(f"No se encontró ningún alumno con el id {id_alumno}")
    close_conection(conection,cursor)

    input("Presione una tecla para continuar...")
    clear_screen()

