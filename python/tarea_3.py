class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

class Cliente:
    def __init__(self, nombre, cedula):
        self.nombre = nombre
        self.cedula = cedula

class CarritoDeCompras:
    def __init__(self, cliente, tasa_iva=0.16):
        self.cliente = cliente
        self.articulos = []
        self.tasa_iva = tasa_iva

    def agregar_producto(self, producto, cantidad=1):
        self.articulos.append({"producto": producto, "cantidad": cantidad})

    def calcular_subtotal(self):
        subtotal = 0
        for articulo in self.articulos:
            subtotal += articulo["producto"].precio * articulo["cantidad"]
        return subtotal

    def calcular_iva(self):
        return self.calcular_subtotal() * self.tasa_iva

    def calcular_total(self):
        return self.calcular_subtotal() + self.calcular_iva()

    def generar_factura(self):
        print("\n" + "="*30)
        print("      FACTURA DE COMPRA")
        print("="*30)
        print(f"Cliente: {self.cliente.nombre}")
        print(f"Cédula:  {self.cliente.cedula}")
        print("-" * 30)
        
        for art in self.articulos:
            prod = art["producto"]
            cant = art["cantidad"]
            total_prod = prod.precio * cant
            print(f"{prod.nombre} (x{cant}) - ${total_prod:.2f}")
            
        print("-" * 30)
        print(f"Subtotal: ${self.calcular_subtotal():.2f}")
        print(f"IVA ({(self.tasa_iva * 100):.0f}%): ${self.calcular_iva():.2f}")
        print(f"TOTAL:    ${self.calcular_total():.2f}")
        print("="*30 + "\n")

def main():
    # 1. Definir el catálogo de productos disponibles
    catalogo = [
        Producto("Laptop", 850.00),
        Producto("Mouse Inalámbrico", 25.00),
        Producto("Teclado Mecánico", 60.00),
        Producto("Monitor 24 pulgadas", 150.00)
    ]

    print("Bienvenido al sistema de ventas")
    
    # 2. Solicitar datos del cliente
    nombre = input("Ingrese su nombre: ")
    cedula = input("Ingrese su cédula: ")
    cliente_actual = Cliente(nombre, cedula)

    # Inicializar el carrito (puedes ajustar la tasa de IVA aquí, ej: 0.16 para 16%)
    carrito = CarritoDeCompras(cliente_actual, tasa_iva=0.16)

    # 3. Bucle principal de compras
    while True:
        print("\n--- CATÁLOGO DE PRODUCTOS ---")
        for i, prod in enumerate(catalogo):
            print(f"{i + 1}. {prod.nombre} - ${prod.precio:.2f}")
        print("0. Finalizar compra y pagar")

        opcion = input("\nSeleccione el número del producto (o 0 para salir): ")

        if opcion == "0":
            break
        
        try:
            indice = int(opcion) - 1
            if 0 <= indice < len(catalogo):
                producto_seleccionado = catalogo[indice]
                cantidad = int(input(f"¿Cuántas unidades de '{producto_seleccionado.nombre}' desea?: "))
                
                if cantidad > 0:
                    carrito.agregar_producto(producto_seleccionado, cantidad)
                    print(f"✅ {cantidad}x {producto_seleccionado.nombre} agregado(s) al carrito.")
                else:
                    print("❌ La cantidad debe ser mayor a cero.")
            else:
                print("❌ Opción inválida. Seleccione un número del catálogo.")
        except ValueError:
            print("❌ Por favor, ingrese un número válido.")

    # 4. Procesar el pago y mostrar la factura
    if carrito.articulos:
        carrito.generar_factura()
    else:
        print("\nNo se agregaron productos. Compra cancelada.")

if __name__ == "__main__":
    main()