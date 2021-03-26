import hashEntry as he


class lista_dobleE(object):
    """docstring for lista_dobleE"""

    def __init__(self):
        self.raiz = None

    def __str__(self):
        if self.raiz is None:
            return "Vacia"
        else:
            Lista_print = "{"
            aux = self.raiz
            while aux is not None:
                Lista_print += "[{}|{}]".format(int(aux.key), aux.value)
                aux = aux.next
                if aux is not None:
                    Lista_print += "<-->"
            Lista_print += "}"

        return Lista_print

    def insertar(self, clave, valor):
        if self.raiz is None:
            nodo = he.HashEntry(clave, valor)
            self.raiz = nodo
            flag = False

        else:
            aux = self.raiz
            while aux is not None:
                if aux.key == clave:
                    aux.value = valor
                    return True
                aux = aux.next
      
            nodo = he.HashEntry(clave, valor)
            nodo.next = self.raiz
            self.raiz.prev = nodo
            self.raiz = nodo
        return False


    def insertar_elem(self, e):

        if self.raiz is None:
            nodo = e
            self.raiz = nodo
            
        else:
            aux = self.raiz
            while aux is not None:
                if aux.key == e.key:
                    aux.value = e.value
                    return True
                aux = aux.next
            
            nodo = e
            nodo.next = self.raiz
            self.raiz.prev = nodo
            self.raiz = nodo
        return False

    def buscar(self, c):
        if self.raiz is None:
            return None
        else:
            aux = self.raiz
            while aux is not None:
                if aux.key == c:
                    return aux.value
                else:
                    aux = aux.next


    def eliminar(self, c):
        if self.raiz is None:
            return None
        
        if self.raiz.next is None:
            if self.raiz.key == c:
                value = self.raiz.value
                self.raiz = None
                return value
        
        if self.raiz.key == c:
            value = self.raiz.value
            self.raiz = self.raiz.next
            self.raiz.prev = None
            return value
           
        aux = self.raiz
        while aux.next is not None:
            if aux.key == c:
                break
            aux = aux.next
        
        if aux.next is not None:
            value = aux.value
            aux.prev.next = aux.next
            aux.next.prev = aux.prev
            return value

        else:
            if aux.key == c:
                value = aux.value
                aux.prev.next = None
                return value                
        return None
    
    def eliminar_elem(self, e):
        
        if self.raiz is None:
            return None
        
        if self.raiz.next is None:
            if self.raiz.key == e.key  and self.raiz.value == e.value:
                value = self.raiz.value
                self.raiz = None
                return value
        
        if  self.raiz.key == e.key  and self.raiz.value == e.value:
            value = self.raiz.value
            self.raiz = self.raiz.next
            self.raiz.prev = None
            return value
           
        aux = self.raiz
        while aux.next is not None:
            if aux.key == e.key  and aux.value == e.value:
                break
            aux = aux.next
        
        if aux.next is not None:
            value = aux.value
            aux.prev.next = aux.next
            aux.next.prev = aux.prev
            return value
        else:
            if aux.key == e.key  and aux.value == e.value:
                value = aux.value
                aux.prev.next = None
                return value

        return None



        if self.raiz is None:
            return None
        else:
            aux = self.raiz
            while aux is not None:
                if aux.key == e.key and aux.value == e.value:
                    aux.prev.next = aux.next
                    aux.next.prev = aux.prev
                    return True
                aux = aux.next
        return False


if __name__ == '__main__':
    alumno1 = he.HashEntry(9, "Juan")
    alumno2 = he.HashEntry(10, "María")
    alumno3 = he.HashEntry(56, "Sofia")
    alumno4 = he.HashEntry(35, "Valentina")
    alumno5 = he.HashEntry(2, "Jose")
    alumno6 = he.HashEntry(11, "Eunis")

    lista = lista_dobleE()
    lista.insertar_elem(alumno1)
    lista.insertar_elem(alumno2)
    lista.insertar_elem(alumno3)
    lista.insertar_elem(alumno4)
    lista.insertar_elem(alumno5)
    lista.insertar_elem(alumno6)
    lista.insertar(20, "Roraima")
    print(lista, "\n\n")
    print("busqueda: ", lista.buscar(10))

    lista.insertar(10, "Fiorella")
    alumno1 = he.HashEntry(9, "Ernesto")
    lista.insertar_elem(alumno1)

    print(lista)
    print("busqueda:", lista.buscar(10))

    print("\n \n")

    print("Eliminar por clave", lista.eliminar(2))

    print(lista)

    print("Eliminar objeto", lista.eliminar_elem(he.HashEntry(3, "Valentina")))

    print(lista)
