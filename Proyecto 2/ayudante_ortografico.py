import pmli as pm 

class crearAyudante():
    def __init__(self):
        MAX = 27
        self.lista1 = [i for i in st.ascii_letters]
        self.lista1.insert(14,"ñ")
        
        self.dicc = [pm.crearPMLI(i) for i in self.lista1]

    def esPalabraValida(s):
        assert(type(s) == str)
     
        self.lista1 = [i for i in st.ascii_letters]
        self.lista1.insert(14,"ñ")

        for letra in s:
            if not (letra in lista1):
                return False
        return True

    def cargarDiccionario(self, fname):
        archivo = open(fname + ".txt", "r")
        for linea in archivo:
            if esPalabraValida(linea) is True:

            elif (esPalabraValida(linea)) is False:
                return

        archivo.close()