import string as st
import pmli as pm 
import sys
import operator as op
from colorama import Cursor, init, Fore, Style, Back
from progress.counter import Countdown
import time as tm

class crearAyudante():
    def __init__(self):
        self.MAX = 27
        self.lista1 = [i for i in st.ascii_lowercase]
        self.lista1.insert(14,"ñ")
        self.dicc = [pm.crearPMLI(i) for i in self.lista1]

    def esPalabraValida(self, s):
        try:
            assert(type(s) == str)
            for letra in s:
                if not (letra in self.lista1):
                    return False
            return True
        except AssertionError:
            print("Usted ingreso valor que no es string")  
        
    def edit_distance(self, s1, s2):
        try:
            assert(type(s1) == str and type(s2) == str)
            m = dict()
            for i in range(len(s1)+1):
               m[i] = dict()
               m[i][0] = i
            for i in range(len(s2)+1):
               m[0][i] = i
            for i in range(1, len(s1)+1):
                for j in range(1, len(s2)+1):
                    m[i][j] = min(m[i][j-1]+1, m[i-1][j]+1, m[i-1][j-1]+(not s1[i-1] == s2[j-1]))
            return m[len(s1)][len(s2)]
        except AssertionError:
            print("Usted ingreso valores que no son strings")  

    def cargarDiccionario(self, fname):
        try:
            with open(fname) as archivo:
                for linea in archivo:
                    linea = linea[:-1]
                    if self.esPalabraValida(linea) is False:
                        return  False                      
            with open(fname) as archivo:
                for linea in archivo:
                    linea = linea[:-1]
                    for i in range(self.MAX):
                        if self.dicc[i].l == linea[0] and  not linea.isspace() and self.buscarPalabra(linea) is None:
                            self.dicc[i].agregarPalabra(linea)
                            break
            return True
        except IOError:
            print("Usted no está intentando cargar un archivo")        


    def borrarPalabra(self, p):
        try:
            assert(self.esPalabraValida(p) is True)
            for i in range(self.MAX):
                if self.dicc[i].l == p[0] and self.dicc[i].eliminarPalabra(p) is True:
                    return True      
            return None
        except AssertionError:
            return False
    
    def buscarPalabra(self, p):
        try:
            assert(self.esPalabraValida(p) is True)
            for i in range(self.MAX):
                if self.dicc[i].l == p[0] and self.dicc[i].buscarPalabra(p) is True:
                    return True
            return None

        except AssertionError:
            print(Fore.RED + Back.WHITE + Style.BRIGHT + "Palabra no es válida" + Fore.RESET + Back.RESET)
    

    def mostrar(self):
        
        for i in range(self.MAX):
            self.dicc[i].mostrar()
            print(Cursor.DOWN(10) + "\n")


    def corregirTexto(self, finput):
        try:
            c = 40
            d = 1
            e = 0
            print("\n")
            with open(finput) as archivo:
                inicio = tm.time()
                lista_archi = "".join(archivo.readlines()).split()
                lista = []
                contador = len(lista_archi) // 20
                for j in lista_archi:
                    if j not in lista and (self.esPalabraValida(j) is True) and (self.buscarPalabra(j) is not True):
                        lista.append(j)

                    if  (d * contador) == e:
                        print(Cursor.UP(1) + Fore.GREEN + "Extrayendo palabras válidas del texto: ")
                        print(Cursor.FORWARD(60) + Cursor.UP(1) + " {}%".format((e * 100) // len(lista_archi)))
                        print(Cursor.FORWARD(c) + Cursor.UP(1) + "°")
                        d += 1
                        c += 1
                    elif (d * contador) == e and len(lista_archi) > 40:
                        print(Cursor.UP(1)  +  "Buscando sugerencias del diccionario: ")
                        print(Cursor.FORWARD(60) + Cursor.UP(1)  +  " {}% ".format((e  * 100) // len(lista) ))
                        print(Cursor.FORWARD(c) + Cursor.UP(1) + "°")
                        c += 1
                        d += 1

                    e += 1

                print(Cursor.FORWARD(60) + Cursor.UP(1) + " 100%" )
                final = tm.time()

                tiempo1 = final - inicio
                

            c = 40
            e = 0
            d = 1
            
            contador = len(lista) // 20
            print("\n")
            with open("foutput.out", "w") as archivo:
                inicio = tm.time()
                for palabra in lista:
                    dlev = {}
                    for i in range(self.MAX):
                        aux = self.dicc[i].pal.tabla
                        dlev1 = {}
                        for j in range(len(aux)):
                            dlev1 = {}
                            if aux[j] is not None:
                                if len(dlev) < 4:
                                    dlev[aux[j]] = self.edit_distance(aux[j], palabra)
                                else:    
                                    pal_dicc = (aux[j], self.edit_distance(aux[j], palabra)) #tupla diccionario, palabra
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
                      
                    longitud = len(lista)
                    if  longitud <= 40:
                        print(Cursor.UP(1)  +  "Sugiriendo palabras del diccionario: ")
                        print(Cursor.FORWARD(60) + Cursor.UP(1)  +  " 100% ")
                        print(Cursor.FORWARD(c) + Cursor.UP(1) + "°°°°°°°°°°°°°°°°°°°°")
                        longitud = 41

                    elif (d * contador) == e and len(lista) > 40:
                        print(Cursor.UP(1)  +  "Buscando sugerencias del diccionario: ")
                        print(Cursor.FORWARD(60) + Cursor.UP(1)  +  " {}% ".format((e  * 100) // len(lista) ))
                        print(Cursor.FORWARD(c) + Cursor.UP(1) + "°")
                        c += 1
                        d += 1

                    e += 1

                final = tm.time()

                tiempo2 = final - inicio
            
            
            print(Cursor.FORWARD(60) + Cursor.UP(1) + " 100%\n" + Fore.RESET)
            print("Texto corregido\n")
            print("Tiempo de corrección del texto es {}s".format(round(tiempo1 + tiempo2, 3)))
            return "foutput.out"
        except IOError:
            print(Fore.RED + Back.WHITE + Style.BRIGHT + "Usted está intentando cargar un elemento no válido como archivo" + Fore.RESET + Back.RESET)  

if __name__ == '__main__':
    
    helpo = crearAyudante()
    helpo.edit_distance("ergo", "papa")
    helpo.cargarDiccionario(sys.argv[1])
    helpo.mostrar()

    # elpo.borrarPalabra(sys.argv[2])
    # helpo.buscarPalabra(sys.argv[3])
    helpo.corregirTexto(sys.argv[4])
    # helpo.mostrar()




    # with open(sys.argv[4]) as archivo:
    #    for linea in archivo:
    #        lista = linea.split()
    #        print(lista)
