import funciones as fn

lista=[]
fn.grabar()
fn.mostrar_opciones



def mostrar_opciones(): #creacion de menu principal
    global op
    op=""
    while(op != "1" and op != "2" and op != "3" and op != "4" ):
        op= input("Ingrese una opcion:\n \n1. grabar \n2. ibuscar \n3. imprimir certificado \n4. Salir\n\nOpcion: ")
        print("") #salto
    else:
        if op=="1":
            grabar()
        elif op=="2":
            buscar()
        elif op=="3": #anula el último vuelto que se compro en el momento, y deja el asiento disponible. (no especifica que sea un vuelo anterior)
            imprimir()
        elif op=="4":
            



