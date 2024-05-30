import tkinter as tk

""" root = tk.Tk()

etiqueta = tk.Label(root,text="Programa alumnos")

entrada = tk.Entry(root)
entrada.grid(row=4,column=0)
entrada.insert(0,"Escriba aqui...")

etiqueta.grid(row=0,column=0)

marco_principal = tk.Frame()
marco_principal.grid(row=1, column=0)
marco_principal.config(width="800",height="600")
marco_principal.config(bg="grey")

def click_button():
    texto = tk.Label(root,text=f"Se almacenó {entrada.get()}").grid(row=3,column=0)

boton1 = tk.Button(root,text="Apreta",command=click_button).grid(row=2,column=0)
 """


#root.mainloop()



def get_option(options: list,screen):
    option_var = tk.IntVar()
    for i in range(len(options)):
        tk.Radiobutton(screen,text=options[i][0],value=options[i][1],variable=option_var).pack()
    enviar = tk.Button(screen,text="Enviar").pack()
    return option_var.get()

def actualiza(value,root):
    resultado = tk.Label(root,text=value).grid(row=3)

def main():
    root = tk.Tk()
    # set_data = tk.Button(root,text="Cargar datos")
    # get_data = tk.Button(root,text="Obtener datos")
    # exit = tk.Button(root,text="Salir")

    # set_data.grid(row=0,column=0)
    # get_data.grid(row=0,column=1)
    # exit.grid(row=1)

    # x = tk.IntVar()
    titulo = tk.Label(root, text="Seleccione la respuesta correcta.").pack()
    # opcion_1 = tk.Radiobutton(root, text="Primera opción", value=1, variable=x, ).grid(row=1)
    # opcion_2 = tk.Radiobutton(root, text="Segunda opción", value=2, variable=x, ).grid(row=2)
    # enviar_boton = tk.Button(root,text="Enviar",command= lambda : actualiza(x.get(),root)).grid(row=4)
    # opciones = tk.IntVar()
    # for i in range(5):
    #     tk.Radiobutton(root, text=f"{i+1}", value=i+1, variable=opciones).grid(row=1,column=i)
    # enviar = tk.Button(root,text="Enviar", command=lambda: actualiza(opciones.get(),root)).grid(row=6)
    option = get_option([["Imprimir",1],["Salir",2],["Volver",3]],root)

    root.mainloop()


main()


    