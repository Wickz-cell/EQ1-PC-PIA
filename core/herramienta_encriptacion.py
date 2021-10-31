from cryptography.fernet import Fernet
import os
import hashlib

# Metodo para generar el archivo clave
def keygen(nombre_archivo_clave):
    #Genera una clave aleatoria
    key = Fernet.generate_key()

    #Asigna el nombre del archivo clave
    archivo_clave = nombre_archivo_clave + '.key'
    

    with open(archivo_clave,'wb') as file:
        file.write(key)

    #file = open(archivo_clave, 'wb')
    #file.write(key)
    #file.close()

# Metodo para encriptar
def encrypt(path_key, path_file):
    #path_key = input('KEY PATH: ')
    #path_file = input('FILE PATH: ')

    with open(path_key, 'rb') as archivo_clave:
        key = archivo_clave.read()
        #print(key)

    with open(path_file, 'rb') as archivo_target:
        contenido = archivo_target.read()
        #print(contenido)

    k = Fernet(key)
    encrypted = k.encrypt(contenido)

    with open(path_file, 'wb') as archivo_encriptado:
        encriptado = archivo_encriptado.write(encrypted)

    print("Terminado: Encriptar")

# Metodo para desencriptar
def decrypt(path_key, path_file):
    #path_key = input('KEY PATH: ')
    #path_file = input('FILE PATH: ')

    with open(path_key, 'rb') as archivo_clave:
        key = archivo_clave.read()
        #print(key)

    with open(path_file, 'rb') as archivo_target:
        contenido = archivo_target.read()
        

    k = Fernet(key)
    decrypted = k.decrypt(contenido)

    with open(path_file, 'wb') as archivo_encriptado:
        encriptado = archivo_encriptado.write(decrypted)

    print("Terminado: Desencriptar")



try:
    # Menu de seleccion
    opcion = int(input("SELECCIONAR OPERACION:\n 1. Generar clave\n 2. Encriptar\n 3. Desencriptar\n>>>"))

       # KEYGEN
    if opcion == 1:
        print("[[KEYGEN]]")
        nombre_archivo_clave = input('ASIGNE UN NOMBRE A SU ARCHIVO: ')
        try:
            keygen(nombre_archivo_clave)
        except:
            print("[ERROR] No se pudo crear el archivo.")
        else:
            print('ARCHIVO CREADO: ' + nombre_archivo_clave + ".key")
            opcion_continuar = input("Continuar con la ENCRIPTACION?...(Y/N)\n")

            if opcion_continuar == "y":
                print("Procediendo con la encriptacion.")
                path_key = input('KEY PATH: ')
                path_file = input('FILE PATH: ')
                encrypt(path_key, path_file)
            elif opcion_continuar == "n":
                print("OPERACION TERMINADA: Se genero una clave; no se encripto ningun archivo.")
            else:
                print("OPERACION TERMINADA: Se genero una clave; no se encripto ningun archivo.")

         # ENCRYPT
    elif opcion == 2:
        print("[[ENCRYPT]]")
        try:
            path_key = input('KEY PATH: ')
            path_file = input('FILE PATH: ')
            encrypt(path_key, path_file)
        except:
            print("[ERROR] No se pudo ENCRIPTAR el archivo.")
            quit()
        else:
            print("ENCRIPTADO EXITOSO")

         # DECRYPT
    elif opcion == 3:
        print("[[DECRYPT]]")
        try:
            path_key = input('KEY PATH: ')
            path_file = input('FILE PATH: ')
            decrypt(path_key, path_file)
        except:
            print("[ERROR] No se pudo DESENCRIPTAR el archivo")
            quit()
            
        else:
            print("DESENCRIPTADO EXITOSO")

    else:
        quit()

except:
    print("[ERROR] Opcion no valida. ---")
    quit()
else:
    print("OPERACION EXITOSA.")