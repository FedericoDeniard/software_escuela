from Packages.Package_Input.Input import *
from Packages.Package_Menus.consult import *
from Packages.Package_Menus.modify import *
from Packages.Package_System.system import *

import traceback
import datetime

def main():
        create_backup()
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


try:
    main()
except Exception as e:
    today = datetime.datetime.now().strftime("%Y-%m-%d")
    with open("error.log", "a") as f:
        f.write(today +"\n"+ traceback.format_exc() + "--------------------------------------------")
    raise