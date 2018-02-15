#!/usr/bin/python3
import sys
acumulado=0
palabraAnterior=None
for linea in sys.stdin:
    linea=linea.strip()
    palabra,valor=linea.split("\t")
    valor=int(valor)
    if palabraAnterior==palabra:
        acumulado=acumulado+valor
    else:
        if palabraAnterior:#resuelve primera línea 
            print(palabraAnterior+"\t"+str(acumulado))
        palabraAnterior=palabra
        acumulado=valor
print(palabraAnterior+"\t"+str(acumulado))#resuelve última línea  