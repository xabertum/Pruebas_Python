# -*- coding: utf-8 -*-
import math

def pedirRadio():
    radio = int(raw_input('Introduce el radio: '))
    return radio


def calcularArea():
    radio = pedirRadio()
    area = round (math.pow(radio, 2) * math.pi ,2)
    print 'El area del circulo es: ' + str(area)

    circun = 2 * math.pi * radio
    print 'La circunferencia es: ' + str(circun)


calcularArea()


