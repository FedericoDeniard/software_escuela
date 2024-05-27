from Packages.Package_CRUD.read import *
from Packages.Package_CRUD.create import write_students


def update_student():
    clear_screen()
    student_id = get_int(message="Ingrese el ID del alumno: ")
    target_student = fetch_id(student_id)
    if len(target_student) > 0:
        student_copy = list(target_student)
        while True:
            clear_screen()
            show_student(student_copy)
            option = get_int(message="1. Modificar nombre\n2. Modificar apellido\n3. Modificar curso\n4. Modificar edad\n5. Modificar dni\n6. Modificar teléfonos\n7. Modificar correos\n8. Modificar alergias\n9. Ver cambios\n10. Guardar y salir\n11. Cancelar\n")
            match option:
                case 1:
                    clear_screen()
                    update_student_name(student_copy)
                case 2:
                    clear_screen()
                    update_student_lastname(student_copy)
                case 3:
                    clear_screen()
                    update_student_course(student_copy)
                case 4:
                    clear_screen()
                    update_student_age(student_copy)
                case 5:
                    clear_screen()
                    update_student_dni(student_copy)
                case 6:
                    clear_screen()
                    update_student_phones(student_copy)
                case 7:
                    clear_screen()
                    update_student_mails(student_copy)
                case 8:
                    clear_screen()
                    update_student_allergies(student_copy)
                case 9:
                    clear_screen()
                    show_student(student_copy)
                    input("Presione una tecla para continuar...")
                case 10:
                    clear_screen()
                    print("Se cargará la siguiente información")
                    show_student(student_copy)
                    if continue_loading():
                        students = fetch_students()
                        for i in range(len(students)):
                            if int(students[i][0]) == student_id:
                                students[i] = student_copy
                        write_students(students)
                        break
                case 11:
                    clear_screen()
                    print("Se perderan los datos modificados")
                    if continue_loading():
                        break 
    else:
        print(f"No se encontró ningún alumno con el id {student_id}")

    input("Presione una tecla para continuar...")
    clear_screen()


def update_student_name(student_copy: dict):
    name = get_string(message="Ingrese el nombre del alumno: ",min_length=1).capitalize()
    student_copy[1] = name

def update_student_lastname(student_copy: dict):
    lastname = get_string(message=f"Ingrese el apellido de {student_copy[1]}: ",min_length=1).capitalize()
    student_copy[2] = lastname

def update_student_course(student_copy: dict):
    course = course_id()
    student_copy[3] = course

def update_student_age(student_copy:dict):
    age = get_int(message=f"Ingrese la edad de {student_copy[1]}: ",attempts=1,min=1,max=18)
    student_copy[4] = age

def update_student_dni(student_copy:dict):
    dni = get_int(message=f"Ingrese el dni de {student_copy[1]}: ",min=10000000,max=99999999)
    student_copy[5] = dni

def update_student_phones(student_copy: dict):
    option = get_int(message="1. Modificar telefono padre\n2. Modificar telefono madre\n",min=1,max=2)
    match option:
        case 1:
            phone = get_int(message=f"Ingrese el teléfono del padre: ",min=1000000000,max=9999999999)
            student_copy[6] = phone
        case 2:
            phone = get_int(message=f"Ingrese el teléfono de la madre: ",min=1000000000,max=9999999999)
            student_copy[7] = phone

def update_student_mails(student_copy: dict):
    option = get_int(message="1. Modificar mail padre\n2. Modificar mail madre\n",min=1,max=2)
    match option:
        case 1:
            email = get_string(message=f"Ingrese el mail del padre: ")
            student_copy[8] = email
        case 2:
            email = get_string(message="Ingrese el mail de la madre: ")
            student_copy[9] = email

def update_student_allergies(student_copy: dict):
    allergies = get_string(message=f"Ingrese las alergias de {student_copy[1]}: ")
    student_copy[10] = allergies
