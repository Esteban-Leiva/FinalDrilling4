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

class Particular(Automovil):
    def __init__(self, marca, modelo, nroRuedas, velocidad, cilindraje, nroPuesto):
        super().__init__(marca,modelo,nroRuedas,velocidad,cilindraje)
        self.nroPuesto = nroPuesto
    
    #Se agrega un getter
    def get_nroPuesto(self):
        return self.nroPuesto
    #se agrega un setter
    def set_nroPuesto(self, nuevo):
        self.nroPuesto = nuevo

    def __str__(self):
        return super().__str__() + f", Numero de Puestos: {self.nroPuesto}"
    
class Carga(Automovil):
    def __init__(self, marca, modelo, nroRuedas, velocidad, cilindraje, pesoCarga):
        super().__init__(marca,modelo,nroRuedas,velocidad,cilindraje)
        self.pesoCarga = pesoCarga

    #Se agrega un getter
    def get_pesoCarga(self):
        return self.pesoCarga
    #se agrega un setter
    def set_pesoCarga(self, nuevo):
        self.pesoCarga = nuevo
    
    def __str__(self):
        return super().__str__() + f", Peso de Carga: {self.pesoCarga}Kg"
    
class Bicicleta(Vehiculo):
    def __init__(self, marca, modelo, nroRuedas, tipo):
        super().__init__(marca, modelo, nroRuedas)
        self.tipo = tipo

    #Se agrega un getter
    def get_tipo(self):
        return self.tipo
    #se agrega un setter
    def set_tipo(self, nuevo):
        self.tipo = nuevo
    
    def __str__(self):
        return super().__str__() + f", Tipo: {self.tipo}"

class Motocicleta(Bicicleta):
    def __init__(self, marca,modelo,nroRuedas,tipo, motor, cuadro, nroRadios):
        super().__init__(marca, modelo, nroRuedas, tipo)
        self.nroRadios = nroRadios
        self.cuadro = cuadro
        self.motor = motor
    
    #Se agrega un getter nroRadios
    def get_nroRadios(self):
        return self.nroRadios
    #se agrega un setter nroRadios
    def set_nroRadios(self, nuevo):
        self.nroRadios = nuevo

    #Se agrega un getter cuadro
    def get_cuadro(self):
        return self.cuadro
    #se agrega un setter cuadro
    def set_cuadro(self, nuevo):
        self.cuadro = nuevo

    #Se agrega un getter motor
    def get_motor(self):
        return self.motor
    #se agrega un setter motor
    def set_motor(self, nuevo):
        self.motor = nuevo


    def __str__(self):
        return super().__str__() + f", Motor: {self.motor}, Cuadro: {self.cuadro}, Nro Radios: {self.nroRadios}"