# -*- coding: utf-8 -*-

esPositivo = True


def pedirNumero():
    num = int(raw_input('Introduce el numero:'))

    if num < 0:
        esPositivo = False


def toPrint():
    print 'el numero es positivo: ' + str(esPositivo)


pedirNumero()
toPrint()
