lista = []
dueño = []
def marca():
    marca = input(("ingrese la marca del auto : "))
    if len(marca) !=15 or not len(marca) !=2: 
        print("valida")
    else:
        print("invalida")
    

def precio():
     while (True):
        precio = int(input("ingrese el precio debe ser superior a 5m: "))
        if precio >= 5000000:
            print("precio valido")
            break
        else:
            print("precio no valido")  
        


        
def patente_A ():

    patente = input("ingrese letras de la patente: ")
    if patente != 4:
        print("valida")
    else:
        print("invalida")

def patente_b():
    while (True):
        patente_num = int(input("ingrese los digitos :"))
        if patente_num >=2:
            print("valido")
            break        
        else:
            print("invalido")

def registro_v():
    multas = int(input("ingre la cantidad de multas: "))
    cantidad_multa = int(input("ingrese total de las multas : "))
    fecha = int(input("ingrese la fecha del registro del auto :"))
    nombre_dueño = input("ingrese el nombre del dueño: ")





def grabar():
    while (True):
        
            tipo_auto = input("ingrese el tipo de vehiculo: ")
                
            marca()       
            precio()
            patente_A()
            patente_b()
            registro_v()
            break


def buscar():
    




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
            
                    