from PIL.ExifTags import TAGS, GPSTAGS
from PIL import Image
from PyPDF2 import PdfFileReader, PdfFileWriter
import os


def buscarMetadataPdf(carpeta):
    try:
        ruta = carpeta
        os.chdir(ruta)
        for root, dirs, files in os.walk(".", topdown=False):
            for name in files:
                ext = name.lower().rsplit('.', 1)[-1]
                if ext in ['pdf']:
                    pdfFile = PdfFileReader(open(ruta+os.path.sep+name, 'rb'))
                    titlePdf = name.rsplit('.', 1)[0]
                    titleTxt = (str(titlePdf) + ".txt")
                    docInfo = pdfFile.getDocumentInfo()
                    foo = open(titleTxt, 'w')
                    foo.write("Título: " + str(pdfFile.documentInfo.title))
                    foo.write("\n")
                    foo.write("Páginas: " + str(pdfFile.getNumPages()))
                    foo.write("\n")
                    foo.write("Tipo: " + str(type(docInfo)))
                    foo.write("\n")
                    for metaItem in docInfo:
                        foo.write('[+] ' + metaItem + ':' + docInfo[metaItem])
                        foo.write("\n")
                    foo.close()
    except:
        pass


def decode_gps_info(exif):
    gpsinfo = {}
    if 'GPSinfo' in exif:
        Nsec = exif['GPSInfo'][2][2]
        Nmin = exif['GPSInfo'][2][1]
        Ndeg = exif['GPSInfo'][2][0]
        Wsec = exif['GPSInfo'][4][2]
        Wmin = exif['GPSInfo'][4][1]
        Wdeg = exif['GPSInfo'][4][0]
        if exif['GPSInfo'][1] == 'N':
            Nmult = 1
        else:
            Nmult = -1
        if exif['GPSInfo'][1] == 'E':
            Wmult = 1
        else:
            Wmult = -1
        Lat = Nmult * (Ndeg + (Nmin + Nsec/60.0)/60.0)
        Lng = Wmult * (Wdeg + (Wmin + Wsec/60.0)/60.0)
        exif['GPSInfo'] = {"Lat": Lat, "Lng": Lng}


def get_exif_metadata(image_path):
    ret = {}
    image = Image.open(image_path)
    if hasattr(image, '_getexif'):
        exifinfo = image._getexif()
        if exifinfo is not None:
            for tag, value in exifinfo.items():
                decoded = TAGS.get(tag, tag)
                ret[decoded] = value
    decode_gps_info(ret)
    return ret


def buscarMetadataImg(carpeta):
    try:
        ruta = carpeta
        os.chdir(ruta)
        for root, dirs, files in os.walk(".", topdown=False):
            for name in files:
                ext = name.lower().rsplit('.', 1)[-1]
                if ext in ['jpg', 'png', 'img']:
                    os.path.join(root, name)
                    titleImg = name.rsplit('.', 1)[0]
                    titleTxt = (str(titleImg) + ".txt")
                    foo = open(titleTxt, "w")
                    try:
                        exifData = {}
                        exif = get_exif_metadata(name)
                        for metadata in exif:
                            foo.write(
                                "Metadata: %s - Value: %s " % (
                                    str(metadata), str(exif[metadata])))
                            foo.write("\n")
                    except:
                        import sys
                        import traceback
                        traceback.print_exc(file=sys.stdout)
    except:
        pass

if __name__ == "__main__":
    buscarMetadataImg(str(os.getcwd()))
    buscarMetadataPdf(str(os.getcwd()))
