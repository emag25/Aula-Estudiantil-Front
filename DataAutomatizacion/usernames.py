
datos = [
    (669, 'Julietta Leandre', 'Danit Housby', '0825812073', '2010-06-24', 12,
     'Avenida 6 de Agosto', '0949940337', 'juliettadanit24@gmail.com', '1er nivel', 9.86, 3),
   	(670, 'Philly Maelle', 'Andino Latus', '1452184900', '2010-02-05', 12,
   	 'Avenida América', '0917263493', 'phillyandino05@gmail.com', '1er nivel', 7.73, 5),
   	(671, 'Doralynn Josephine', 'Bantock Olek', '1346759146', '1998-11-21', 25,
   	 'Avenida Arce', '0955192632', 'doralynnbantock21@gmail.com', '3er nivel', 7.79, 1),
   	(672, 'Chelsy Solene', 'Iannazzi Bury', '2204603873', '2003-05-15', 20,
   	 'Avenida Ballivián', '0937252226', 'chelsyiannazzi15@gmail.com', '2do nivel', 9.85, 3),
   	(673, 'Ginnie Berangere', 'Okie Tassell', '0458967046', '2002-03-09', 21,
   	 'Avenida Busch', '0996776923', 'ginnieokie09@gmail.com', '2do nivel', 9.93, 2),
   	(674, 'Douglass Ines', 'Cazin Sheardown', '0414852037', '1995-08-20', 28,
   	 'Avenida Camacho', '0932257727', 'douglasscazin20@gmail.com', '3er nivel', 9.11, 5),
   	(675, 'Timmi Maella', 'Rainey Butten', '2032169700', '2008-01-09', 15,
   	 'Avenida Cristóbal de Mendoza', '0981060699', 'timmirainey09@gmail.com', '1er nivel', 8.01, 5),
   	(676, 'Tedie Beatrice', 'Mansford McBlain', '0928254037', '2004-07-11', 19,
   	 'Avenida del Ejército', '0980655332', 'tediemansford11@gmail.com', '2do nivel', 8.3, 2),
   	(677, 'Michele Marie-eve', 'Toth Nuccii', '1944328091', '1995-02-03', 28,
   	 'Avenida Heroínas', '0975108223', 'micheletoth03@gmail.com', '3er nivel', 7.28, 2),
   	(678, 'Rudie Stevina', 'Feldon Dibley', '0900579828', '2010-06-04', 12,
   	 'Avenida Hernando Siles', '0919801452', 'rudiefeldon04@gmail.com', '1er nivel', 7.95, 5)

]

CREDENCIALES = []

print(len(datos))
for dato in datos:
    username = dato[1].split()[0].lower() + "_" + dato[2].split()[0].lower() + dato[4][-2:]
    credenciales_obj = (username, '12345678', 1)
    CREDENCIALES.append(credenciales_obj)


for objeto in CREDENCIALES:
    print(objeto,',')