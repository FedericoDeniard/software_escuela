from Packages.Package_SQL.conection import *
from Packages.Package_SQL.read import *
from Packages.Package_SQL.create import write_students

def delete_student():
    student_id = get_int(message="Ingrese el ID del alumno a eliminar: ")
    target_student = fetch_id(int(student_id))
    students_copy = []
    if len(target_student) > 0:
        show_student(target_student)
        if continue_loading():
            students = fetch_students()
            for i in range(1,len(students)):
                if int(students[i][0]) != student_id:
                    students_copy.append(students[i])
            write_students(students_copy)
            print(f"Alumno eliminado con exito")
    else:
        print(f"No se encontró ningún alumno con el id {student_id}")
    input("Presione una tecla para continuar...")
    clear_screen()
