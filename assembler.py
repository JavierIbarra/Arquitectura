import tkinter as tk
import tkinter.filedialog as filedialog
import tkinter.messagebox as tkMessageBox
import re


def exp_regulares(dicc):
    lista = dicc.keys()
    expreciones = {}
    dicc_2 = {}
    for txt in lista:
        exp = str(txt)
        exp = re.sub("Lit", "((25[0-5]|[0-2]?[0-4]?[0-9])|['#'][A-F0-9][A-F0-9])", exp)
        exp = re.sub("['(']Dir[')']",
                     "['(']((25[0-5]|[0-2]?[0-4]?[0-9])|['#'][A-F0-9][A-F0-9])[')']", exp)
        exp = re.sub("Dir", "((25[0-5]|[0-2]?[0-4]?[0-9])|['#'][A-F0-9][A-F0-9])", exp)
        exp = re.sub("\s", "['\\\s']+", exp)
        exp = re.sub(",", "['\\\s']+", exp)
        expreciones[txt] = exp
        dicc_2[exp] = [dicc[txt]]
    return expreciones, dicc_2


def buscar(instrucciones, texto):  # instrucciones= bus{instruccion:expresion_regular}
    texto = re.sub(",", " ", texto)

    for ins in instrucciones.values():
        # print(ins)
        x = re.search(ins, texto)
        if x is not None:
            x = x.group(0)
            if len(x) == len(texto):
                return True

    return False


def abrir_archivo():
    files = [("ass", "*.ass"), ("Archivos de texto", "*.txt"), ('All Files', '*.*')]
    archivo = filedialog.askopenfilename(title="abrir", filetypes=files)
    if archivo != '' and archivo != ():
        text.delete('1.0', tk.END)
        texto = open(archivo, "r")
        for linea in texto.readlines():
            text.insert(tk.INSERT, linea)
    error()


def guardar_archivo():
    files = [("ass", "*.ass"), ("Archivos de texto", "*.txt"), ('All Files', '*.*')]
    save = filedialog.asksaveasfile(mode='w', filetypes=files, defaultextension=files)
    if save is not None:
        contenido = text.get("1.0", 'end-1c')
        save.write(contenido)


def marcar_error(rows):
    pos = str(rows)
    text.tag_add(pos, pos+".0", pos+".90")
    text.tag_config(pos, foreground="red")


def correcto(rows):
    pos = str(rows)
    text.tag_add(pos, pos+".0", pos+".90")
    text.tag_config(pos, foreground="white")


def error():
    contenido = text.get("1.0", 'end-1c')
    contenido = contenido.split("\n")

    instrucciones = open("instrucciones.txt", "r")
    inst = {}
    for i in instrucciones.readlines():
        i = i.split("|")
        inst[i[0]] = i[1][0:7]

    # inst = {"MOV A,B": "0000000", "MOV B,A": "0000001"}

    bus, dicc = exp_regulares(inst)

    assembler(bus, dicc, contenido)

    i = 0
    i_correcto = 0
    i_incorrecto = 0
    while i < len(contenido):
        valido = buscar(bus, contenido[i])
        if valido:
            correcto(i+1)
            i_correcto += 1
        else:
            marcar_error(i+1)
            i_incorrecto += 1
        i += 1
    tkMessageBox.showinfo("El programa detecto",
                          "{correcto} correctos y {incorrecto} incorrectos".format(correcto=i_correcto,
                                                                                   incorrecto=i_incorrecto))


def assembler(bus, dicc, contenido):
    i = 0
    """

Falta hacer un metodo que lea el numero y lo ponga en binario entre el dicc[key] y el \n  """

    for i in range(len(contenido)):
        contenido[i] = re.sub(",", " ", contenido[i])
        trigger = 0
        for key in dicc.keys():
            x = re.search(key, contenido[i])
            if x is not None:
                trigger = 1
                text2.insert(tk.INSERT, dicc[key][0]+"\n")
        if trigger == 0:
            text2.insert(tk.INSERT, "X_NULL_X\n")


def menu():
    my_menu = tk.Menu(root)
    root.config(menu=my_menu)

    file_menu = tk.Menu(my_menu, tearoff=0)
    my_menu.add_cascade(label="Archivos", menu=file_menu)
    file_menu.add_command(label="Abrir", command=abrir_archivo)
    file_menu.add_command(label="Guardar como", command=guardar_archivo)
    file_menu.add_separator()
    file_menu.add_command(label="Salir", command=root.quit)

    run = tk.Menu(my_menu, tearoff=0)
    my_menu.add_cascade(label="Ejecutar", menu=run)
    run.add_command(label="Recalcular errores", command=error)
    run.add_command(label="Assembler", command=assembler)

    calculate = tk.Menu(my_menu, tearoff=0)
    calculate.add_command(label="Recalcular errores", command=error)


if __name__ == '__main__':
    root = tk.Tk()
    root.title('Assembler')
    root.geometry("1200x720")
    root.grid_rowconfigure(0, weight=1)
    root.grid_columnconfigure((1, 2), weight=1)

    menu()

    text = tk.Text(root, bg="black", fg="white", insertbackground="white")     # textbox code assembly
    text.grid(row=0, column=1, sticky="nsew")

    text2 = tk.Text(root, bg="black", fg="white", insertbackground="white")    # textbox code assembler
    text2.grid(row=0, column=2, sticky="nsew")

    root.mainloop()
