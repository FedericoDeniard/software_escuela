from Packages.Package_Input.Validate import *
from os import system
from Packages.Package_System.system import *

def get_int(message: str, error_message = "Error", attempts = 0, min = True, max = True,) -> int|None:
    """Obtains an integer from the user.

    Args:
        message (str): The prompt for user input.
        error_message (str): The error message to display if validation fails.
        min (int): The minimum value for the number's range. (Optional)
        max (int): The maximum value for the number's range. (Optional)
        attempts (int): The number of attempts allowed for user input. (Optional)

    Returns:
        int|None: Returns an interger if succesfull, or None otherwise.
    """
    attempt = 1
    number = input(message)
    while not validate_number(number=number, min=min, max=max):
        if attempt == attempts:
            number = None
            break
        print(error_message)
        input("Presione una tecla para continuar..\n")
        clear_screen()
        number = input(message)
        attempt +=1        
    if number != None:
        number = int(number)
    return number


def get_float(message: str, error_message: str,  attempts = 0, min = True, max = True) -> float|None:
    """Obtains a float from the user

    Args:
        message (str): The prompt for user input.
        error_message (str): The error message to display if validation fails.
        min (float): The minimum value for the number's range. (Optional)
        max (float): The maximum value for the number's range. (Optional)
        attempts (float): The number of attempts allowed for user input. (Optional)

    Returns:
        float|None: Returns a float if succesfull, or None otherwise.
    """
    attempt = 1
    number = input(message)
    number = float(number)
    while not validate_number(number=number, min=min, max=max):
        if attempt == attempts:
            number = None
            break
        else:
            pass
        print(error_message)
        number = input(message)
        number = float(number)
        attempt +=1
        
    return number

def get_string( message: str, max_length = True , min_length = True) -> str:
    """Obtains a string from the user

    Args:
        message (str): The prompt for user input.
        max_length (int): Maximum length of the string. (Optional)

    Returns:
        str|None: Returns a string.
    """
    text = input(message)
    if type(max_length) == int or (max_length) == int:
        while not check_max_length(max_length, text) or not check_min_length(min_length,text):
            if type(min_length) == int and type(max_length) == int:
                print(f"El texto debe tener por lo menos {min_length} caracteres y {max_length} como maximo")
            elif type(min_length) == int:
                print(f"El texto debe tener por lo menos {min_length} caracteres")
            else:
                print(f"El texto debe tener {max_length} como maximo")
            text = input(message)
    if len(text) == 0:
        text = None
    return text


def get_max_number(list: list) -> int:
    """Returns de max value from a list

    Args:
        list (list): The array of numbers you are going to compare

    Returns:
        int: The max value
    """
    number = 0
    for i in range(len(list)):
        if list[i] > number or i == 1:
            number = list[i]
    return number

def continue_loading(message = "¿Confirmar?\nS/N: ") -> bool:
    value = get_string(message=message,max_length=1,min_length=1).lower()
    while value not in ["s","n"]:
        value = get_string(message="¿Confirmar?\nS/N: ",max_length=1,min_length=1).lower()
    return value == "s"

def course_id() -> int:
    nivel = get_int(message="Ingrese el nivel (numero)\n1 - Primaria | 2 - Jardín\n",min=1,max=2)
    if nivel == 1:
        grado = get_int(message="Ingrese el grado\n1 - 2 - 3 - 4 - 5 - 6 - 7\n",min=1,max=7)
    else:
        grado = get_int(message="Ingrese la sala\n3 - 4 - 5\n",min=3,max=5)
    turno = get_int(message="Ingrese el turno\n1. Mañana\n2. Tarde\n3. Extendido\n",min=1,max=3)
    if nivel == 1:
        id = (grado - 1) * 3 + turno
    else:
        id = (grado - 3) * 3 + turno + 21
    return id

def get_course(id_curso: int) -> str:
    if id_curso >= 1 and id_curso <= 21:
        nivel = "Primaria"
        grado = (id_curso - 1) // 3 + 1
        turno = (id_curso - 1) % 3 + 1
    else:
        nivel = "Jardín"
        grado = (id_curso - 22) // 3 + 3
        turno = (id_curso - 22) % 3 + 1
    
    if turno == 1:
        texto_turno = "TM"
    elif turno == 2:
        texto_turno = "TT"
    else:
        texto_turno = "HE"
    
    return f"{nivel}, {grado} {texto_turno}"

def convert_valuet(student: list):
    age,dni,dad_phone,mom_phone = student[4],student[5],student[6],student[7]
    if validate_number(age):
        age = int(age)
    if validate_number(dni):
        dni = int(dni)
    if validate_number(dad_phone):
        int(dad_phone)
    if validate_number(mom_phone):
        int(mom_phone)
    return age,dni,dad_phone,mom_phone