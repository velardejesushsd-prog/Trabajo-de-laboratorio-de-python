from utils import limpiar_pantalla, pausar
import productos as prod

def menu_principal():
    # Cargamos los productos al iniciar el programa
    productos = prod.cargar_productos()
    
    while True:
        limpiar_pantalla()
        print("="*50)
        print("   SISTEMA DE CAJA - SUPERMERCADO")
        print("="*50)
        print("1. Gestión de Productos")
        print("2. Realizar Venta")
        print("3. Estadísticas")
        print("4. Salir")
        print("="*50)
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            productos = menu_productos(productos)   # Actualizamos los productos
        elif opcion == "2":
            print("Módulo de ventas (en desarrollo...)")
            pausar()
        elif opcion == "3":
            print("Estadísticas (en desarrollo...)")
            pausar()
        elif opcion == "4":
            print("¡Gracias por usar el sistema!")
            break
        else:
            print("Opción inválida.")
            pausar()

def menu_productos(productos):
    while True:
        # Recargamos los productos cada vez que entramos al menú
        productos = prod.cargar_productos()
        
        limpiar_pantalla()
        print("--- GESTIÓN DE PRODUCTOS ---")
        print("1. Agregar Producto")
        print("2. Listar Productos")
        print("3. Volver al menú principal")
        
        op = input("Opción: ")
        
        if op == "1":
            prod.agregar_producto(productos)
        elif op == "2":
            prod.listar_productos(productos)
        elif op == "3":
            break
        else:
            print("Opción inválida.")
        
        pausar()
    
    return productos  # Devolvemos el diccionario actualizado

if __name__ == "__main__":
    menu_principal()