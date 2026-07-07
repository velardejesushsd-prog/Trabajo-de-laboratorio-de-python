from utils import limpiar_pantalla, pausar
import productos as prod
import ventas as vent
import estadisticas as stats

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
            productos = menu_productos(productos)
        elif opcion == "2":
            vent.realizar_venta(productos)
        elif opcion == "3":
            stats.mostrar_estadisticas(productos)
        elif opcion == "4":
            print("¡Gracias por usar el sistema!")
            break
        else:
            print("Opción inválida.")
            pausar()

def menu_productos(productos):
    while True:
        productos = prod.cargar_productos()
        
        limpiar_pantalla()
        print("--- GESTIÓN DE PRODUCTOS ---")
        print("1. Agregar Producto")
        print("2. Listar Productos")
        print("3. Modificar Producto")
        print("4. Eliminar Producto")
        print("5. Volver al menú principal")
        
        op = input("Opción: ")
        
        if op == "1":
            prod.agregar_producto(productos)
        elif op == "2":
            prod.listar_productos(productos)
        elif op == "3":
            prod.modificar_producto(productos)
        elif op == "4":
            prod.eliminar_producto(productos)
        elif op == "5":
            break
        else:
            print("Opción inválida.")
        
        pausar()
    
    return productos

if __name__ == "__main__":
    menu_principal()