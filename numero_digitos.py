import math

num = int(raw_input('Introduce el numero por favor: '))


def intCount (n):
    if n > 0:
        digits = int(math.log10(n)) + 1
    elif n == 0:
        digits = 1
    else:
        digits = int(math.log10(-n)) + 1
    print digits

intCount(num)
