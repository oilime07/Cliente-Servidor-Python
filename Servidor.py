# echo-server.py

import socket
import os

HOST = "127.0.0.1"  
PORT = 65432  
tam = 5 * 1024

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        os.system("cls")
        print(f"Conexión por: \t {addr}")
        while True: 
            data = conn.recv(1024)
            if not data:
                break
            data2=(data.decode('utf-8'))
            print("Ruta recibida: "+data2)
            if os.fspath(data2):
                print("La carpeta del usuario existe.\n")
            try:
                os.chdir(data2)
                contenido = data2
                lista=os.listdir(contenido)
                lista_bytes=' '.join(lista)
                conn.sendall(bytes(lista_bytes, 'utf-8'))
                try:
                    while True: 
                        fileGet = conn.recv(1024)
                        if not fileGet:
                            break
                        file=(fileGet.decode('utf-8'))
                        with conn:
                            with open(file, 'rb') as f:
                                arc = f.read(tam)
                                while arc:
                                    conn.sendall(arc)
                                    arc = f.read(tam)
                except OSError:
                    break
            except FileNotFoundError:                  
                data2="No existe la carpeta del usuario..."
                conn.sendall(bytes(data2, 'utf-8'))
                


                    



                
                
            
