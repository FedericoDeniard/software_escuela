from Packages.Package_SQL.conection import *
from Packages.Package_SQL.read import *

def delete_student():
    conection,cursor = start_conection()

    sql = 'DELETE FROM alumnos WHERE id=%s'
    student_id = get_int(message="Ingrese el ID del alumno a eliminar: ")
    student_id = str(student_id)

    if id_exists(cursor, student_id):
        student = fetch_id(student_id)
        show_student(student)
        if continue_loading():
            cursor.execute(sql,(student_id,))
            conection.commit()
            print(f"Alumno eliminado con exito")
    else:
        print(f"No se encontró ningún alumno con el id {student_id}")
    close_conection(conection,cursor)

    input("Presione una tecla para continuar...")
    clear_screen()
