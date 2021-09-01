
import os

def zmien(ścieżka):

    lista = os.listdir(ścieżka)

    for i in lista:

        if os.path.isdir(ścieżka + '\\' + i):

            zmien(ścieżka + '\\' + i)

        elif 'png' in i.lower():

            os.rename(ścieżka + '\\'+ i, ścieżka + '\\' + i[:-3] + 'jpg')

ścieżka = r"C:\Users\FLorenzLen\Pictures\aaaa"

zmien(ścieżka)