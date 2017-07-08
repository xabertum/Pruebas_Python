def saludar(nombre, mensaje):
    print nombre, mensaje

saludar('Javier', 'Hola');


def preguntarEdad():
    edad = raw_input('Introduce tu edad...:')
    if (edad > 35):
        print 'Enhorabuena!';

preguntarEdad()
