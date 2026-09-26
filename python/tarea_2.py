# 1. Creamos la fábrica de juguetes (La Clase)
class Juguete:
    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

    # Una función para calcular cuánto cuestan estos juguetes juntitos
    def calcular_subtotal(self):
        return self.precio * self.cantidad


# 2. Creamos la fábrica del carrito de compras
class CarritoDeCompras:
    def __init__(self):
        self.items = [] # El carrito empieza vacío

    def agregar_juguete(self, juguete):
        self.items.append(juguete) # Metemos el objeto juguete al carrito

    def mostrar_ticket(self):
        total_a_pagar = 0
        print("\n--- TICKET DEL SUPERMERCADO DE BEBÉ ---")
        
        for juguete in self.items:
            subtotal = juguete.calcular_subtotal()
            total_a_pagar += subtotal
            print(f"- {juguete.cantidad}x {juguete.nombre} = ${subtotal}")
            
        print(f"\nTotal a pagar (pídeselo a mamá): ${total_a_pagar}")


# --- HORA DE JUGAR (AQUÍ CREAS TUS OBJETOS MANUALMENTE) ---

# 1. Compramos un carrito vacío
mi_carrito = CarritoDeCompras()

# 2. Creamos los juguetes manualmente como si fueran soldaditos
juguete1 = Juguete("Sonajero de Dinosaurio", 10.50, 2)
juguete2 = Juguete("Chupete Mágico", 5.00, 1)
juguete3 = Juguete("Galletita de Avena", 2.50, 4)

# 3. Metemos los juguetes al carrito con ruedas
mi_carrito.agregar_juguete(juguete1)
mi_carrito.agregar_juguete(juguete2)
mi_carrito.agregar_juguete(juguete3)

# 4. Imprimimos el resultado final
mi_carrito.mostrar_ticket()