from utils import limpiar_pantalla, pausar
import productos as prod

def menu_principal():
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
            menu_productos()
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

def menu_productos():
    while True:
        limpiar_pantalla()
        print("--- GESTIÓN DE PRODUCTOS ---")
        print("1. Agregar Producto")
        print("2. Listar Productos")
        print("3. Volver al menú principal")
        
        op = input("Opción: ")
        if op == "1":
            # Aquí iremos agregando la lógica
            print("Función de agregar producto en desarrollo...")
        elif op == "2":
            print("Listado de productos en desarrollo...")
        elif op == "3":
            break
        else:
            print("Opción inválida")

if __name__ == "__main__":
    menu_principal()