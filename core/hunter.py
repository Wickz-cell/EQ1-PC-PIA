import json
import requests
import logging


def analizarCorreo(txt, key):
    logging.info('Búsqueda de correos iniciada')
    # Definimos nuestra api key
    apikey = key
    # Abrimos los txt para leer y escribir
    fo = open(txt, "r")
    foo = open("result.txt", "w")
    # Realizamos el proceso por cada email
    for line in fo:
        email = line
        # Verificamos el email con la api de hunter
        page = requests.get("https://api.hunter.io/v2/email-verifier?"
                            "email="+email+"&api_key="+apikey)
        # Registramos la conexión
        foo.write("La respuesta HTTP para " + email + " es " +
                  str(page.status_code) + "\n")
        # Revisamos los datos obtenidos
        hunter = json.loads(page.content)
        for key in hunter["data"]:
            # Buscamos las posibles fuentes donde se encuentre el email
            if key == "sources":
                foo.write("El correo se encontró en " +
                          str(len(hunter["data"]["sources"]))+" fuentes:\n")
                # Registramos cada fuente
                for sourc in range(len(hunter["data"]["sources"])):
                    url = ("http://" +
                           hunter["data"]["sources"][sourc]["domain"])
                    pagestat = requests.get(url)
                    # Revisamos la conexión con la web
                    if pagestat.status_code == 200:
                        foo.write(str(sourc) + "\t" + url + "\tstatus: " +
                                  str(pagestat.status_code) + "\n")
                    else:
                        foo.write(str(sourc) + "\t" + url + "\tstatus: " +
                                  str(pagestat.status_code) +
                                  " Falló" + "\n")
        foo.write("\n")
    logging.info('Búsqueda de correos terminada')
    # Guardamos los txt
    fo.close()
    foo.close()
