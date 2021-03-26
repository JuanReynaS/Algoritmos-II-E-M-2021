import dlista as dl


class crear_tabla(object):
    """docstring for crear_tabla"""

    def __init__(self, n):
        self.n = n
        self.tabla = [None] * self.n
        self.elementos = 0


    def agregar(self, c, d):
        """ agregar clave valor """

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
        #    self.mostrar()
        #    print("Factor de carga: {}".format(round(self.factor_carga(),3)))
            self.__rehashing()

    def agregar_elem(self, e):
        """ agregar elemento tipo hash entry """

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
        #    self.mostrar()
        #    print("Factor de carga: {}".format(round(self.factor_carga(),3)))
            self.__rehashing()

    def eliminar(self, c):
        """ Elimina elemento que coincida con una clave dada y retorna su
            asociado, si no existe elemento con clave dada, se retorna None
        """
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
        indice = c % self.n
        
        if self.tabla[indice] is None:
            return None

        return self.tabla[indice].buscar(c)

    def mostrar(self):
        print("*** Tabla de Hash ***")
        for i in range(len(self.tabla)):
            print("{}: {}".format(i, self.tabla[i]))
        print("*** Número de elementos: {} ***\n". format(self.elementos))

    def __rehashing(self):
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
        print("Como queda")
        self.mostrar()
        print("*** REHASHING finalazado con éxito ***")

    def factor_carga(self):
        return self.nelementos() / self.n

    def nelementos(self):
        return self.elementos
