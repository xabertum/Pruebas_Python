# -*- coding: utf-8 -*-

def saludar(nombre, mensaje):
    print (nombre, mensaje)


def preguntarEdad():
    edad = int(input('Introduce tu edad...:'))
    if (edad > 35):
        print ('Enhorabuena!')
   
    return edad


def calcularFecha():
    date = 2017 - preguntarEdad()
    print('Tu fecha de nacimiento es: ' + str(date))


def quiereSeguirJugando():
    respuesta = input('Quiere seguir jugando: ')
    if (respuesta == 's'):
        calcularFecha()
    else:
        print ('Gracias!')


saludar('Javier', 'Bienvenido a ti mismo')
calcularFecha()
quiereSeguirJugando()
