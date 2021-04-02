import string as st
import pmli as pm 
import sys
import operator as op

class crearAyudante():
    def __init__(self):
        self.MAX = 27
        self.lista1 = [i for i in st.ascii_lowercase]
        self.lista1.insert(14,"ñ")
        
        self.dicc = [pm.crearPMLI(i) for i in self.lista1]

    def esPalabraValida(self, s):
        assert(type(s) == str)
        for letra in s:
            if not (letra in self.lista1):
                return False
        return True
        
    def distance(self, s1, s2):
        d=dict()
        for i in range(len(s1)+1):
           d[i]=dict()
           d[i][0]=i
        for i in range(len(s2)+1):
           d[0][i] = i
        for i in range(1, len(s1)+1):
            for j in range(1, len(s2)+1):
                d[i][j] = min(d[i][j-1]+1, d[i-1][j]+1, d[i-1][j-1]+(not s1[i-1] == s2[j-1]))
        return d[len(s1)][len(s2)]    

    def cargarDiccionario(self, fname):
        with open(fname) as archivo:
            for linea in archivo:
                linea = linea[:-1].lower()
                # print(linea)
                if self.esPalabraValida(linea) is True:
                    for i in range(self.MAX):
                        if self.dicc[i].l == linea[0] and  not linea.isspace():
                            #print(i, self.dicc[i].l, len(self.dicc))
                            #resolver las lineas en blamco
                            self.dicc[i].agregarPalabra(linea)
                            break              
                else:
                    return

    def borrarPalabra(self, p):
        assert(self.esPalabraValida(p) is True)
        for i in range(self.MAX):
            if self.dicc[i].l == p[0] and self.dicc[i].eliminarPalabra(p) is True:
                return           

    def buscarPalabra(self, p):
        assert(self.esPalabraValida(p) is True)
        for i in range(self.MAX):
            if self.dicc[i].l == p[0] and self.dicc[i].buscarPalabra(p) is True:
                return True

    def mostrar(self):
        for i in range(self.MAX):
            self.dicc[i].mostrar() 
            print("\n")

    def corregirTexto(self, finput):
        lista_let = []
        with open(finput) as archivo:
            lista_archi = "".join(archivo.readlines()).split()
            # print(lista_archi)
            for casilla in lista_archi:
                if self.esPalabraValida(casilla) is True:
                    lista_let.append(casilla)
                else:
                    aux = ""
                    #rint(casilla)
                    for l in  casilla:
                        if (l in st.punctuation) or (l in st.digits) or (l in st.whitespace):
                            if len(aux) > 0:
                                lista_let.append(aux)
                            aux = ""
                            
                        elif (l not in st.punctuation) and (l not in st.digits) and (l not in st.whitespace):
                            aux += l
                    if len(aux) > 0:
                        lista_let.append(aux)
            #print("\n \n \n######################################################")
            # print(lista_let)

            
            # lista = [i for i in lista_let
            #         if (self.esPalabraValida(i) is True) and (self.buscarPalabra(i) is not True)]
            # lista = [i for i in lista if lista.count(i) == 1]

            lista = []
            for j in lista_let:
                if j not in lista and (self.esPalabraValida(j) is True) and (self.buscarPalabra(j) is not True):
                    lista.append(j)

            for palabra in lista:
                dlev = {}
                for i in range(self.MAX):
                    aux = self.dicc[i].pal.tabla
                    dlev1 = {}
                    for j in range(len(aux)):
                        dlev1 = {}
                        if aux[j] is not None:
                            if len(dlev) < 4:
                                dlev[aux[j]] = self.distance(aux[j], palabra)
                            else:    
                                pal_dicc = (aux[j], self.distance(aux[j], palabra))
                                dlev = dict(sorted([i for i in dlev.items()], key=lambda x: x[1]))
                                for i in dlev.items():
                                    if i[1] <= pal_dicc[1] and len(dlev1) < 4:
                                        dlev1[i[0]] = i[1]  
                                    elif i[1] > pal_dicc[1] and len(dlev1) < 4:       
                                        dlev1[pal_dicc[0]] = pal_dicc[1]    
                                        pal_dicc = i

                                dlev = dlev1

                with open("foutput.txt", "a") as archivo:
                    salida = dlev
                    salida = [clave for clave in salida.keys()]
                    salida.insert(0, palabra)
                    salida = ",".join(salida)
                    archivo.write(salida)
                    archivo.write("\n")

                                
                        
                        

                
                # for i in d.items():
                # print("*", lista,"\n")


helpo = crearAyudante()
helpo.cargarDiccionario(sys.argv[1])

# print(helpo.mostrar())

# elpo.borrarPalabra(sys.argv[2])
# helpo.buscarPalabra(sys.argv[3])
helpo.corregirTexto(sys.argv[4])
# helpo.mostrar()




# with open(sys.argv[4]) as archivo:
#    for linea in archivo:
#        lista = linea.split()
#        print(lista)
