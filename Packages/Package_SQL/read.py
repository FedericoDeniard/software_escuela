from Packages.Package_SQL.conection import *

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

def fetch_id(id:int)->tuple:
    conection,cursor = start_conection()
    sql = 'SELECT * FROM alumnos where id=%s'
    cursor.execute(sql,(id,))
    register = cursor.fetchone()

    close_conection(conection,cursor)
    return register

def show_all_students(students: list):
    clear_screen()
    header = ["ID", "Alumno", "Edad", "DNI", "Teléfono padre", "Teléfono madre", "Email madre", "Email padre", "Alergias", "Curso"]
    print(f"{header[0]:^5}|{header[1]:^20}|{header[2]:^6}|{header[3]:^10}|{header[4]:^15}|{header[5]:^15}|{header[6]:^26}|{header[7]:^26}|{header[8]:^12}|{header[9]:^10}")
    for student in students:
        show_student(student,False)

    

def show_student(student: tuple,title = True):
    if title:
        header = ["ID", "Alumno", "Edad", "DNI", "Teléfono padre", "Teléfono madre", "Email madre", "Email padre", "Alergias", "Curso"]
        print(f"{header[0]:^5}|{header[1]:^20}|{header[2]:^6}|{header[3]:^10}|{header[4]:^15}|{header[5]:^15}|{header[6]:^26}|{header[7]:^26}|{header[8]:^12}|{header[9]:^10}")
    message = []
    message.append(f"{student[0] if student[0] is not None else 'none':^5}") # ID
    message.append(f"{(student[1] if student[1] is not None else 'none') + ' ' + (student[2] if student[2] is not None else 'none'):^20}") # Name and Lastname
    message.append(f"{student[4] if student[4] is not None else 'none':^6}") # Age
    message.append(f"{student[5] if student[5] is not None else 'none':^10}") # DNI
    message.append(f"{student[6] if student[6] is not None else 'none':^15}") # Dad's phone
    message.append(f"{student[7] if student[7] is not None else 'none':^15}") # Mom's phone
    message.append(f"{student[9] if student[9] is not None else 'none':^26}") # Mom's email
    message.append(f"{student[8] if student[8] is not None else 'none':^26}") # Dad's email
    message.append(f"{student[10] if student[10] is not None else 'none':^12}") # Allergies
    message.append(f"{get_course(student[3]):^10}") # Course
    final_message = "|".join(message)
    print(final_message)