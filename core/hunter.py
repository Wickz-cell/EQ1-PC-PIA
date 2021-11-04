import json 
import requests 

def analizarCorreo(txt, key, result):
    apikey = key 
    fo = open(txt, "r")
    foo = open(result, "w")
    for line in fo:
        email = line
        page = requests.get("https://api.hunter.io/v2/email-verifier?email="+email+"&api_key="+apikey)
        foo.write("La respuesta HTTP para " + email + " es " + str(page.status_code) + "\n")
        hunter = json.loads(page.content)
        for key in hunter["data"]:
            if key == "sources":
                foo.write("El correo se encontró en " + str(len(hunter["data"]["sources"])) + " fuentes:\n")
                for sourc in range(len(hunter["data"]["sources"])):
                    url = "http://" + hunter["data"]["sources"][sourc]["domain"]
                    pagestat = requests.get(url)
                    if pagestat.status_code == 200:
                        foo.write(str(sourc) + "\t" + url + "\tstatus: " + str(pagestat.status_code) + "\n")
                    else:
                        foo.write(str(sourc) + "\t" + url + "\tstatus: " + str(pagestat.status_code) + " Falló" + "\n")
        foo.write("\n")

txt = input("Txt: ")
key = input("Key: ")
result = input("Result txt: ")

analizarCorreo(txt, key, result)
