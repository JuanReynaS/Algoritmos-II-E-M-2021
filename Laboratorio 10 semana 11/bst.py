#
# Implementacion de un Arbol de Busqueda Binario (BST)
#

import sys


# Clase que construye los nodos que conforman el arbol binario
class _BSTNode(object):
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.parent = None
        self.left = None
        self.right = None


class BST(object):
    # Crea un arbol vacio
    def __init__(self):
        self._root = None
        self._size = 0

    # Retorna el numero de elementos del arbol
    def __len__(self):
        return self._size

    # Metodo que retorna un subarbol al encontra una clave dada
    def _bstSearch(self, subTree, target):
        if subTree is None:
            return None
        elif target < subTree.key:
            return self._bstSearch(subTree.left, target)
        elif target > subTree.key:
            return self._bstSearch(subTree.right, target)
        else:
            return subTree

    # Determina si el arbol contiene una clave dada
    # def hasKey(self, key):
    def __contains__(self, key):
        return self._bstSearch(self._root, key) is not None

    # Retorna el valor que esta asosciado a una clave dada
    def valueOf(self, key):
        node = self._bstSearch(self._root, key)
        assert node is not None, "Error, la clave no esta en el arbol."
        return node.value

    # Metodo de ayuda que inserta un nuevo nodo en el arbol
    def _bstInsert(self, subTree, key, value):
        if subTree is None:
            subTree = _BSTNode(key, value)
        elif key < subTree.key:
            subTree.left = self._bstInsert(subTree.left, key, value)
        elif key > subTree.key:
            subTree.right = self._bstInsert(subTree.right, key, value)
        else:
            sys.exit("Error, se esta insertando una clave que ya existe.")
        return subTree

    # Si la clave no se encuentra en el arbol,
    # agrega un nuevo nodo con la clave y el valor, en caso contrario
    # reemplaza el valor de la clave existente por el valor de la entrada
    def add(self, key, value):
        # Busca el nodo que contiene la clave
        node = self._bstSearch(self._root, key)
        # si clave esta en el arbol actualiza su valor
        if node is not None:
            node.value = value
            return False
        # En caso contrario agregamos un nuevo nodo al arbol
        else:
            self._root = self._bstInsert(self._root, key, value)
            self._size += 1
            return True

    # Metodo auxiliar que recorre un arbol "inorder"
    def _inOrderTrav(self, subTree):
        if subTree is not None:
            self._inOrderTrav(subTree.left)
            print("[{0}:{1}] ".format(subTree.key, subTree.value))
            self._inOrderTrav(subTree.right)

    # Imprime el arbol por salida estandar
    def printInorder(self):
        print("Arbol:")
        self._inOrderTrav(self._root)

    def tree_minimun(self, x):
        while x is not None and x.left is not None:
            x = x.left
        return x

    def sucessor(self, x):
        if x.right is not None:
            return self.tree_minimun(x.right)
        else:
            y = x.parent
            while y is not None and x == y.right:
                x = y
                y = y.parent
            return y



    # Metodo auxiliar que elimina un nodo recursivamente dada una clave target
    def _bstRemove(self, subTree, target):
        if subTree is None:
            return subTree
        elif subTree.key < target:
            subTree.right = self._bstRemove(subTree.right, target)

        elif subTree.key > target:
            subTree.left = self._bstRemove(subTree.left, target)

        else:
            if subTree.left is None and subTree.right is None:
                subTree = None
            elif subTree.right is None:
                aux = subTree.left
                subTree = None
                return aux
            elif subTree.left is None:
                aux = subTree.right
                subTree = None
                return aux
            elif subTree.left is not None and subTree.right is not None:
                print("-----Dos hijos", subTree.key)
                y = self.sucessor(self._bstSearch(subTree, target))
                clave = y.key
                valor = y.value
                self._bstRemove(subTree, y.key)
                print(y.key, y.value)
                subTree.key = clave
                subTree.value = valor

        return subTree



    # Elimina el nodo en el arbol que posee la clave dada
    def remove(self, key):
        assert key in self, "Error, clave invalida"
        self.root = self._bstRemove(self._root, key)
        self._size -= -1


raiz = BST()
raiz.add(50, "juan")
raiz.add(30, "Luis")
raiz.add(20, "Karina")
raiz.add(40, "Ana")
raiz.add(70, "Sofia")
raiz.add(60, "Samanta")
raiz.add(80, "Fiorella")
raiz.printInorder()
print("----------------")

raiz.remove(30)
print("")
raiz.printInorder()

raiz.remove(20)
print("")
raiz.printInorder()

raiz.remove(70)
print("")
raiz.printInorder()
