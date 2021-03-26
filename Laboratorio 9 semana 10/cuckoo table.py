# https://www.educative.io/edpresso/the-fatal-refusing-to-merge-unrelated-histories-git-error
# https://github.com/DeborahHier/CuckooHash/blob/master/CuckooHash.py
import CuckooEntry as ce


class crearCuckooTable(object):
    """docstring for crearCuckooTable"""

    def __init__(self, n):
        self.n = n
        self.tabla1 = [None] * self.n
        self.tabla2 = [None] * self.n
        self.elementos = 0

    def h1(self, key):
        return key % self.n

    def h2(self, key):
        return hash(key) % self.n

    def __rehashing(self):
        print("REHASHING...")
        tabla_aux = crearCuckooTable(self.n * 2)
        nlongitud = tabla_aux.n
        self.elementos = 0
        for i in range(self.n):
            if self.tabla1[i] is not None:
                tabla_aux.agregar(self.tabla1[i].clave, self.tabla1[i].valor)
            
            if self.tabla2[i] is not None:
                tabla_aux.agregar(self.tabla2[i].clave, self.tabla2[i].valor)
        
        self.tabla1 = tabla_aux.tabla1
        self.tabla2 = tabla_aux.tabla2
        self.elementos = tabla_aux.elementos
        self.n = self.n * 2

        print("*** REHASHING finalizado con éxito ***")

    def factor_carga(self):
        """Retorna el factor de carga actual de la tabla de hash."""
        return self.elementos / self.n

    def agregar(self, c, v):
        if self.buscar(c) is not None:
            if (self.tabla1[self.h1(c)] is None and self.tabla2[self.h2(c)].clave == c):
                self.tabla2[self.h2(c)].valor = v
            elif self.tabla2[self.h2(c)] is None and self.tabla1[self.h1(c)].clave == c:
                self.tabla1[self.h1(c)].valor = v
            return

        nuevo = ce.crearCuckooEntry(c, v)


        q = self.h1(nuevo.clave)
        p = q
        tabla = self.tabla1

        for i in range(10):

            if tabla[p] is None:
                tabla[p] = nuevo
                self.elementos += 1
                
                if self.factor_carga() > 0.7:
                    self.__rehashing()
                return

            nuevo, tabla[p] = tabla[p], nuevo

            if p == q:
                q = self.h1(nuevo.clave)
                r = self.h2(nuevo.clave)
                p = r
                tabla = self.tabla2
            else:
                q = self.h1(nuevo.clave)
                r = self.h2(nuevo.clave)
                p == q
                tabla = self.tabla1

        self.__rehashing()
        self.agregar(nuevo.clave, nuevo.valor)

    def buscar(self, c):
        if self.tabla1[self.h1(c)] is None and self.tabla2[self.h2(c)] is None:
            return None
        
        elif (self.tabla1[self.h1(c)] is not None and self.tabla1[self.h1(c)].clave == c):
            return self.tabla1[self.h1(c)].valor
        
        elif self.tabla2[self.h2(c)] is not None and self.tabla2[self.h2(c)].clave == c:
            return self.tabla2[self.h2(c)].valor

    def eliminar(self, c):
        if self.tabla1[self.h1(c)] is None and self.tabla2[self.h2(c)] is None:
            return None

        elif self.tabla1[self.h1(c)].clave == c:
            value = self.tabla1[self.h1(c)].valor
            self.tabla1[self.h1(c)] = None
            self.elementos -= 1
            return value

        elif self.tabla2[self.h2(c)].clave == c:
            value = self.tabla2[self.h2(c)].valor
            self.tabla2[self.h2(c)] = None
            self.elementos -= 1
            return value

    def mostrar(self):
        print("\nTabla1 \t\t\t\t Tabla2")
        for i in range(self.n):
            tabla1 = self.tabla1[i]
            tabla2 = self.tabla2[i]
            if tabla1 is None and tabla2 is not None:
                print("{0}: {1} \t \t \t {0}: {2}".format(i, None, (tabla2.clave, tabla2.valor )))

            elif tabla1 is not None and tabla2 is None:
                print("{0}: {1} \t \t \t {0}: {2}".format(i, (tabla1.clave, tabla1.valor ), None))

            elif tabla1 is not None and tabla2 is not None:
                print("{0}: {1} \t \t \t {0}: {2}".format(i, (tabla1.clave, tabla1.valor), (tabla2.clave, tabla2.valor )))

            elif tabla1 is None and tabla2 is None:
                print("{0}: {1} \t \t \t {0}: {2}".format(i, None, None) )



if __name__ == '__main__':
    tabla = crearCuckooTable(10)
    print("Tamaño de la tabla: {}".format(tabla.n))
    tabla.agregar(2, "2")
    tabla.agregar(42, "42")
    tabla.agregar(22, "22")
    tabla.agregar(25, "25")
    tabla.agregar(27, "27")
    tabla.agregar(23, "23")
    tabla.agregar(25, "25")
    tabla.agregar(33, "33")
    tabla.agregar(51, "51")
    tabla.agregar(54, "54")
    # print(tabla.buscar(22))
    # print(tabla.tabla1)
    # print(tabla.tabla2)
    # print(tabla.buscar(25))
    tabla.mostrar()
    print("Hay {} elementos en la tabla".format(tabla.elementos))
    print("Tamaño de la tabla: {}".format(tabla.n))
    # tabla.eliminar(2)
    # tabla.eliminar(25)

    # tabla.mostrar()
    # print("Hay {} elementos en la tabla".format(tabla.elementos))