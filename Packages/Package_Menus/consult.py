from Packages.Package_SQL.sentences import *
from Packages.Package_System.system import *

def menu_get_data():
    clear_screen()
    while True:
          option = get_int(message="1. Listado de alumnos\n2. Búsqueda por valor\n3. Atras\n",min=1,max=3,error_message="Numeros validos del 1 al 3")
          match option:
               case 1:
                    alumnos = fetch_all()
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
                         break
               case 3:
                    clear_screen()
                    break
          clear_screen()
          if len(alumnos) > 0:
               for alumno in alumnos:
                    message = []
                    for i in range(len(alumno)):
                         if alumno[i] != None:
                              match i:
                                   case 0:
                                        message.append(f"ID: {alumno[i]}")
                                   case 1:
                                        message.append(f"Nombre: {alumno[i]}")
                                   case 2:
                                        message.append(f"Apellido: {alumno[i]}")
                                   case 3:
                                        message.append(f"Edad: {alumno[i]}")
                                   case 4:
                                        message.append(f"DNI: {alumno[i]}")
                                   case 5:
                                        message.append(f"Teléfono padre: {alumno[i]}")
                                   case 6:
                                        message.append(f"Teléfono madre: {alumno[i]}")
                                   case 7:
                                        message.append(f"Email madre: {alumno[i]}")
                                   case 8:
                                        message.append(f"Email padre: {alumno[i]}")
                                   case 9:
                                        message.append(f"Alergias: {alumno[i]}")
                                   case 10:
                                        message.append(f"curso: {get_course(alumno[i])}")
                    final_message = " - ".join(message)
                    print(final_message)
               input("Presione una tecla para continuar...")
          clear_screen()