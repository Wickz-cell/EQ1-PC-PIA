# Importamos los módulos para excel, virustotal y
# manejar los tiempos de ejecución
from openpyxl import Workbook
from openpyxl import load_workbook
from hashlib import md5
from virus_total_apis import PublicApi
import time

# Abrimos el txt para leer las urls
fo = open("urls_virustotal.txt", "r")

# Abrimos un archivo excel para guardar el reporte
libro = Workbook()
hoja = libro.active

# Escribimos los encabezados de cada apartado
# del reporte
hoja.cell(1, 1, "Url")
hoja.cell(1, 2, "Fecha de análisis")
hoja.cell(1, 3, "Total de análisis")
hoja.cell(1, 4, "Análisis positivos")
hoja.cell(1, 5, "Clasificación")

# Le pedimos al usuario introducir su api para trabajar
api_key = input("Introduzca su llave de api: ")
api = PublicApi(api_key)

# Agregamos una variable para asignar al reporte
# una url por fila
i = 2

# Por cada url en el archivo txt se hace el análisis y
# se llena cada columna del reporte con la información
# indicada
for line in fo:
    response = api.get_url_report(line)
    hoja.cell(i, 1, line)
    # Si se realiza la conexión con éxito,
    # se guardará la información en el reporte
    if response["response_code"] == 200:
        hoja.cell(i, 2, response["results"]["scan_date"])
        hoja.cell(i, 3, len(response["results"]["scans"]))
        hoja.cell(i, 4, response["results"]["positives"])
        # Dependiendo de la cantidad de análisis positivos
        # se le declara una clasificación de amenaza
        if response["results"]["positives"] <= 3:
            hoja.cell(i, 5, "Baja")
        elif (response["results"]["positives"] > 3 and
              response["results"]["positives"] <= 10):
            hoja.cell(i, 5, "Medio")
        elif response["results"]["positives"] > 10:
            hoja.cell(i, 5, "Alto")
    # Si no se logra conectar, se escribe un mensaje de error
    else:
        hoja.cell(i, 2, "Error de conexión")
    # Se suma a la variable i para pasar de fila
    i += 1
    # Cuando acaba el ciclo se notifica y espera 15 segundos
    # para poder continuar con la siguiente url
    print(line + "analizado...")
    time.sleep(15)

# Al terminar, se notifica al usuario
print("Análisis terminado")

# Cierra el archivo txt y excel
fo.close()
libro.save("reporte_analizador_urls.xlsx")
