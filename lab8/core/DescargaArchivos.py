import os
from lxml import html
from bs4 import BeautifulSoup
import requests


def descargaPdf(url):
        try:
                response = requests.get(url)
                parsed_body = html.fromstring(response.text)
                pdfs = parsed_body.xpath(
                    '//a[@href[contains(., ".pdf")]]/@href')
                if len(pdfs) > 0:
                        os.system("mkdir pdfs")
                for pdf in pdfs:
                        if pdf.startswith("http") is False:
                                download = url + pdf
                        else:
                                download = pdf
                        r = requests.get(download)
                        foo = open('pdfs/%s' % download.split('/')[-1], 'wb')
                        foo.write(r.content)
                        foo.close()
        except:
                pass
        f = open("Pdfs descargados.txt", "w")
        for pdf in pdfs:
                f.write(str(pdf))
                f.write("\n")
        f.close()


def descargaImg(url):
        try:
                response = requests.get(url)
                parsed_body = html.fromstring(response.text)
                images = parsed_body.xpath('//img/@src')
                os.system("mkdir images")
                for image in images:
                        if image.startswith("http") is False:
                                download = url + image
                        else:
                                download = image
                        r = requests.get(download)
                        foo = open('images/%s' % download.split('/')[-1], 'wb')
                        foo.write(r.content)
                        foo.close()
        except:
                pass
        f = open("Imagenes descargadas.txt", "w")
        for image in images:
                f.write(str(image))
                f.write("\n")
        f.close()

if __name__ == "__main__":
        url = 'http://www.google.es'
        descargaPdf(url)
        descargaImg(url)
