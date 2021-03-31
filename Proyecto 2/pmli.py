import string as st
import open_htable as ot

class crearPMLI(object):
    """docstring for crearPMLI"""
    def __init__(self, l):
        assert(type(l) == str)
        self.l = l
        
        self.pal = ot.OpenHtable(27)
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

