class Vehiculo():
    def __init__(self, marca, modelo, nroRuedas):
        self.marca = marca
        self.modelo = modelo
        self.nroRuedas = nroRuedas
    
    def __str__(self):
        return (f"Marca {self.marca}, Modelo {self.modelo}, {self.nroRuedas} ruedas")

class Automovil(Vehiculo):
    def __init__(self, marca, modelo, nroRuedas, velocidad, cilindraje):
        super().__init__(marca, modelo, nroRuedas)
        self.velocidad = velocidad
        self.cilindrada = cilindraje
    
    def __str__(self):
        return super().__str__() + f" {self.velocidad} Km/h, {self.cilindrada}cc motor"
        