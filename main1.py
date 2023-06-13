from clases1 import Vehiculo, Automovil

autos = []

n = int(input("Cuantos autos desea insertar: "))

for index, i in enumerate(range(n)):
    print (f"Datos del automovil {index+1}")
    marca = input("Ingrese la marca del automovil: ")
    modelo = input("Ingrese el modelo: ")
    nroRuedas = int(input("Ingrese el numero de ruedas:  "))
    velocidad = int(input("Ingrese su velocidad en km/h: "))
    cilindrada = int(input("Ingrese el cilindraje en cc: "))
    auto = Automovil(marca, modelo, nroRuedas, velocidad, cilindrada)
    autos.append(auto)

print("------------------------------------------------")
print("Los autos gurdados son: ")
for index, auto in enumerate(autos):
    print(f"Datos del vehiculo {index+1}: {auto}")