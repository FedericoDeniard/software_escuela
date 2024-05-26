from Packages.Package_SQL.create import *
from Packages.Package_SQL.update import *
from Packages.Package_SQL.delete import *


def menu_set_data():
    while True:
        clear_screen()
        option = get_int(message="1. Nuevo alumno\n2. Modificar alumno\n3. Eliminar alumno\n4. Buscar ID\n5. Atras\n",min=1,max=5,error_message="Numeros validos del 1 al 4")
        match option:
            case 1:
                clear_screen()
                new_student()
            case 2:
                clear_screen()
                update_student()
            case 3:
                clear_screen()
                delete_student()
            case 4:
                clear_screen()
                value = get_int(message="1. Buscar por nombre\n2. Buscar por apellido\n3. Buscar por curso\n4. Atras\n",min=1,max=4,error_message="Números válidos del 1 al 4")
                match value:
                    case 4:
                        clear_screen()
                    case _:
                        clear_screen()
                        alumnos = fetch_value(value)
                        show_all_students(alumnos)
                        input("Presione una tecla para continuar...")
            case 5:
                clear_screen()
                break
                
