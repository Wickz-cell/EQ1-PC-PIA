import json 

import requests 

 

apikey = ("b28e63393a32cd2c22aa2cb38d77c276e8ab4445") 

email = "steli@close.io" 

page = requests.get ("https://api.hunter.io/v2/email-verifier?email="+email+"&api_key="+apikey) 

print ("La respuesta HTTP:", page.status_code) 

hunter = json.loads(page.content) 

 

input("Se muestra el contenido del diccionario") 

for key in hunter["data"]: 

    print (key, hunter["data"][key]) 

    if key == "sources": 

        print ("Sources",len(hunter["data"]["sources"])) 

        print ("\n\nEl correo "+email+", se encontró en las siguientes fuentes:") 

        for sourc in range(len(hunter["data"]["sources"])): 

            URL = "http://"+hunter["data"]["sources"][sourc]["domain"] 

            pagestat = requests.get(URL) 

            if pagestat.status_code == 200: 

                print (sourc,"\t",URL,"\tstatus:",pagestat.status_code) 

            else: 

                print (sourc,"\t",URL,"\tstatus:",pagestat.status_code, "Falló") 

