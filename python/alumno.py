CATALOGO = {
    1: {"nombre": "luis", "promedio": 35.00},
    2: {"nombre": "monica", "promedio": 18.50},
    3: {"nombre": "pedro", "promedio": 100.00},
    4: {"nombre": "areli", "promedio": 25.00}
}





def mostrar_catalogo():
    """Muestra la lista de productos y sus precios."""
    print("\n--- lista de alumnos ---")
    for codigo, item in CATALOGO.items():
        print(f"[{codigo}] {item['nombre']} - promedio: {item['promedio']:.2f}")
    print("-----------------------------")

def solicitar_datos_cliente():
    """Pide y retorna el nombre y cédula del comprador."""
    print("=== registro profesor ===")
    nombre = input("Ingrese el nombre : ").strip()
    cedula = input("Ingrese la cédula o ID: ").strip()
    return nombre, cedula



 
def main():
    nombre, cedula = solicitar_datos_cliente()
    carrito = []

    
    while True:
        mostrar_catalogo()
        opcion = input("\nSeleccione una opción: ").strip()
        
        if opcion == "0":
            print("Saliendo del programa...")
            break
            
        elif opcion == "1":
          
            try:
                nuevo_id = int(input("Ingrese el ID del nuevo alumno: "))
                
               
                if nuevo_id in CATALOGO:
                    print("Error")
                else:
                    nuevo_nombre = input("Ingrese el nombre: ").strip()
                    nuevo_promedio = float(input("Ingrese el promedio: "))
                    
                 
                    CATALOGO[nuevo_id] = {"nombre": nuevo_nombre, "promedio": nuevo_promedio}
                    print(f"Alumno {nuevo_nombre} agregado correctamente")
            except ValueError:
                print("❌ Error: El ID debe ser un número entero y el promedio un número (ej: 15.5).")
        
        else:
            print("❌ Opción no válida. Por favor, seleccione una opción del menú.")

# Punto de entrada de la aplicación
if __name__ == "__main__":
    main()