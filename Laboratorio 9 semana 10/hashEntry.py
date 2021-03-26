# Descripción: Contiene una clase con la implementacion del tipo de datos HashEntry.
#
# Creado por: Juan Reyna
# email: 10-10883@usb.ve
# version: 1.0


class HashEntry(object):
    """Clase que contiene atributos de objetos tipo Hash Entry"""

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None
