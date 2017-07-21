# -*- coding: utf-8 -*-
import math

cant_info = raw_input('Introduce una cantidad de información')
unidad_info = raw_input('¿ En que unidad esta expresada ? (bit, byte, KB, MB o GB) : ')
unidad_info_conv = raw_input('A que unidad desesa convertir (bit, byte, KB, MB o GB)')

def conversor(cant, unidad, unidad_conv):
    if unidad == unidad_conv:
        pass
    else:
        if unidad == 'bit' and unidad_conv == 'KB':
            cant = float(cant) * math.pow(10, -3)
        if unidad == 'bit' and unidad_conv == 'MB':
            cant = float(cant) * math.pow(10, -6)
        if unidad == 'bit' and unidad_conv == 'GB':
            cant = float(cant) * math.pow(10, -9)

    return cant

print str(conversor(cant_info, unidad_info, unidad_info_conv)) + " " + unidad_info_conv




