# Descripción: Cliente con el que se prueba y muestra el correcto funcionamiento
#              de las operaciones de la tabla de hash.
#               
#             La ejecución de este módulo se hace a través de la siguiente
#             línea de comando:
#
#             >./probar_tabla_hash.py
#
# Creado por: Juan Reyna
# email: 10-10883@usb.ve
# version: 1.0


import string as st
import random as rd
import tabla_hash as th
import hashEntry as he
import time

lista = st.ascii_letters
lista1 = []

for i in range(len(lista)):
    lista1.append(lista[i])
n = rd.randint(50, 150)
m = rd.randint(500, 1500)

# Se crea lista de claves enteras
claves = [rd.randint(1, 100) for i in range(m)]

# Se crea lista de strings
valores = ["".join([rd.choice(lista1) for x in range(5)]) for i in range(m)]

# Se crea tabla de hash
tablaH = th.crear_tabla(n)

# Se insertan pares (clave, valor) generados de manera aleatoria.
# Se insertan objetos tipos hash entry generados de manera aleatoria.
texto_ins = "Se insertan {} elementos en la tabla de HASH\n".format(m)
print(texto_ins.center(50, "*"))
time.sleep(2)
print("La tabla se creó con {} casillas".format(n))
for i in range(m):
    clave = rd.choice(claves)
    valor = rd.choice(valores)
    if clave % 2 == 0:
        tablaH.agregar(clave, valor)
    elif clave % 2 == 1:
        tablaH.agregar_elem(he.HashEntry(clave, valor))


# Se buscan claves existentes en la tabla de Hash en caso contrario
# Si se encuentra la clavese retorna su String asociado, si no existe
# se retorna None

texto_ins = "\nSe buscan {} elementos el la tabla HASH\n".format(m // 2)
print(texto_ins.center(50, "*"))
time.sleep(2)
claves_buscadas = []
for x in range(m):
    search = rd.choice(claves)

#   Eliminar estas lineas el programa funciona paro busca las mismas claves
#    while search in claves_buscadas and len(claves_buscadas) <  len(claves):
#        print(search)
#        search = rd.choice(claves)
    claves_buscadas.append(search)
    print("Clave buscada: {}, Valor asociado a la clave: {}"
                                .format(search, tablaH.buscar(search)))

# Se eliminan pares (clave, valor) generados de manera aleatoria.
# Se eliminan objetos tipos hash entry generados de manera aleatoria.
texto_ins = "\nSe intentará eliminar {} elementos en la tabla HASH\n".format(m //2)
print(texto_ins.center(50, "*"))
time.sleep(2) 
for i in range(m):
    clave = rd.choice(claves_buscadas)
    valor = rd.choice(valores)
    if clave % 2 == 0:
        elim = tablaH.eliminar(clave)
        print("* Clave a eliminar: {}, valor asociado: {}".format(clave, elim))
    elif clave % 2 == 1:
        elim = tablaH.eliminar_elem(he.HashEntry(clave, valor))
        print("* Objeto HE a eliminar con clave: {}, con valor: {}"
                                                          .format(clave, elim))

print("Los elementos son:", tablaH.elementos)
