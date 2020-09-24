from tkinter import *
from tkinter import filedialog
import re

def exp_regulares(lista):
    expreciones = {} 
    for txt in lista:
        exp = str(txt)
        exp = re.sub("Lit", "((25[0-5]|[0-2]?[0-4]?[0-9])|['#'][A-F0-9][A-F0-9])", exp)
        exp = re.sub("['(']Dir[')']", "['(']((25[0-5]|[0-2]?[0-4]?[0-9])|['#'][A-F0-9][A-F0-9])[')']", exp)
        exp = re.sub("Dir", "((25[0-5]|[0-2]?[0-4]?[0-9])|['#'][A-F0-9][A-F0-9])", exp)
        exp = re.sub("\s", "['\\\s']+", exp)
        exp = re.sub(",", "['\\\s']+", exp)
        expreciones[txt]=exp
    return expreciones

def buscar(instrucciones,texto): # instrucciones= bus{instruccion:expresion_regular}
    texto = re.sub(",", " ", texto)
    
    for ins in instrucciones.values():
        x = re.search(ins, texto)
        if x!=None:
            x = x.group(0)
            return True
        
    return False
        


def abrir_archivo():
    files = [("ass","*.ass"), ("Archivos de texto","*.txt"), ('All Files', '*.*')]
    archivo = filedialog.askopenfilename(title="abrir", filetypes=files)
    if archivo != '' and archivo != ():
        text.delete('1.0', END)
        texto = open(archivo, "r")
        for linea in texto.readlines():
            text.insert(INSERT, linea)
    error()

def guardar_archivo():
    files = [("ass","*.ass"), ("Archivos de texto","*.txt"), ('All Files', '*.*')]
    save = filedialog.asksaveasfile(filetypes=files, defaultextension=files)
    if save != None:
        contenido = text.get("1.0",'end-1c')
        save.write(contenido)
        save.close()

def marcar_error(rows):
    pos = str(rows)
    text.tag_add(pos, pos+".0", pos+".90")
    text.tag_config(pos, foreground="red")

def correcto(rows):
    pos = str(rows)
    text.tag_add(pos, pos+".0", pos+".90")
    text.tag_config(pos, foreground="white")

def error():
    contenido = text.get("1.0",'end-1c')
    contenido = contenido.split("\n")
   
    instrucciones = open("instrucciones.txt","r")
    inst={}
    for i in instrucciones.readlines():
        i = i.split("|")
        inst[i[0]]=i[1][0:7]

    #inst = {"MOV A,B": "0000000", "MOV B,A": "0000001"}

    bus = exp_regulares(inst.keys())
    #print(bus)

    i = 0
    while i < len(contenido):
        valido = buscar(bus, contenido[i])
        if valido:
            correcto(i+1)
        else:
            marcar_error(i+1)
        i += 1


def assembler():
    pass

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
    run.add_command(label="Recalcular errores", command=error)
    run.add_command(label="Assembler", command=assembler)


if __name__ == '__main__':
    root = Tk()
    root.title('Assembler')
    root.geometry("1200x720")

    menu()

    text = Text(root, height=100, width=300, bg="black", fg="white", insertbackground="white")
    text.pack()

    root.mainloop()

