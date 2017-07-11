# -*- coding: utf-8 -*-


user_presion_atm = input('Introduzca el nivel de presion atmosferica (0,1,2): ')
user_humedad_realativa = input('Introduzca el nivel de humadad relativa (0,1,2,): ')


def probabilidad_lluvia():
    if user_presion_atm == 2:
        if user_humedad_realativa == 0:
            print('>>>> Probabilidad de lluvia MUY ALTA <<<<')
        if user_humedad_realativa == 1:
            print('>>>> Probabilidad de lluvia ALTA <<<<')
        if user_humedad_realativa == 2:
            print('>>>> Probabilidad de lluvia MEDIA <<<<')

    elif user_presion_atm == 1 and user_humedad_realativa == 1:
        print('>>>> Probabilidad de lluvia MEDIA <<<<')

    else:
        print('>>>> Probabilidad de lluvia BAJA <<<<')



def probabilidad_sol():
    if user_presion_atm == 2:
        if user_humedad_realativa == 0:
            print('>>>> Probabilidad de sol BAJA <<<<')
        if user_humedad_realativa == 1:
            print('>>>> Probabilidad de sol MEDIA <<<<')
        if user_humedad_realativa == 2:
            print('>>>> Probabilidad de sol MEDIA <<<<')

    elif user_presion_atm == 1 and user_humedad_realativa == 1:
        print('>>>> Probabilidad de sol MEDIA <<<<')

    else:
        print('>>>> Probabilidad de sol ALTA <<<<')


def probabilidad_frio():
    if user_presion_atm == 2:
        if user_humedad_realativa == 0:
            print('>>>> Probabilidad de frio ALTA <<<<')
        if user_humedad_realativa == 1:
            print('>>>> Probabilidad de frio ALTA <<<<')
        if user_humedad_realativa == 2:
            print('>>>> Probabilidad de frio ALTA <<<<')

    elif user_presion_atm == 1:
        if user_humedad_realativa == 0:
            print('>>>> Probabilidad de frio ALTA <<<<')
        if user_humedad_realativa == 1:
            print('>>>> Probabilidad de frio MEDIA <<<<')

    else:
        print('>>>> Probabilidad de lluvia BAJA <<<<')

probabilidad_lluvia()
probabilidad_sol()
probabilidad_frio()

