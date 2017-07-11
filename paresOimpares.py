# -*- coding: utf-8 -*-


def preguntarUsuario ():
    respuesta = input('Quieres ver los pares "p" o los impares "i" : ')

    return respuesta


if preguntarUsuario() == 'p':
    for i in range(0, 1001):
        if i % 2 == 0:
            print(i)

elif preguntarUsuario() == 'i':
    for i in range(0, 1001):
        if i % 3 == 0:
            print(i)

else:
    print('Gracias por participar... ')





