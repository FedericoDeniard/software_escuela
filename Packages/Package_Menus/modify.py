from Packages.Package_SQL.sentences import *

def menu_set_data():
    clear_screen()
    while True:
        option = get_int(message="1. Nuevo alumno\n2. Modificar alumno\n3. Eliminar alumno\n4. Atras\n",min=1,max=4,error_message="Numeros validos del 1 al 4")
        match option:
            case 1:
                new_student()
            case 2:
                update_student()
            case 3:
                delete_student()
            case 4:
                clear_screen()
                break
