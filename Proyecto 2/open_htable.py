class OpenHtable(object):
    """docstring for ClassName"""
    def __init__(self, n):
        self.tabla = [None] * n
        self.n = n
        self.elementos = 0
    
    def h(self, key, i):
        return ((key % self.n) + i) % self.n

    def agregar(self, k):
        i = 0
        m = 0
        while i < self.n:
            casilla = self.h(k, i)

            if self.tabla[casilla] is None:
                self.tabla[casilla] = k
                print("casilla: {}".format(casilla))
                return

            else:
                if m == self.n:
                    print("Desbordamiento de la tabla")
                    return                
                elif i == self.n - 1:
                    i = 0
                    m += 1
                else:
                    i += 1
                    m += 1

    def buscar(self, k):
        i = 0
        m = 0
        while i < self.n:
            casilla = self.h(k, i)

            if self.tabla[casilla] == k:
                print("Clave encontrada: {}, en casilla: {}".format(self.tabla[casilla], casilla))
                return

            else:
                if m == self.n:
                    return None

                elif i == self.n - 1:
                    i = 0
                    m += 1
                else:
                    i += 1
                    m += 1

    def eliminar(self, k):
        i = 0
        m = 0
        while i < self.n:
            casilla = self.h(k, i)

            if self.tabla[casilla] == k:
                self.tabla[casilla] = None
                print("Clave eliminada: {}, en casilla: {}".format(self.tabla[casilla], casilla))
                return

            else:
                if m == self.n:
                    return None

                elif i == self.n - 1:
                    i = 0
                    m += 1
                else:
                    i += 1
                    m += 1



if __name__ == '__main__':
    tabla = OpenHtable(8)
    tabla.agregar(16)
    tabla.agregar(2)
    tabla.agregar(3)
    tabla.agregar(11)
    tabla.agregar(5)
    tabla.agregar(6)
    tabla.agregar(27)
    tabla.agregar(8)
    #tabla.agregar(18)
    tabla.buscar(8)
    tabla.buscar(27)      
    tabla.eliminar(27)
    tabla.eliminar(11)    
    tabla.eliminar(16)      
    print(tabla.tabla)
