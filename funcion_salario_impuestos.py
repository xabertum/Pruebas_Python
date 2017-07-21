# -*- coding: utf-8 -*-

horas = int(input('Cuantas horas has trabajado esta semana : '))
precio = int(input('Cual era el precio? : '))


def calcularSalario(h, p):
    if h > 40:
        if h == 45:
            salario = h - 40 * (p * 1.5)
        if h > 45:
            salario = h - 40 * (p * 2)
    else:
        salario = h * p

    return salario


def impuestos():
    if salario < 1000:
        impuesto = salario * 0.1
    else:
        impuesto = salario * 0.15

    return impuesto


salario = calcularSalario(horas, precio)

print('El salario antes de impuestos: ' + str(salario))
print('El salario despues de impuestos' + str(salario - impuestos()))
