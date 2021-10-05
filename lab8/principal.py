from core.BuscarMetadata import buscarMetadataPdf
from core.BuscarMetadata import buscarMetadataImg
from core.DescargaArchivos import descargaPdf
from core.DescargaArchivos import descargaImg
import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument('-e', '--extension', type=str,
                    choices=["pdf", "img", "both"], default="both",
                    help="Type of document to analize")
parser.add_argument('-f', '--fount', type=str, choices=["local", "web"],
                    default="local",
                    help="Type of search: Local archives or web search")
parser.add_argument('-s', '--source', type=str, default=(str(os.getcwd())),
                    help="Source of search{web or local}")
args = parser.parse_args()

if args.extension == "pdf":
    if args.fount == "web":
        descargaPdf(args.source)
        buscarMetadataPdf(str(os.getcwd()) + "\pdfs")
    else:
        buscarMetadataPdf(args.source)

if args.extension == "img":
    if args.fount == "web":
        descargaImg(args.source)
        buscarMetadataImg(str(os.getcwd()) + "\images")
    else:
        buscarMetadataImg(args.source)

if args.extension == "both":
    if args.fount == "web":
        path = str(os.getcwd())
        descargaImg(args.source)
        descargaPdf(args.source)
        buscarMetadataImg(path + "\images")
        buscarMetadataPdf(path + "\pdfs")
    else:
        buscarMetadataImg(args.source)
        buscarMetadataPdf(args.source)
