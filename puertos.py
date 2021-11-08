import subprocess
import logging


def analisisPuertos(ip):
    logging.info('Búsqueda de puertos iniciada')
    # Abrimos los txt en donde están las ip y donde registramos los resultados
    fo = open(ip, 'r')
    foo = open("registroPuertos.txt", 'w')
    # Repetimos el proceso por cada ip
    for ip in fo:
        direccion = ip
        # Llamamos a nuestra función de powershell
        comando = "powershell -ExecutionPolicy ByPass -File EscanerPuertos.ps1 -direccion_ip " + str(direccion)
        # Guardamos la salida del proceso
        try:
            procesoPowerShell = subprocess.check_output(comando)
            # Escribimos el ip que escaneamos y la salida de powershell
            foo.write("Puerto: " + str(ip) + "\n")
            foo.write(procesoPowerShell.decode())
            foo.write("\n\n")
        except Exception as e:
            foo.write("Puerto: " + str(ip) + "\n")
            foo.write(str(e))
            foo.write("\n\n")
            logging.warning('Error en búsqueda de puertos')
    # Guardamos lo escrito en nuestro txt
    logging.info('Búsqueda de puertos terminada')
    fo.close()
    foo.close()
