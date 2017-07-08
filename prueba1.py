def pedirNombre():
    name = raw_input('Introduce el nombre: ')
    return name


def imprimirNombre(nombre):
    print 'el nombre introducido es... ' + nombre


imprimirNombre(pedirNombre())