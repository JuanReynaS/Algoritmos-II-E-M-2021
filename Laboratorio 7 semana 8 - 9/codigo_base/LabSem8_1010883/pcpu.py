class Proceso(object):

    def __init__(self, identificador, tiempo_quemado, prioridad_CPU, tiempo_llegada):
        self.identificador = identificador
        self.tiempo_quemado = tiempo_quemado
        self.prioridad_CPU = prioridad_CPU
        self.tiempo_llegada = tiempo_llegada

