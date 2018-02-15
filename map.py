#!/usr/bin/python3
import sys
for linea in sys.stdin: #cambiar pruebas por sys.stdin
    linea=linea.strip()
    campos=linea.split(",")
    if len(campos)==6 and campos[0]!="ProductID":#campos[3].isnumeric():
        print(campos[0].zfill(4)+"\t"+campos[3])