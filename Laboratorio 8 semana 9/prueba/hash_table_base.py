import hashEntry as he

class Hash_table_base:

    def __init__(self, n):
        self.n = n
        self.table = {}

    def agregar_elem(self, e):
        self.table[e.key] = e

    def agregar(self, c, d):
        self.table[c] = he.HashEntry(c, d)

    def eliminar_elem(self, e):
        if e.key in self.table:
            self.table.pop(e.key)

    def eliminar(self, c):
        if c in self.table:
            value = self.table[c].value
            self.table.pop(c)
            return value
        else:
            return None
            
    def buscar(self, c):
        if c in self.table:
            return self.table[c].value
        else:
            return None
        
    def mostrar(self):
        print()
        print("*****************************************")
        print("Mostrando la tabla de hash")
        print()
        for k in self.table:
            print("Clave: "+str(k)+" -- Valor: "+self.table[k].value)
        print("*****************************************")

    def numero_elementos(self):
        return len(self.table)

    def obtener_claves(self):
        return self.table.keys()

