#!/usr/bin/env python3

import unittest
import hash_table_base as htb
import tabla_hash as ht
import random as rd
import hashEntry as he

class TestStringMethods(unittest.TestCase):

    def data_generation(self, n, m, s):
        assert(n > 0)
        data = []
        rd.seed(s)
        for i in range(0, m):
            value = rd.randint(1, n)
            data.append((value, str(value)))
        return data

    def contain_all(self, mht, mhtb):
        hkeys = mhtb.obtener_claves()
        for key in hkeys:
            valueb = mhtb.buscar(key)
            assert(valueb)
            value = mht.buscar(key)
            if not value:
                print("Error, Missing key "+str(key))
                return False
            if not valueb == value:
                print("Error searching, Missing values with same key")
                print("Key: "+str(key))
                print("Value ht: "+value+" Value ht base: "+valueb)
                return False
        return True

    def delete_all_w_key(self, mht, mhtb):
        for key in mhtb.table:
            valueb = mhtb.buscar(key)
            assert(valueb)
            value = mht.eliminar(key)
            if not value:
                print("Error deleting the key "+str(key))
                return False
            if not valueb == value:
                print("Error deleting, Missing values with same key")
                print("Key: "+str(key))
                print("Value ht: "+value+" Value ht base: "+valueb)
                return False
        return True
    
    def test_one(self):
        print("")
        print("---- Starting test one ---- ")
        n = 10
        s1 = 191275
        my_ht = ht.crear_tabla(n)
        my_htb = htb.Hash_table_base(n)
        data1 = self.data_generation(n, 2*n, s1)
        for (key, value) in data1:
            my_ht.agregar(key, value)
            my_htb.agregar(key, value)
        self.assertTrue(self.contain_all(my_ht, my_htb))
        print("The table contain all the elements for Test one")
        for (key, value) in data1:
            my_entry = he.HashEntry(key, value)
            my_ht.agregar_elem(my_entry)
            my_htb.agregar_elem(my_entry)
        self.assertTrue(self.contain_all(my_ht, my_htb))
        print("***********************")
        print("Tabla base:")
        my_htb.mostrar()
        print("***********************")
        print("Tabla a evaluar:")
        my_ht.mostrar()
        print("Test one done")

    def test_two(self):
        print("")
        print("---- Starting test two ---- ")
        n = 62233
        s1 = 191282
        icont = 0
        dcont = 0
        my_ht = ht.crear_tabla(n)
        my_htb = htb.Hash_table_base(n)
        m = 10*n
        data1 = self.data_generation(m, m, s1)
        for (key, value) in data1:
            if not my_ht.buscar(key):
                my_ht.agregar(key, value)
                my_htb.agregar(key, value)
                icont += 1
            else:
                my_ht.eliminar(key)
                my_htb.eliminar(key)
                dcont += 1
        print("Num. of insertions: "+str(icont))
        print("Num. of deletions: "+str(dcont))
        print("Num. of elements in base table: "+str(my_htb.numero_elementos()))
        self.assertTrue(self.contain_all(my_ht, my_htb))
        print("The table contain all the elements for Test two")
        self.assertTrue(self.delete_all_w_key(my_ht, my_htb))
        print("All the elements in the table were erase")
        self.assertTrue(self.not_contain_all(my_ht, my_htb))
        print("The table does not contain any element inserted")
        print("Printing the hash table in test two")
        my_ht.mostrar()
        print("Test two done")

    def data_generation(self, n, m, s):
        assert(n > 0)
        data = []
        rd.seed(s)
        for i in range(0, m):
            value = rd.randint(1, n)
            data.append((value, str(value)))
        return data

    def data_entry_generation(self, n, m, s):
        assert(n > 0)
        data = {}
        rd.seed(s)
        for i in range(0, m):
            value = rd.randint(1, n)
            if value not in data:
                hentry = he.HashEntry(value, str(value))
                data[value] = hentry
        return data.values()

    def delete_all_w_entry(self, data, mht):
        for entry in data:
            value = mht.eliminar_elem(entry)

    def not_contain_all(self, mht, mhtb):
        hkeys = mhtb.obtener_claves()
        for key in hkeys:
            value = mht.buscar(key)
            if value:
                print("Error, the key "+str(key)+" is in hash table")
                return False
        return True
            
    def test_three(self):
        print("")
        print("---- Starting test three ---- ")
        n = 62233
        s = 191635
        my_ht = ht.crear_tabla(n)
        my_htb = htb.Hash_table_base(n)
        icont = 0
        dcont = 0
        m = 10*n
        p = 20*n
        data = self.data_entry_generation(p, m, s)
        for e in data:
            assert(not my_htb.buscar(e.clave))
            my_ht.agregar_elem(e)
            my_htb.agregar_elem(e)
        self.assertTrue(self.contain_all(my_ht, my_htb))
        print("The table contain all the elements for Test three")
        self.delete_all_w_entry(data, my_ht)
        print("All the elements in the table were erase")
        self.assertTrue(self.not_contain_all(my_ht, my_htb))
        print("The table does not contain any element inserted")
        print("Printing the hash table in test two")
        my_ht.mostrar()
        print("Test three done")
        
if __name__ == '__main__':
    unittest.main()

