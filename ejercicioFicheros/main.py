# Lee el fichero y procésalo de tal manera que sea capaz de mostrar
# la temperatura máxima para una ciudad dada. Esa ciudad la debe poder recibir
# como un argumento de entrada. Si la ciudad no existe, se deberá manejar a
# través de una excepción.
import csv
import sys


def temp_maximas(ciudad_dada):
    with open("climatologia.csv", encoding="utf-8", newline="\n") as fichero:
        reader = reader = csv.DictReader(fichero)

        for ciudad_dada in reader:
                print(ciudad_dada['estacion'], ciudad_dada['temperatura_maxima'])



print(temp_maximas('Estaca de Bares'))