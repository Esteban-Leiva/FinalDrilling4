from clases2 import Vehiculo, Automovil, Particular, Carga, Motocicleta, Bicicleta

autos = []

#PARTE 1 DRILLING FINAL 4
"""
n = int(input("Cuantos autos desea insertar: "))
print("Agregando vehículos (Parte 1)................. ")

for index, i in enumerate(range(n)):
    print (f"Datos del automovil {index+1}")
    marca = input("Ingrese la marca del automovil: ")
    modelo = input("Ingrese el modelo: ")
    nroRuedas = int(input("Ingrese el numero de ruedas:  "))
    velocidad = int(input("Ingrese su velocidad en km/h: "))
    cilindrada = int(input("Ingrese el cilindraje en cc: "))
    auto = Automovil(marca, modelo, nroRuedas, velocidad, cilindrada)
    autos.append(auto)
"""


#PARTE 2 DRILLING FINAL 4
particular = Particular("Ford", "Fiesta", 4, "180", "500", 5)
autos.append(particular)
carga = Carga("Daft Trucks", "G 38", 10, 120, "1000", "20000")
autos.append(carga)
bicicleta = Bicicleta("Shimano", "MT Ranger", 2, "Carrera")
autos.append(bicicleta)
motocicleta = Motocicleta("BMW", "F800s",2,"Deportiva","2T","Doble Viga", 21)
autos.append(motocicleta)


print("------------------------------------------------")
print("Los autos gurdados son: ")
for index, auto in enumerate(autos):
    print(f"Datos del vehiculo {index+1}: {auto}")

print("Verificando relaciones entre clase motocicleta y otros vehículos............")
print(f"Motocicleta es instancia con relación a Vehículo: {isinstance(motocicleta, Vehiculo)}")
print(f"Motocicleta es instancia con relación a Automovil: {isinstance(motocicleta, Automovil)}")
print(f"Motocicleta es instancia con relación a Vehículo particular: {isinstance(motocicleta, Particular)}")
print(f"Motocicleta es instancia con relación a Vehículo de carga: {isinstance(motocicleta, Carga)}")
print(f"Motocicleta es instancia con relación a Bicicleta: {isinstance(motocicleta, Bicicleta)}")
print(f"Motocicleta es instancia con relación a Motocicleta: {isinstance(motocicleta, Motocicleta)}")