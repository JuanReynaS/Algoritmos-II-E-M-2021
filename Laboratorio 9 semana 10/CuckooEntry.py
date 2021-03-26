class crearCuckooEntry(object):
    """docstring for crearCuckooEntry"""

    def __init__(self, clave, valor):
        assert(type(clave) == int)
        assert(type(valor) == str)
        self.clave = clave
        self.valor = valor
