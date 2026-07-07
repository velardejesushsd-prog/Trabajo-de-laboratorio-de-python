from utils import limpiar_pantalla, pausar
import productos as prod
from datetime import datetime   # ← Para la fecha

def realizar_venta(productos):
    carrito = {}   # código -> cantidad
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
        print("No se agregaron productos.")
        pausar()
        return
    
    # Aplicar promoción simple (10% si total > 5000)
    descuento = 0
    if total > 5000:
        descuento = total * 0.10
        total_final = total - descuento
        print("\n¡Promoción aplicada! 10% de descuento por compras mayores a $5000")
    else:
        total_final = total
    
    # Mostrar ticket mejorado
    limpiar_pantalla()
    print("="*70)
    print("              TICKET DE VENTA - SUPERMERCADO")
    print("="*70)
    print(f"Fecha y Hora: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")
    print("-" * 70)
    print(f"{'Producto':<30} {'Cant':<6} {'Precio':<10} {'Subtotal':<12}")
    print("-" * 70)
    
    for codigo, cantidad in carrito.items():
        p = productos[codigo]
        subtotal = cantidad * p['precio']
        print(f"{p['nombre']:<30} {cantidad:<6} ${p['precio']:<9.2f} ${subtotal:<12.2f}")
    
    print("-" * 70)
    print(f"{'Subtotal:':<50} ${total:.2f}")
    if descuento > 0:
        print(f"{'Descuento (10%):':<50} -${descuento:.2f}")
    print(f"{'TOTAL A PAGAR:':<50} ${total_final:.2f}")
    print("="*70)
    
    # Actualizar stock
    for codigo, cantidad in carrito.items():
        productos[codigo]['stock'] -= cantidad
    
    prod.guardar_productos(productos)
    print("\nVenta realizada y stock actualizado.")
    pausar()