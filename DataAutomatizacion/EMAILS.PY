

data = [
    (95, 'Camila Alejandra', 'Tirado Sarmiento', '2231643973', '2001-03-22', 21,
     'Calle Oe3 y la 19', '0997816928', 'Camila Tirado22@gmail.com', '2do nivel', 9.4, 2),
   	(96, 'Javier Andres', 'Guzman Benavides', '1511829646', '1999-12-05', 23,
   	 'Calle Bolivar y la 6ta', '0910355897', 'Javier Guzman05@gmail.com', '3er nivel', 9.8, 3),
   	(97, 'Gabriela Andrea', 'Chavez Ayala', '2226572191', '2003-10-20', 19,
   	 'Calle Oriente y la 10ma', '0910197138', 'Gabriela Chavez20@gmail.com', '2do nivel', 8.5, 1),
   	(98, 'Juan Diego', 'Paredes Cevallos', '0755804164', '2005-06-03', 16,
   	 'Calle Loja y la 13', '0964361367', 'Juan Paredes03@gmail.com', '1er nivel', 7.9, 5),
   	(99, 'Karla Daniela', 'Mora Barrera', '1113954100', '2001-12-22', 21,
   	 'Calle Santa Cruz y la 20', '0912558600', 'Karla Mora22@gmail.com', '2do nivel', 9.2, 2),
   	(100, 'Luis Alberto', 'Salazar Cevallos', '1034196537', '2004-05-11', 18,
   	 'Calle San Gabriel y la 21', '0954148848', 'Luis Salazar11@gmail.com', '2do nivel', 8.7, 3),
   	(101, 'Johana Paola', 'Gutierrez Arroyo', '0414512682', '2002-09-01', 20,
   	 'Calle Los Rios y la 22', '0977255348', 'Johana Gutierrez01@gmail.com', '2do nivel', 9.5, 2),
   	(102, 'Andrea Nicole', 'Gallardo Molina', '0519251046', '2003-03-04', 18,
   	 'Calle Sucre y la 12', '0963304313', 'Andrea Gallardo04@gmail.com', '2do nivel', 7.8, 5),
   	(103, 'Mateo Esteban', 'Sandoval Torres', '2342435691', '1999-08-13', 23,
   	 'Calle Loja y la 16', '0975009253', 'Mateo Sandoval13@gmail.com', '3er nivel', 9.6, 4),
   	(104, 'Santiago Alberto', 'Vasquez Morales', '0215179428', '2004-11-28', 18,
   	 'Calle San Francisco y la 10', '0940630002', 'Santiago Vasquez28@gmail.com', '2do nivel', 8.9, 2),
   	(105, 'Carla Margarita', 'Moreira Ortega', '0218051464', '2001-06-02', 21,
   	 'Av. de las Américas y 6 de Diciembre', '0925291533', 'Carla Moreira02@gmail.com', '2do nivel', 9.7, 2),
   	(106, 'Luisa Fernanda', 'García Pérez', '2010716346', '1998-11-22', 24,
   	 'Calle Guayaquil y Rocafuerte', '0972277453', 'Luisa García22@gmail.com', '3er nivel', 9.3, 3)
]


print(len(data))
updated_data = []
for obj in data :
    email = obj[8].lower()
    # Eliminamos los espacios en blanco del valor de email
    email = email.replace(" ", "")
    # Creamos una tupla con los datos actualizados y la agregamos a la lista updated_data
    updated_obj = (obj[0], obj[1], obj[2], obj[3], obj[4], obj[5],
                obj[6], obj[7], email, obj[9], obj[10], obj[11])
    updated_data.append(updated_obj)
    


# imprimir los datos
for d in updated_data:
    print(d,',')