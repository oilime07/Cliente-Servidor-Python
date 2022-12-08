#menu.py
import os

def opcion():
    correcto=False
    opc=0
    while(not correcto):
        try:
            opc = int (input ("Ingresa alguna opcion: \n""1) Conectar Usuario \n"  "2) Salir \n"))

            correcto=True
        except ValueError:
            print("Error no es un numero entero")
    return opc
salir = False
opc2=0

opc2 = opcion()
if opc2 == 1:
        os.system("cls")
        import libconnect
        libconnect.login()
elif opc2 == 2:
        salir = True
else:
        os.system("cls")
        print ("Introduce un numero entre 1 y 2")
        opcion()

  