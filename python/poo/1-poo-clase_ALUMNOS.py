class Alumno:

    def __init__(self, nombre, edad, carrera, matematicas, fisica, quimica):
    

        self.nombre = nombre
        self.edad = edad
        self.carrera = carrera
        self.matematicas = matematicas
        self.fisica = fisica
        self.quimica = quimica
        self.graduado = False
    
    def se_gradua (self):
        self.graduado = True
        print ("el alumno ha graduado")
        
        
    def no_gradua (self):
        self.graduado = False
    
    
    def dar_promedio (self):
        if self.graduado is True:
            promedio = (self.matematicas + self.fisica + self.quimica) / 3
            print(f"el promedio de {self.nombre} es {promedio}")
        else:
            print("el alumno debe estar graduado para darle el promedio")    
    
    
    
mi_alumno = Alumno("pedro", 21, "medicina", 8.5, 3.5, 9.5)
    
mi_alumno.se_gradua()
mi_alumno.dar_promedio()
print(mi_alumno.matematicas)
print(mi_alumno.fisica)
print(mi_alumno.quimica)
print(mi_alumno.carrera)
    