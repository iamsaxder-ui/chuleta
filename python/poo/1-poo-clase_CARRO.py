class Carro:

    def __init__(self, marca, modelo, color):
    

        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.encendido = False
    
    def encender (self):
        self.encendido = True
        print ("el carro ha encendido")
        
        
    def apagar (self):
        self.encendido = False
    
    
    def acelerar (self):
        if self.encendido:
            print("el carro esta acelerando")
        else:
            print("el carro debe estar encendido para acelerar")    
    
    
    
mi_carro = Carro("toyota", "corolla", "blanco")
    

mi_carro.acelerar()
    