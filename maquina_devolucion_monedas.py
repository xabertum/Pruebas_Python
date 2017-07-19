# -*- coding: utf-8 -*-

import math

cantidad = float(input('Introduce la cantidad a devolver: '))

cantidad_monedas_euro = math.trunc(cantidad)
i = 25

def devolucion(cantidad, tipo):
    for i in range(0, cantidad):
        cantidad -= tipo
        return i


print devolucion(25, 1)
