from clases3 import Vehiculo, Automovil, Particular, Carga, Motocicleta, Bicicleta


particular = Particular("Ford", "Fiesta", 4, "180", "500", 5)
particular.guardar_datos_csv()

carga = Carga("Daft Trucks", "G 38", 10, 120, "1000", "20000")
carga.guardar_datos_csv()

bicicleta = Bicicleta("Shimano", "MT Ranger", 2, "Carrera")
bicicleta.guardar_datos_csv()

motocicleta = Motocicleta("BMW", "F800s",2,"Deportiva","2T","Doble Viga", 21)
motocicleta.guardar_datos_csv()

automovil = Automovil("Renault", "Clio", 4, 160, 1600)
automovil.guardar_datos_csv()

particular2 = Particular("Mercedez Benz", "a200", 4, "240", "2000", 5)
particular2.guardar_datos_csv()

particular.leer_datos_csv()
carga.leer_datos_csv()
bicicleta.leer_datos_csv()
motocicleta.leer_datos_csv()
automovil.leer_datos_csv()
