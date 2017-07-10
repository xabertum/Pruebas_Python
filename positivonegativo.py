# -*- coding: utf-8 -*-

esPositivo = True

num = int(raw_input('Introduce el numero:'))

if num < 0:
    esPositivo = False

print 'el numero es positivo: ' + str(esPositivo)


