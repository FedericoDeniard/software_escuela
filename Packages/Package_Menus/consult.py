from Packages.Package_SQL.conection import *
from Packages.Package_System.system import *
from Packages.Package_SQL.read import *

def menu_get_data():
    clear_screen()
    while True:
          option = get_int(message="1. Listado de alumnos\n2. Búsqueda por valor\n3. Atras\n",min=1,max=3,error_message="Numeros validos del 1 al 3")
          match option:
               case 1:
                    alumnos = fetch_all()
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


"""                     alumnos = [
    [1, "Juan", "Perez", 15, "12345678", "555-1234", "555-5678", "madre@gmail.com", "padre@gmail.com", "Ninguna", 101],
    [2, "María", "González", 16, "87654321", "555-9876", "555-5432", "madre2@gmail.com", "padre2@gmail.com", "Ninguna", 102],
    [3, "Pedro", "López", 14, "13579246", "555-1111", "555-2222", "madre3@gmail.com", "padre3@gmail.com", "Ninguna", 103],
    [4, "Ana", "Martínez", 17, "24681357", "555-3333", "555-4444", "madre4@gmail.com", "padre4@gmail.com", "Ninguna", 104],
    [5, "Luis", "Sánchez", 15, "98765432", "555-5555", "555-6666", "madre5@gmail.com", "padre5@gmail.com", "Ninguna", 105],
    [6, "Laura", "Díaz", 16, "74185296", "555-7777", "555-8888", "madre6@gmail.com", "padre6@gmail.com", "Ninguna", 106],
    [7, "Carlos", "Gómez", 14, "36925814", "555-9999", "555-0000", "madre7@gmail.com", "padre7@gmail.com", "Ninguna", 107],
    [8, "Elena", "Fernández", 17, "58274639", "555-1122", "555-3344", "madre8@gmail.com", "padre8@gmail.com", "Ninguna", 108],
    [9, "Diego", "Ruiz", 15, "16384925", "555-5566", "555-7788", "madre9@gmail.com", "padre9@gmail.com", "Ninguna", 109],
    [10, "Sofía", "Hernández", 16, "29384716", "555-9900", "555-1122", "madre10@gmail.com", "padre10@gmail.com", "Ninguna", 110]
] """