from Packages.Package_SQL.conection import *

def fetch_students() -> list:
    students = ''
    with open('data/alumnos.csv',newline='') as f:
        data = csv.reader(f, delimiter=',')
        students = list(data)
    return students

def fetch_id(id: int) -> list:
    students = ''
    with open('data/alumnos.csv',newline='') as f:
        data = csv.reader(f, delimiter=',')
        students = list(data)
    target_student = None
    for i in range(1,len(students)):
        if int(students[i][0]) == id:
            target_student = students[i]
            break
    return target_student

def fetch_value(filter: int):
    students = fetch_students()
    match filter:
        case 1: # Name
            index = 1
            value = get_string(message=f"Ingrese el nombre del alumno: ",min_length=1).capitalize()

        case 2: # Lastname
            index = 2
            value = get_string(message=f"Ingrese el apellido del alumno: ",min_length=1).capitalize()

        case 3: # Curso
            index = 3
            value = course_id()
    target_students = []
    for student in students:
        if student[index] == value:
            target_students.append(student)

    return target_students

def show_all_students(students: list):
    header = ["ID", "Alumno", "Edad", "DNI", "Teléfono padre", "Teléfono madre", "Email madre", "Email padre", "Alergias", "Curso"]
    print(f"{header[0]:^5}|{header[1]:^20}|{header[2]:^6}|{header[3]:^10}|{header[4]:^17}|{header[5]:^17}|{header[6]:^26}|{header[7]:^26}|{header[8]:^12}|{header[9]:^16}")
    for i in range(1,len(students)):
         show_student(students[i], False)

def show_student(student: list,title = True):
    if title:
        header = ["ID", "Alumno", "Edad", "DNI", "Teléfono padre", "Teléfono madre", "Email madre", "Email padre", "Alergias", "Curso"]
        print(f"{header[0]:^5}|{header[1]:^20}|{header[2]:^6}|{header[3]:^10}|{header[4]:^17}|{header[5]:^17}|{header[6]:^26}|{header[7]:^26}|{header[8]:^12}|{header[9]:^16}")
    id = int(student[0])
    name,lastname = student[1],student[2]
    age,dni,dad_phone,mom_phone = convert_valuet(student)
    allergies = student[10]
    course = get_course(int(student[3]))
    mom_email,dad_email = student[9],student[8]
    message = []
    message.append(f"{id:^5}") # ID
    message.append(f"{name + ' ' + lastname:^20}") # Name and Lastname
    message.append(f"{age:^6}") # Age
    message.append(f"{dni:^10}") # DNI
    message.append(f"{dad_phone:^17}") # Dad's phone
    message.append(f"{mom_phone:^17}") # Mom's phone
    message.append(f"{mom_email:^26}") # Mom's email
    message.append(f"{dad_email:^26}") # Dad's email
    message.append(f"{allergies:^12}") # Allergies
    message.append(f"{course:^16}") # Course
    final_message = "|".join(message)
    print(final_message)