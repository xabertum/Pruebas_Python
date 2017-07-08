# -*- coding: utf-8 -*-

def saludar(nombre, mensaje):
    print nombre, mensaje

saludar('Javier', 'Hola');


def preguntarEdad():
    edad = raw_input('Introduce tu edad...:')
    if (edad > 35):
        print 'Enhorabuena!'
    return edad;


def calcularAnio():
    date = 2017 - int(preguntarEdad())
    print 'Tu año de nacimiento fue el: ' + str(date)

calcularAnio()

probando...
