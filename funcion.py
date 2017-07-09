# -*- coding: utf-8 -*-

def saludar(nombre, mensaje):
    print nombre, mensaje


def preguntarEdad():
    edad = int(raw_input('Introduce tu edad...:'))
    if (edad > 35):
<<<<<<< HEAD
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
=======
        print 'Enhorabuena!'
    return edad;


def calcularAnio():
    date = 2017 - int(preguntarEdad())
    print 'Tu año de nacimiento fue el: ' + str(date)

calcularAnio()

probando...
>>>>>>> cbff3022cc156423abae39c80047f83e1281a5fa
