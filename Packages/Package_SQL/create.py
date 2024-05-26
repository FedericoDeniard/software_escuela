from Packages.Package_SQL.conection import *

# INSERT
def new_student():
    conection,cursor = start_conection()

    name = get_string(message="Ingrese el nombre del alumno: ",min_length=1).capitalize()
    lastname = get_string(message=f"Ingrese el apellido de {name}: ",min_length=1).capitalize()
    course = course_id()
    age, dni, dad_number, dad_email, mom_number, mom_email, allergies = (None, None, None, None, None, None, None)
    sql = 'INSERT INTO alumnos (nombre, apellido,id_curso, edad, dni, telefono_padre, telefono_madre, mail_padre,mail_madre, alergias) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
    if continue_loading():
        print("Los siguientes valores son opcionales.")
        while True:
            option = get_int(message="¿Que valor desea agregar?\n1. Edad\n2. DNI\n3. Telefonos\n4.Correos\n5.Alergias\n6. Continuar\n",min=1,max=6)
            match option:
                case 1:
                    age = get_int(message=f"Ingrese la edad de {name}: ",min=1,max=18)
                case 2:
                    dni = get_int(message=f"Ingrese el dni de {name}: ",min=10000000,max=99999999)
                case 3:
                    select_phone = get_int(message="1. Telefono mamá\n2. Telefono papa\n",min=1,max=2)
                    match select_phone:
                        case 1:
                            mom_number = get_int(message="Ingrese el teléfono de la madre: ",min=1000000000,max=9999999999)
                        case 2:
                            dad_number = get_int(message=f"Ingrese el teléfono del padre: ",min=10000000,max=99999999)
                case 4:
                    select_email = get_int(message="1. Correo madre\n2. Correo padre\n",min=1,max=2)
                    match select_email:
                        case 1:
                            mom_email = get_string(message="Ingrese el mail de la madre: ")
                        case 2:
                            dad_email = get_string(message=f"Ingrese el mail del padre: ")
                case 5:
                    allergies = get_string(message="Escriba las alergias (Todas en la misma respuesta): ")
                case 6:
                    if continue_loading():
                        break
    info = (name, lastname, course, age, dni,dad_number,mom_number,dad_email,mom_email,allergies)
    cursor.execute(sql, info)
    conection.commit()
    
    print(f"Alumno {lastname} {name} cargado.")
    
    close_conection(conection,cursor)

    input("Presione una tecla para continuar...")
    clear_screen()
