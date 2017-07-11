# -*- coding: utf-8 -*-

lados = input('Introduce el numero de lados : ')
long_lado = input('Introduce su longitud : ')
apotema = input('¿Cual es su apotema?')
tipo_poligono = ""


def calcularArea():
    area = (lados * long_lado * apotema) / 2

    return area


def calcularPerimetro():
    perim = lados * long_lado

    return perim


def tipoPoligono(num_lados):
    pass



