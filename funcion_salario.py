# -*- coding: utf-8 -*-

horas = int(input('Cuantas horas has trabajado esta semana : '))
precio = int(input('Cual era el precio? : '))


def calcularSalario(h, p):
    if h > 40:
        salario = h * (p * 1.5)
    else:
        salario = h * p

    return salario


print(calcularSalario(horas, precio))
