import string as st
import open_htable as ot
from colorama import Cursor, init, Fore, Style, Back
init()

class crearPMLI(object):
    """docstring for crearPMLI"""
    def __init__(self, l):
        assert(type(l) == str)
        self.l = l
        
        self.pal = ot.OpenHtable(26)
        self.lista1 = [i for i in st.ascii_letters]
        self.lista1.insert(14,"ñ")

    def agregarPalabra(self, p):
        assert(type(p) == str and p[0] in self.lista1)
        self.pal.agregar(p)
    
    def eliminarPalabra(self, p):
        assert(type(p) == str and p[0] in self.lista1)
        return self.pal.eliminar(p)

    def buscarPalabra(self, p):
        assert(type(p) == str and p[0] in self.lista1)
        return self.pal.buscar(p)

    def mostrar(self):
        print(Fore.BLACK  + Back.WHITE + "Letra: {}".format(self.l) + Fore.RESET + Back.RESET)
        print(" ")
        e = 0
        c = 0
        d = 1
        for i in sorted([j for j in self.pal.tabla if j is not None]):
            if c < 10:    
                print(Cursor.FORWARD(e) + "* {}".format(i))        
                
                c += 1

            elif c == 10:
                if d == 4:
                    print("-----------------------------------------------------------------------")
                    print(Cursor.BACK(20))
                    e = 0
                    d = 1
                    c = 1

                else:
                    e += 20
                    print(Cursor.FORWARD(e) +  Cursor.UP(10) + "* {}".format(i))
                    c = 1
                    d += 1
                    

        

