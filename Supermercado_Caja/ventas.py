from utils import limpiar_pantalla, pausar
import productos as prod

def realizar_venta(productos):
    carrito = {}   
    total = 0.0
    
    while True:
        limpiar_pantalla()
        print("--- REALIZAR VENTA ---")
        print("Código del producto (0 para finalizar): ")
        codigo = input().strip().upper()
        
        if codigo == "0":
            break
        
        if codigo not in productos:
            print("Producto no encontrado.")
            pausar()
            continue
        
        try:
            cantidad = int(input(f"Cantidad de {productos[codigo]['nombre']}: "))
            if cantidad <= 0:
                print("Cantidad debe ser mayor a 0.")
                pausar()
                continue
            if cantidad > productos[codigo]['stock']:
                print("Stock insuficiente.")
                pausar()
                continue
        except ValueError:
            print("Ingrese un número válido.")
            pausar()
            continue
        
        
        if codigo in carrito:
            carrito[codigo] += cantidad
        else:
            carrito[codigo] = cantidad
        
        subtotal = cantidad * productos[codigo]['precio']
        total += subtotal
        print(f"Agregado: {cantidad} x {productos[codigo]['nombre']} = ${subtotal:.2f}")
        pausar()
    
    if not carrito:
        print("No se agregaron productos a la venta.")
        pausar()
        return
    
    # Mostrar ticket
    limpiar_pantalla()
    print("="*60)
    print("              TICKET DE VENTA")
    print("="*60)
    print(f"{'Producto':<25} {'Cant':<6} {'Precio':<10} {'Subtotal':<10}")
    print("-" * 60)
    
    for codigo, cantidad in carrito.items():
        p = productos[codigo]
        subtotal = cantidad * p['precio']
        print(f"{p['nombre']:<25} {cantidad:<6} ${p['precio']:<9.2f} ${subtotal:<9.2f}")
    
    print("-" * 60)
    print(f"{'TOTAL A PAGAR:':<42} ${total:.2f}")
    print("="*60)
    
    # Actualizar stock
    for codigo, cantidad in carrito.items():
        productos[codigo]['stock'] -= cantidad
    
    prod.guardar_productos(productos)
    print("\nVenta realizada y stock actualizado.")
    pausar()