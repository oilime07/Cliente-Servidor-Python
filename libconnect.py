#libconnect

import socket
import os

HOST = "127.0.0.1"
PORT = 65432 
tam = 5 * 1024

def login():
    os.system("cls")
    user = input("Ingresa usuario\t")
    passw = input("Ingresa la contraseña\t")
    os.system("cls")
    print("Se ingreso el usuario "+user)
    cierto=False
    separador=","
    with open ("Data.csv", encoding="utf-8") as archivo:
        next(archivo)
        for linea in archivo:
            linea=linea.rstrip("\n")
            columnas=linea.split(separador)
            usuario=columnas[0]
            contra=columnas[1]
            ruta=columnas[2]
            try:
                if user == usuario and passw == contra:
                    cierto=True
                    break
                if user != usuario or passw != contra:
                    cierto=False
            except ValueError:
                print("ups, algo salio mal")
        if cierto == True:
            print("Usuario correcto\n")
            print("Ruta: \n"+ruta)
        else:
            os.system("cls")
            print("No existe el usuario "+user+" o esta mal escrito algun campo.\nIntentelo de nuevo.") 
            opc=int (input("\n**Escriba 1 para ir a menu o 2 para reintentarlo**.\n"))
            if opc == 1:
                os.system("cls")
                import menu
                menu.opcion
            elif opc == 2:
                os.system("cls")
                login()      
            else:
                print("Palabra no valida")                   
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        s.sendall(ruta.encode('utf-8'))
        data = s.recv(1024)
        data2 = data.decode('utf-8')
        print(f"Lista de Archivos del usuario:\n {user} en la ruta: {ruta}\n\n{data2!r}")
        def opcion():
            correcto=False
            opc=0
            while(not correcto):
                try:
                    opc = int (input ("\n\n1) Bajar Archivo \n" "2) Cancelar \n"))
                    correcto=True
                except ValueError:
                    print("Error no es un numero entero")
                return opc

        opc2=0
        salir=False  
        opc2 = opcion()
        if opc2 == 1:
            file = input("Ingresa el archivo a bajar:\n")
            print("El archivo a bajar es"+file)
            s.sendall(file.encode('utf-8'))
            os.system("cls")
            with open(file, "wb") as f:        
                chunk = s.recv(tam)
                while chunk:
                    f.write(chunk)
                    chunk = s.recv(tam)
        elif opc2 == 2:
           salir = True
        else:
            print ("Introduce un numero entre 1 y 2")

    






