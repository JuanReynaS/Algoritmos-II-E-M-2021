import string as st


class crearPMLI(object):
    """docstring for crearPMLI"""
    def __init__(self, l):
        assert(type(l) == str)
        self.l = l
 
        self.lista1 = [i for i in st.ascii_letters]
        self.lista1.insert(14,"ñ")

    def agregarPalabra(self, p):
        assert(type(p) == str and p[0] in self.lista1)