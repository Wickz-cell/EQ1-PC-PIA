# EQ1-PC-PIA
Para llamar al script tiene que utilizar los siguientes parámetros de acuerdo a las tareas que quiere realizar:
  Para activar el análisis de urls con VirusTotal utilice los parámetros -a (La llave api de VirusTotal) y -tv (Nombre del archivo txt con las urls a analizar).
  Para la búsqueda de correos con Hunter utilice los parámetros -b (La llave api de Hunter) y -th (Nombre del archivo con los correos a buscar).
  Para el escaneo de puertos ip utilice -p (Nombre del archivo con los puertos a analizar).
  Para activar la búsqueda de metadatos utilice el parámetro -m (Path o nombre de la carpeta con los archivos a analizar).
  Para activar el cifrado de un mensaje utilice el parámetro -c (Mensaje a cifrar entre comillas (Tipo string)).
  Para el descifrado de un mensaje utilice el parámetro -d (Nombre del archivo con los mensajes a descifrar).

Ejemplo:
py main.py [-h] [-a Api VirusTotal] [-tv Txt urls] [-b Api Hunter] [-th Txt correos] [-p Txt puertos] [-m Path/Nombre carpeta] [-c Mensaje] [-d Txt mensajes]
