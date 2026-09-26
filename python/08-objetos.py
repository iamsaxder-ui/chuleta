class Alumno:
    def __init__(self,nombre): #constructor crea la funcion (metodo)
        self.nombre = nombre
        self.notas = []
    def agregar_notas(self,nota):
        self.notas.append(nota)
        print(f"nota {nota} agregada con exito a {self.nombre}")
    def obtener_promedio(self):
        if len(self.notas) == 0: #si numero de notas = 0 retorna 0
            return 0.0
        promedio = sum(self.notas)/len(self.notas) #las suma de las notas mas el numero de notas
        return promedio

alumno1= Alumno("jenny")
alumno1.agregar_notas(18)   
alumno1.agregar_notas(12)  
alumno1.agregar_notas(20)   
print(f"promedio de {alumno1.nombre}: {alumno1.obtener_promedio():2f}")
    