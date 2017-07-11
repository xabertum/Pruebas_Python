# -*- coding: utf-8 -*-

lados = input('Introduce el numero de lados : ')
long_lado = input('Introduce su longitud : ')
apotema = input('¿Cual es su apotema?')


def calcularArea():
    area = (lados * long_lado * apotema) / 2

    return area


def calcularPerimetro():
    perim = lados * long_lado

    return perim


def tipoPoligono(num_lados):
    return {
        3: 'triangulo',
        4: 'cuadrilatero',
        5: 'pentagno',
        6: 'hexagono',
        7: 'Heptagono',
        8: 'Octagono',
        9: 'Eneagono',
        10: 'Decagono',
        11: 'Undecagono',
        12: 'Dodecagono'
    }.get(num_lados,'demasidados lados')


print 'El area es: ' + str(calcularArea())
print 'El perimetro es ' + str(calcularPerimetro())
print 'Tu poligono se llama: ' + str(tipoPoligono(lados))
