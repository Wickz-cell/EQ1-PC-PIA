import argparse
import logging
from core.analizarUrl import analizarUrl
from core.hunter import analizarCorreo
from puertos import analisisPuertos
from core.busquedaMetadata import buscarMetadataPdf
from core.busquedaMetadata import buscarMetadataImg
from core.cifradoCesar import cifradoCesar
from core.descifradoCesar import descifradoCesar

logging.basicConfig(filename='main.log', level=logging.INFO,
                    format='%(levelname)s:%(asctime)s:%(message)s')

# Creamos un párrafo de info para -h
info = ("\nScript para la ejecución de tareas de ciberseguridad"
        "\nPara activar el análisis de virustotal utilice -a y -tv"
        "\nPara la búsqueda de correos utilice -b y -th"
        "\nPara el escaneo de puertos utilice -p"
        "\nPara la búsqueda de metadatos utilice -m"
        "\nPara el cifrado de un mensaje utilice -c"
        "\nPara el descifrado de un mensaje utilice -d")

# Definimos los argumentos aceptados
parser = argparse.ArgumentParser(info)
parser.add_argument('-a', '--analisis', type=str,
                    help="Llave api de VirusTotal para analizar urls")
parser.add_argument('-tv', '--txtvirus', type=str,
                    help="Nombre del archivo con las urls")
parser.add_argument('-b', '--busqueda', type=str,
                    help="Llave api de Hunter para búsqueda de correos")
parser.add_argument('-th', '--txthunter', type=str,
                    help="Nombre del archivo con los correos")
parser.add_argument('-p', '--puertos', type=str,
                    help="Nombre del archivo con los puertos a analizar")
parser.add_argument('-m', '--metadata', type=str,
                    help="Nombre de la carpeta con los archivos a analizar")
parser.add_argument('-c', '--cifrado', type=str,
                    help="Mensaje a cifrar entre comillas")
parser.add_argument('-d', '--descifrado', type=str,
                    help="Nombre del archivo con el mensaje a descifrar")

args = parser.parse_args()

# Llamamos a las funciones deseadas de acuerdo a los parámetros utilizados
if args.analisis is not None:
    analizarUrl(args.txtvirus, args.analisis)

if args.busqueda is not None:
    analizarCorreo(args.txthunter, args.busqueda)

if args.puertos is not None:
    analisisPuertos(args.puertos)

if args.metadata is not None:
    buscarMetadataPdf(args.metadata)
    buscarMetadataImg(args.metadata)

if args.cifrado is not None:
    cifradoCesar(args.cifrado)

if args.descifrado is not None:
    descifradoCesar(args.descifrado)
