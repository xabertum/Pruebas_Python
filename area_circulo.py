# -*- coding: utf-8 -*-
import math

def pedirRadio():
	radio = int(raw_input('Introduce el radio: '))
	return radio

def calcularArea():
	area = pedirRadio() ** math.pi
	print 'El area del circulo es: ' + str(area)

calcularArea()


