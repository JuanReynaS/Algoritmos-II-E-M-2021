# Descripción: En este archivo se implementa el tipo de dato cuckoo table, haciendo
#              uso de los tipo de datos cuckooEntry.
#
# Creado por: Juan Reyna
# email: 10-10883@usb.ve
# version: 1.0



import CuckooEntry as ce


class crearCuckooTable(object):
    """Crea objeto CuckooTable"""

    def __init__(self, n):
        self.n = n
        self.tabla1 = [None] * self.n
        self.tabla2 = [None] * self.n
        self.elementos = 0

    def h1(self, key):
        """ Función de hash método de la división """
        return key % self.n

    def h2(self, key):
        """ Función de hash de la biblioteca estandar python """
        return hash(key) % self.n

    def __rehashing(self, motivo):
        """Es un método privado, es decir, no debe ser usado
           por el usuario. Su objetivo es el de duplicar el
           tama no de la tabla de hash en caso de
           que el factor de carga sea mayor a 0.7
        """

        print("\n*** REHASHING POR {}...".format(motivo))
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

        print("*** REHASHING finalizado con éxito ***\n")

    def factor_carga(self):
        """Retorna el factor de carga actual de la tabla de hash."""
        return self.elementos / self.n

    def agregar(self, c, v):
        """ Se agrega a la tabla de hash una clave c, que tiene asociada un
            valor v. Si la clave a agregar se encuentra en la tabla de hash,
            entonces se sustituye el valor asociado a la clave por el valor
            de v. Debe prevenir que este m ́etodo quede en un ciclo infinito,
            utilizando la condici ́on adecuada para terminar el mismo. Si para
            agregar un elemento es necesario hacer rehashing, entonces las
            tablas duplican su tamano. Si al agregar un elemento, el factor
            de carga es igual o mayor a 0,7, entonces se hace rehashing,
            duplicando el tama ̃no de ambas tablas.
        """

        assert(type(c) == int)
        assert(type(v) == str)

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

        for i in range(self.n):

            if tabla[p] is None:
                tabla[p] = nuevo
                self.elementos += 1

                if self.factor_carga() > 0.7:
                    motivo = "FACTOR DE CARGA {}".format(round(self.factor_carga(), 2))
                    self.__rehashing(motivo)
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
        motivo = "EXCESOS DE COLISIONES"
        self.__rehashing(motivo)
        self.agregar(nuevo.clave, nuevo.valor)

    def buscar(self, c):
        """ Dada un clave c, se busca el elemento en la tabla de hash que
            posea la clave igual a c. Si el elemento se encuentra en la
            tabla, entonces se retorna el valor asociado a esa clave.
            En caso de que no haya ninguna clave c en la tabla de hash, se
            retorna None. """

        assert(type(c) == int)

        if self.tabla1[self.h1(c)] is None and self.tabla2[self.h2(c)] is None:
            return None

        elif (self.tabla1[self.h1(c)] is not None and self.tabla1[self.h1(c)].clave == c):
            return self.tabla1[self.h1(c)].valor

        elif self.tabla2[self.h2(c)] is not None and self.tabla2[self.h2(c)].clave == c:
            return self.tabla2[self.h2(c)].valor

    def eliminar(self, c):
        """
        Dada un clave c, si algún elemento en la tabla de hash tiene una
        clave igual a c, entonces el elemento se elimina de la tabla y se
        retorna el valo asociado a esa clave. En caso de que no haya ninguna
        clave c en la tabla de hash, se retorna None.
        """

        assert(type(c) == int)

        if self.tabla1[self.h1(c)] is None and self.tabla2[self.h2(c)] is None:
            return None

        elif self.tabla1[self.h1(c)] is not None and self.tabla1[self.h1(c)].clave == c:
            value = self.tabla1[self.h1(c)].valor
            self.tabla1[self.h1(c)] = None
            self.elementos -= 1
            return value

        elif self.tabla2[self.h2(c)] is not None and self.tabla2[self.h2(c)].clave == c:
            value = self.tabla2[self.h2(c)].valor
            self.tabla2[self.h2(c)] = None
            self.elementos -= 1
            return value

    def mostrar(self):
        """ Muestra por la salida est ́andar todos los elementos de la tabla
            de hash, en forma de pares clave y valor."""

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
    tabla.agregar(21, "21")
    tabla.agregar(25, "25")
    tabla.agregar(27, "27")
    tabla.agregar(23, "23")
    tabla.agregar(25, "25")
    tabla.agregar(33, "33")
    tabla.agregar(51, "51")
    tabla.agregar(54, "54")
    tabla.agregar(22, "22")
    # print(tabla.buscar(22))
    # print(tabla.tabla1)
    # print(tabla.tabla2)
    print("busqueda", tabla.buscar(29))
    tabla.mostrar()
    print("Hay {} elementos en la tabla".format(tabla.elementos))
    print("Tamaño de la tabla: {}".format(tabla.n))
    # tabla.eliminar(2)
    # tabla.eliminar(25)

    # tabla.mostrar()
    # print("Hay {} elementos en la tabla".format(tabla.elementos))