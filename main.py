from Packages.Package_Input.Input import *
from Packages.Package_Menus.consult import *
from Packages.Package_Menus.modify import *
from Packages.Package_System.system import *

def main():
        while True:
                option = get_int(message="1. Cargar datos\n2. Consultar datos\n3. Salir\n",min=1,max=3,error_message="Numeros validos del 1 al 3")
                match option:
                        case 1:
                                menu_set_data()
                        case 2:
                                menu_get_data()
                        case 3:
                                clear_screen()
                                break

main()
