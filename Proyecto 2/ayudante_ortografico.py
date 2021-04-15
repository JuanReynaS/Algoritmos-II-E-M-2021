mport sys
from colorama import Cursor, init, Fore, Style, Back
import time as tm
import string as st
import pmli as pm
import re
import os.path as osp

init()

class crearAyudante():
    def __init__(self):
        self.MAX = 27
        self.lista1 = [i for i in st.ascii_lowercase]
        self.lista1.insert(14, "ñ")
        self.dicc = [pm.crearPMLI(i) for i in self.lista1]
        self.guar_dicc = []

    def esPalabraValida(self, s):
        """ Este método recibe un string y retorna True si cada caracter del
            string es una letra minúscula del abecedario.
        """
        try:
            assert(type(s) == str)
            for letra in s:
                if not (letra in self.lista1):
                    return False
            return True
        except AssertionError:
            print("Usted ingreso valor que no es string")

    def edit_distance(self, s1, s2):
        """ Este método recibe dos strings y retorna la distancia 
            de Levenshtein (valor entero) que existe entre ambas.
        """
        try:
            assert(type(s1) == str and type(s2) == str)
            m = dict()
            for i in range(len(s1) + 1):
                m[i] = dict()
                m[i][0] = i
            for i in range(len(s2) + 1):
                m[0][i] = i
            for i in range(1, len(s1) + 1):
                for j in range(1, len(s2) + 1):
                    m[i][j] = min(m[i][j - 1] + 1,
                                  m[i - 1][j] + 1,
                                  m[i - 1][j - 1]
                                  + (not s1[i - 1] == s2[j - 1]))
            return m[len(s1)][len(s2)]
        
        except AssertionError:
            print("Usted ingreso valores que no son strings")

    def cargarDiccionario(self, fname):
        """Este método recibe un archivo, si el archivo contiene una palabra
           válida por línea y tiene extensión txt. Se carga su contenido en
           corrector ortogréfico y retorna True. Si se encuentra una palabra no
           válida se retorna False           
        """
        try:
            
            ubicacion = osp.isfile(fname)            
            assert(ubicacion is True), "Archivo no existe en la ruta indicada"
            
            cola, ext = osp.splitext(fname)
            assert(ext == ".txt"), "El archivo indicado no tiene formato txt"

            ruta, nombre = osp.split(fname)
            if nombre in self.guar_dicc:
                return None

            with open(fname, "r", encoding="utf8") as archivo:
                for linea in archivo:
                    linea = linea[:-1]
                    if self.esPalabraValida(linea) is False:
                        # Se encontró palabra no válida
                        return False

            self.guar_dicc.append(nombre)
            with open(fname, "r", encoding="utf8") as archivo:
                for linea in archivo:
                    linea = linea[:-1]
                    for i in range(self.MAX):
                        if (self.dicc[i].l == linea[0]
                            and not linea.isspace()
                            and self.buscarPalabra(linea) is None):
                            
                            self.dicc[i].agregarPalabra(linea)
                            break
            # Se cargó con exitó el diccionario
            return True
        
        except AssertionError as error:         
            return error

    def borrarPalabra(self, p):
        """Este procedimiento recibe como entrada una palabra, si la misma
           se encuentra en dicc la elimina se retorna True.
           Si la palabra no se encuentra en retorna None.
        """

        try:
            assert(self.esPalabraValida(p) is True)
            for i in range(self.MAX):
                if (self.dicc[i].l == p[0]
                    and self.dicc[i].eliminarPalabra(p) is True):
                    return True
            return None
        except AssertionError:
            return False

    def buscarPalabra(self, p):
        """Este método recibe un string, si es válido es buscado la estructura
           dicc. Si es encontrada la palabra retorna True en caso contrario
           retorna None
        """
        try:
            assert(self.esPalabraValida(p) is True)
            for i in range(self.MAX):
                if (self.dicc[i].l == p[0]
                    and self.dicc[i].buscarPalabra(p) is True):
                    return True
            return None

        except AssertionError:
            print(Fore.RED + Back.WHITE + Style.BRIGHT
                  + "Palabra no es válida" + Fore.RESET + Back.RESET)

    def imprimirDiccionario(self):
        """Imprime por la salida estándar la estructura dicc"""
        for i in range(self.MAX):
            self.dicc[i].mostrar()
            print(Cursor.DOWN(10) + "\n")

    def corregirTexto(self, finput):
        """Este método recibe la ruta de un archivo si el archivo existe y tiene
           extensión txt, extonces busca en el archivo las palabras válidas que
           no están en el diccionario y a cada una de ellas se le sugieren 4 
           palabras del diccionario con menor distancia Levenshtein.

           Este metodo crea un archivo que en cada línea tiene 5 palabras
           separadas por coma, la primera de esas palabras es la palabra válida
           del extraída del texto y las otras 4 son las sugerencias del
           diccionario
        """
        try:
            
            ubicacion = osp.isfile(finput)            
            assert(ubicacion is True), "Archivo no existe en la ruta indicada"
            
            cola, ext = osp.splitext(finput)
            assert(ext == ".txt"), "El archivo indicado no tiene formato txt"
                      
            c = 40
            d = 1
            e = 0
            print("\n")
            with open(finput, "r", encoding="utf8") as archivo:
                inicio = tm.time()
                cadena_arch = "".join(archivo.readlines())
                lista_archi = re.sub('[%s]' % re.escape(st.punctuation), ' ',
                                     cadena_arch).split()
                lista = []
                contador = len(lista_archi) // 20
                for j in lista_archi:
                    if (j not in lista and (self.esPalabraValida(j) is True)
                        and (self.buscarPalabra(j) is not True)):

                        lista.append(j)


                    longitud = len(lista_archi)
                    if longitud <= 40:
                        print(Cursor.UP(1) + Fore.GREEN
                              + "Extrayendo palabras válidas del texto: ")
                        print(Cursor.FORWARD(60) + Cursor.UP(1) + " 100% ")
                        print(Cursor.FORWARD(c) + Cursor.UP(1)
                              + "°°°°°°°°°°°°°°°°°°°°")
                        longitud = 41
                    elif (d * contador) == e and len(lista_archi) > 40:
                        print(Cursor.UP(1) + Fore.GREEN
                              +  "Extrayendo palabras válidas del texto: ")
                        print(Cursor.FORWARD(60)
                              + Cursor.UP(1)
                              +  " {}%".format((e * 100) // len(lista_archi)))
                        print(Cursor.FORWARD(c)
                              + Cursor.UP(1) + "°")
                        c += 1
                        d += 1
                    e += 1

                print(Cursor.FORWARD(60) + Cursor.UP(1) + " 100%" + Fore.RESET)

                final = tm.time()

                tiempo1 = final - inicio

            c = 40
            e = 0
            d = 1

            contador = len(lista) // 20
            print("\n")
            print(Fore.GREEN + "Leyendo diccionario...")
            with open("foutput.out", "w") as archivo:
                inicio = tm.time()
                
                for palabra in lista:
                    dlev = {}
                    longitud = len(lista)
                    
                    if longitud <= 40:
                        print(Cursor.UP(1)
                              + "Sugiriendo palabras del diccionario: ")
                        print(Cursor.FORWARD(60) + Cursor.UP(1) + " 100% ")
                        print(Cursor.FORWARD(c) + Cursor.UP(1)
                              + "°°°°°°°°°°°°°°°°°°°°")
                        longitud = 41

                    elif (d * contador) == e and len(lista) > 40:
                        print(Cursor.UP(1)
                              + "Sugiriendo palabras del diccionario: ")
                        print(Cursor.FORWARD(60) + Cursor.UP(1)  
                              + " {}% ".format((e  * 100) // len(lista) ))
                        print(Cursor.FORWARD(c) + Cursor.UP(1) + "°")
                        c += 1
                        d += 1
                    e += 1

                    for i in range(self.MAX):
                        aux = self.dicc[i].pal.tabla
                        dlev1 = {}
                        for j in range(len(aux)):
                            dlev1 = {}
                            if aux[j] is not None:
                                if len(dlev) < 4:
                                    dlev[aux[j]] = self.edit_distance(aux[j], palabra)
                                else:
                                    
                                    pal_dicc = (aux[j], 
                                                self.edit_distance(aux[j], palabra)
                                               ) 
                                    
                                    dlev = dict(sorted([i for i in dlev.items()], key=lambda x: x[1]))
                                    for i in dlev.items():
                                        if i[1] <= pal_dicc[1] and len(dlev1) < 4:
                                            dlev1[i[0]] = i[1]
                                        elif i[1] > pal_dicc[1] and len(dlev1) < 4:
                                            dlev1[pal_dicc[0]] = pal_dicc[1]
                                            pal_dicc = i

                                    dlev = dlev1

                    salida = dlev
                    salida = [clave for clave in salida.keys()]
                    salida.insert(0, palabra)
                    salida = ",".join(salida)
                    archivo.write(salida)
                    archivo.write("\n")

                final = tm.time()

                tiempo2 = final - inicio
            print(Cursor.FORWARD(60) + Cursor.UP(1) + " 100%\n" + Fore.RESET)
            print("Texto corregido\n")
            print("\nTiempo de corrección del texto: {}s".format(round(tiempo1 + tiempo2, 3)))
            return None 
        
        except AssertionError as error:
            return error


if __name__ == '__main__':

    helpo = crearAyudante()
    helpo.edit_distance("ergo", "papa")
    helpo.cargarDiccionario(sys.argv[1])
    helpo.imprimirDiccionario()

    # elpo.borrarPalabra(sys.argv[2])
    # helpo.buscarPalabra(sys.argv[3])
    helpo.corregirTexto(sys.argv[4])
    # helpo.mostrar()




    # with open(sys.argv[4]) as archivo:
    #    for linea in archivo:
    #        lista = linea.split()
    #        print(lista)
