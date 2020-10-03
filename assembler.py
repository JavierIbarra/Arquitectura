from tkinter import *
from tkinter import filedialog
import tkinter.messagebox as MessageBox
from funciones import *
import re


def abrir_archivo():
    files = [("ass","*.ass"), ("Archivos de texto","*.txt"), ('All Files', '*.*')]
    archivo = filedialog.askopenfilename(title="Abrir", filetypes=files)
    if archivo != '' and archivo != ():
        text.delete('1.0', END)
        text2.delete('1.0', END)
        text3.delete('1.0', END)
        texto = open(archivo, "r")
        for linea in texto.readlines():
            text.insert(INSERT, linea)
    error()

def guardar_archivo():
    files = [("out","*.out"), ('All Files', '*.*')]
    archivo = filedialog.asksaveasfilename(title="Guardar", filetypes=files)
    if archivo != '' and archivo != ():
        save = open(archivo, "w")
        contenido = text2.get("1.0",'end-1c')
        save.write(contenido)
        save.close()
        save = open(archivo[:-4]+".mem", "w")
        contenido = text3.get("1.0",'end-1c')
        save.write(contenido)
        save.close()
        save = open(archivo[:-4]+".ass", "w")
        contenido = text.get("1.0",'end-1c')
        save.write(contenido)
        save.close()
    


def error():
    text2.delete('1.0', END)
    text3.delete('1.0', END)
    texto = text.get("1.0",'end-1c')
   
    contenido = separar(texto)

    data = contenido[1][:-1]
    code = contenido[0]
    #print(data.split('\n'), code.split('\n'))

    variables, pos_textbox = buscar_data(data,text)

    instrucciones_texto , inst, literales= buscar_code(code, variables, pos_textbox, text)


def assembler():
    text2.delete('1.0', END)
    text3.delete('1.0', END)
    texto = text.get("1.0",'end-1c')
   
    contenido = separar(texto)

    data = contenido[1][:-1]
    code = contenido[0]
    #print(data, code)

    variables, pos_textbox = buscar_data(data,text,text3)

    instrucciones_texto , inst, literales= buscar_code(code, variables, pos_textbox, text)

    for codigo in inst:         #inst = {"MOV A,B": "0000000", "MOV B,A": "0000001"}
        instrucciones_texto = instrucciones_texto.replace(codigo, inst[codigo])
    for lit in literales:
        instrucciones_texto = instrucciones_texto.replace("Lit", lit, 1)

    instrucciones_texto = instrucciones_texto.replace(" ", "")
    instrucciones_texto = instrucciones_texto.replace("\t", "")
    text2.insert(INSERT, instrucciones_texto)

def menu():
    my_menu = Menu(root)
    root.config(menu=my_menu)

    file_menu = Menu(my_menu, tearoff=0)
    my_menu.add_cascade(label="Archivos", menu=file_menu)
    file_menu.add_command(label="Abrir", command=abrir_archivo)
    file_menu.add_command(label="Guardar como", command=guardar_archivo)
    file_menu.add_separator()
    file_menu.add_command(label="Salir", command=root.quit)


    run = Menu(my_menu, tearoff=0)
    my_menu.add_cascade(label="Ejecutar", menu=run)
    run.add_command(label="Recalcular Errores", command=error)
    run.add_command(label="Assembler", command=assembler)


if __name__ == '__main__':
    root = Tk()
    root.title('Assembler')
    root.geometry("1200x720")
    root.grid_rowconfigure(0, weight=1)
    root.grid_columnconfigure((1,2), weight=1)

    menu()

    text = Text(root, bg="black", fg="white", insertbackground="white")     # textbox code
    text.grid(row=0, column=1, rowspan=2, sticky="nsew")

    text2 = Text(root, bg="black", fg="white", insertbackground="white")    # textbox assembler
    text2.grid(row=0, column=2, sticky="nsew")

    text3 = Text(root, bg="black", fg="white", insertbackground="white")    # textbox mem
    text3.grid(row=1, column=2, sticky="nsew")

    root.mainloop()

