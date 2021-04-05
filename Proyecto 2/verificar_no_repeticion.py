import sys

lista = []

with open(sys.argv[1], "r") as archivo:
	for linea in archivo.readlines():
		linea = linea.split(",")
		if linea[0] not in lista:
			lista.append(linea[0])

# print("Lista de palabras:\n")
# print(lista)

print("Palabras no repetidas: {}".format(len(lista)))

