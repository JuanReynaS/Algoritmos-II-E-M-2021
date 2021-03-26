# Descripción: En este archivo se implementa el tipo de datos tabla de hash, haciendo
#              uso de los tipo de datos HashEntry y Dlist.  
#
#
# Creado por: Juan Reyna
# email: 10-10883@usb.ve
# version: 1.0


import dlista as dl


class crear_tabla(object):
    """Clase que construye una tabla de Hash"""

    def __init__(self, n):
        self.n = n
        self.tabla = [None] * self.n
        self.elementos = 0


    def agregar(self, c, d):
        """ Se agrega a la tabla de hash una clave c, que tiene asociada un
            dato de tipo String d. Si la clave a agregar se encuentra en la
            tabla de hash, entonces se sustituye el valor del dato en la tabla
            de hash por el valor de d."""

        assert(type(c) == int)
        assert(type(d) == str)
        indice = c % self.n
        if self.tabla[indice] is None:
            self.elementos += 1
            self.tabla[indice] = dl.lista_dobleE()        
            self.tabla[indice].insertar(c, d)
        else:
            if self.tabla[indice].insertar(c, d) == True:
                pass
            else:
                self.elementos += 1
        if self.factor_carga() > 0.7:
            self.mostrar()
            print("Factor de carga: {}".format(round(self.factor_carga(),3)))
            self.__rehashing()

    def agregar_elem(self, e):
        """ Se agrega un elemento e de tipo HashEntry a la tabla de hash. Si
            la clave del elemento agregar e.clave se encuentra en la tabla de
            hash, entonces se sustituye el objeto HashEntry en la tabla de hash
            por el objeto de la entrada e. """

        indice = e.key % self.n
        if self.tabla[indice] is None:
            self.elementos += 1
            self.tabla[indice] = dl.lista_dobleE()
            self.tabla[indice].insertar_elem(e)
        else:         
            if self.tabla[indice].insertar_elem(e) == True:
                pass
            else:
                self.elementos += 1
        if self.factor_carga() > 0.7:
            self.mostrar()
            print("Factor de carga: {}".format(round(self.factor_carga(),3)))
            self.__rehashing()

    def eliminar(self, c):
        """Dada un clave c, si alg ́un elemento en la tabla de hash tiene una
           clave igual a c, entonces el elemento se elimina de la tabla y retorna
           el String asociado a esa clave. En caso de que no haya ninguna clave
           c en la tabla de hash, se retorna None. """
        
        assert(type(c) == int)
        indice = c % self.n
        if self.elementos == 0 or self.tabla[indice] is None:
            return None

        value = self.tabla[indice].eliminar(c)
        if value is None:
            return value
        else:  
            self.elementos -= 1
            return value


    def eliminar_elem(self, e):
        """ Dada una referencia de un elemento e de tipo HashEntry de la tabla
            de hash, entonces se elimina a e de la tabla y se retorna T rue.
            Si e no es una referencia a un elemento en la tabla de hash, entonces
            la operaci ́on no tiene ning ́un efecto en la tabla y se retorna F alse."""
        
        indice = e.key % self.n
        if self.elementos == 0 or self.tabla[indice] is None:
            return None
        
        value = self.tabla[indice].eliminar_elem(e)
        if value is None:
            return False
        else:
            self.elementos -= 1    
            return True
            


    def buscar(self, c):
        """ Dada un clave c, se busca el elemento en la tabla de hash que posea la
            clave igual a c. Si el elemento se encuentra en la tabla, entonces se retorna
            el String asociado a esa clave. En caso de que no haya ninguna clave c en la
            tabla de hash, se retorna None. """

        assert(type(c) == int)
        indice = c % self.n
        if self.tabla[indice] is None:
            return None

        return self.tabla[indice].buscar(c)

    def mostrar(self):
        """Se muestra por la salida est ́andar todos los elementos de la tabla
           de hash, en forma de pares clave y valor asociado."""

        print("*** Tabla de Hash ***")
        for i in range(len(self.tabla)):
            print("{}: {}".format(i, self.tabla[i]))
        print("*** Número de elementos: {} ***\n". format(self.elementos))

    def __rehashing(self):
        """Es un m ́etodo privado, es decir, no debe ser usado por el usuario.
           Su objetivo es el de duplicar el tama ̃no de la tabla de hash en caso de
           que el factor"""

        print("REHASHING...")
        tabla_aux = crear_tabla(self.n * 2)
        nlongitud = len(tabla_aux.tabla)
        self.elementos = 0
        for i in range(len(self.tabla)):
            if self.tabla[i] is not None:
                aux = self.tabla[i].raiz
                while aux is not None:
                    tabla_aux.agregar(aux.key, aux.value)
                    aux = aux.next
                    self.elementos += 1


        self.tabla = tabla_aux.tabla
        print("*** REHASHING finalizado con éxito ***")
        self.mostrar()
        

    def factor_carga(self):
        """Retorna el factor de carga actual de la tabla de hash."""
        return self.nelementos() / self.n

    def nelementos(self):
        """Retorna el n ́umero de elementos en la tabla de hash."""
        return self.elementos
