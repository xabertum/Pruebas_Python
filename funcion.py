# -*- coding: utf-8 -*-

def saludar(nombre, mensaje):
    print nombre, mensaje


def preguntarEdad():
    edad = int(raw_input('Introduce tu edad...:'))
    if (edad > 35):
        print 'Enhorabuena!';
   
    return edad


def calcularFecha():
    date = 2017 - preguntarEdad()
print('Tu fecha de nacimiento es: ' + str(date))


def quiereSeguirJugando():
    respuesta = raw_input('Quiere seguir jugando: ')
    if (respuesta == 's'):
        calcularFecha()


saludar('Javier', 'Bienvenido a ti mismo')
calcularFecha()
quiereSeguirJugando()
