from Packages.Package_System.system import *
from Packages.Package_CRUD.read import *

def menu_get_data():
    clear_screen()
    while True:
          option = get_int(message="1. Listado de alumnos\n2. Búsqueda por valor\n3. Atras\n",min=1,max=3,error_message="Numeros validos del 1 al 3")
          match option:
               case 1:
                    alumnos = fetch_students()
                    show_all_students(alumnos)
               case 2:
                    while True:
                         clear_screen()
                         value = get_int(message="1. Buscar por nombre\n2. Buscar por apellido\n3. Buscar por curso\n4. Atras\n",min=1,max=4,error_message="Números válidos del 1 al 4")
                         match value:
                              case 4:
                                   clear_screen()
                                   break
                              case _:
                                   clear_screen()
                                   alumnos = fetch_value(value)
                                   show_all_students(alumnos)
                                   break
               case 3:
                    clear_screen()
                    break
          input("Presione una tecla para continuar...")
          clear_screen()

