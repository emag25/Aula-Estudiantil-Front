
n=600

objetos = [
    (1, '2022-09-15', '2022-2023 CII')
]

while n < 610:
    n += 1
    objetos.append((n, '2022-05-15', '2022-2023 CI'))


# Imprimir los objetos actualizados
for objeto in objetos:
    print(objeto, ',')
