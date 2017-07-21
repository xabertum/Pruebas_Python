
cant_info = input('Introduce una cantidad de información')
unidad_info = input('¿ En que unidad esta expresada ?: ')




def convertir(cant, unidad):
    return {
        'bit': cant




    }.get(unidad, 'Unidad no reconocida')
