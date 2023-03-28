import random


def asignar_nivel(edad):
    if edad < 17:
        return '1er nivel'
    elif edad < 23:
        return '2do nivel'
    else:
        return '3er nivel'


# Definir la lista de objetos
objetos = [

    (1, '2022-10-03', '2022-10-05', '.PDF', 'Tarea'),
    (1, '2022-10-05', '2022-10-10', '.PPT', 'Tarea'),
    (1, '2022-10-10', '2022-10-12', '.PDF', 'Tarea'),
    (1, '2022-10-12', '2022-10-17', '.PDF', 'Tarea'),
    (1, '2022-10-17', '2022-10-19', '.PPT', 'Tarea'),
    (1, '2022-10-19', '2022-10-24', '.JPG', 'Tarea'),
    (1, '2022-10-24', '2022-10-26', '.PDF', 'Tarea'),
    (1, '2022-10-26', '2022-10-31', '.PPT', 'Tarea'),
    (1, '2022-10-31', '2022-11-02', '.PDF', 'Tarea'),
    (1, '2022-11-02', '2022-11-04', '.TXT', 'Tarea')
]


fechas = [
    '2004-12-03', '2005-09-18', '2010-03-13', '2012-05-22', '2008-11-14', '2010-01-29', '2010-09-10', '2008-02-06', '1995-09-20', '2002-08-01', '2003-04-17', '1995-06-18', '2010-06-24', '2010-02-05', '1998-11-21', '2003-05-15', '2002-03-09', '1995-08-20', '2008-01-09', '2004-07-11', '1995-02-03', '2010-06-04', '1998-08-19', '2002-05-25', '2010-06-28', '2002-04-18', '2008-03-30', '2002-10-17', '2012-01-17', '2008-03-19', '2012-11-22', '2008-05-28', '2012-02-06', '2008-09-26', '2010-08-08', '2010-06-28', '2008-06-20', '2008-09-23', '2010-04-16', '2008-09-10', '2010-10-12', '2002-10-23', '2003-02-10', '2010-09-12', '2002-08-22', '2002-07-19', '2010-10-21', '2003-03-05', '2002-08-09', '2010-05-02'
]
edades = [
    18, 17, 12, 20, 15, 21, 12, 15, 28, 21, 20, 28, 12, 12, 25, 20, 21, 28, 15, 19, 28, 12, 25, 21, 12, 21, 15, 21, 12, 20, 15, 20, 15, 15, 12, 12, 15, 15, 12, 15, 12, 21, 20, 12, 21, 21, 12, 20, 21, 12
]

direcciones = [
    "Avenida Bolívar",
    "Calle Los Mangos",
    "Calle El Sol",
    "Avenida Libertador",
    "Avenida Universidad",
    "Calle El Empalme",
    "Calle El Progreso",
    "Avenida 5 de Julio",
    "Avenida Caracas",
    "Calle La Línea",
    "Calle Los Pinos",
    "Avenida Miranda",
    "Calle Santa Rosa",
    "Calle Los Jabillos",
    "Avenida Andrés Bello",
    "Calle El Tamarindo",
    "Calle El Progreso",
    "Avenida Intercomunal",
    "Calle La Salle",
    "Avenida Principal",
    "Calle La Victoria",
    "Avenida Las Américas",
    "Calle Las Flores",
    "Calle Los Cocos",
    "Avenida Libertad",
    "Calle Las Margaritas",
    "Calle Los Almendrones",
    "Avenida Los Jardines",
    "Calle El Encanto",
    "Calle Los Robles",
    "Avenida Los Samanes",
    "Calle El Cardón",
    "Avenida Francisco de Miranda",
    "Calle Las Acacias",
    "Avenida La Costa",
    "Calle Los Pinos",
    "Avenida Las Delicias",
    "Calle Los Naranjos",
    "Avenida Los Caobos",
    "Calle Los Abetos",
    "Avenida Los Mangos",
    "Calle La Guacamaya",
    "Avenida San Martín",
    "Calle Los Guayacanes",
    "Calle Los Aleros",
    "Avenida Los Aviadores",
    "Calle El Trébol",
    "Avenida Los Cedros",
    "Calle Los Abetos",
    "Calle Los Cerezos"
    ]

cedulas = [
    '0105420764', '2410192382', '2423720619', '0333715946', '0340723855', '0956704937', '2106783191', '1847913200', '2034678391', '1343426900', '1405836419', '1439841255', '1720872946', '1738609137', '2049026319', '0734715982', '0716312582', '0139682437', '2453689028', '0827139455', '2358032719', '0504862719', '0648719055', '1304062791', '1739742519', '1822130746', '1742471500', '1557956082', '2241803628', '2054352091', '2031079564', '2319571482', '1643912455', '0655867200', '1039217537', '1153697519', '1928347091', '0902507482', '1113724091', '0900386746', '2214071328', '1743168546', '1624015273', '1001427900', '0523862746', '1551348955', '0710536191', '0658906428', '0800675182', '1744130755'

]

telefonos = [
    '0954634692', '0996694481', '0960690838', '0981226522', '0991585607', '0970249268', '0951618246', '0998812451', '0973968160', '0989711774', '0912779883', '0989860799', '0937257696', '0944084827', '0968249309', '0972620361', '0981566510', '0975892745', '0965210817', '0944663387', '0965190446', '0911216567', '0950116487', '0987093761', '0990807687', '0955248096', '0952178176', '0930132478', '0999461835', '0935510724', '0982558414', '0962666541', '0974811606', '0923613357', '0990076648', '0958693188', '0934186346', '0916742488', '0945880587', '0923562027', '0920775881', '0920190675', '0965254977', '0966435421', '0945852614', '0958049637', '0924716743', '0977394672', '0940031112', '0916452341'

]


print('----------------------------------------------------------------------------------')
print('----------------------------------------------------------------------------------')
print('datos', len(objetos))
print('cedulas', len(cedulas))
print('fechas', len(fechas))
print('edades', len(edades))
print('----------------------------------------------------------------------------------')
print('----------------------------------------------------------------------------------')


ultimo_registro = 593
for i in range(len(objetos)):
    objetos[i] = list(objetos[i])
    ultimo_registro += 1
    objetos[i][0] = ultimo_registro
    objetos[i].insert(3, cedulas[i])
    objetos[i].insert(4, fechas[i])
    objetos[i].insert(5, edades[i])
    objetos[i].insert(6, direcciones[i])
    objetos[i].insert(7, telefonos[i])
    objetos[i].insert(8, (objetos[i][1].split(' ')[0] + objetos[i][2].split(' ')
                      [0] + objetos[i][4].split('-')[2] + '@gmail.com').lower())
    objetos[i].insert(9, asignar_nivel(objetos[i][5]))
    objetos[i].insert(10, round(random.uniform(7.01*100, 9.99*100) / 100, 2))
    objetos[i].insert(11, random.randint(1, 5))
    objetos[i] = tuple(objetos[i])


# Imprimir los objetos actualizados
for objeto in objetos:
    print(objeto, ',')
