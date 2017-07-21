datos = []
suma = 0
media = 0

for i in range(0, 10 + 1):
    datos.append(raw_input('Introduce el numero: '))
    suma = suma + int(datos[i])



media = suma / 10
print suma, media

print datos