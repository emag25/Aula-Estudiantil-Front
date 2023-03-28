import unicodedata

datos = [

    (51, 'Andre Long', 'Vineall Casaccia'),
    (52, 'Lemuel Nadege', 'Son Ahlf'),
    (53, 'Chelsey Marylene', 'Bradforth Haville'),
    (54, 'Valaria Meline', 'Ucchino McHenry'),
    (55, 'Olivero Maeline', 'Garbar MacAlpyne'),
    (56, 'Bobette Lea', 'Thackham Greve'),
    (57, 'Donelle Esteve', 'Tschierasche Dymott'),
    (58, 'Dav Adelie', 'Swedeland Westerman'),
    (59, 'Jeffrey Ma', 'Iskow Sargent'),
    (60, 'Dulsea Meline', 'Cyseley Willows'),
    (61, 'Gabey Gwenaelle', 'Howlett Tabourier'),
    (62, 'Kerrin Serena', 'MacCartan Soutar'),
    (63, 'Archibald Maella', 'Fateley Orme')

]

print(len(datos))
# Función para eliminar los acentos y símbolos de las vocales
def eliminar_acentos(cadena):
    return ''.join((c for c in unicodedata.normalize('NFD', cadena) if unicodedata.category(c) != 'Mn'))


for i in range(len(datos)):
    datos[i] = datos[i][:1] + (eliminar_acentos(datos[i][3]),) + datos[i][6:]
    

for objeto in datos:
    print(objeto, ',')
