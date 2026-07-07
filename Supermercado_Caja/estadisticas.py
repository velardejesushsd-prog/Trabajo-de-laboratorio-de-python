from utils import limpiar_pantalla, pausar

def mostrar_estadisticas(productos, ventas_historial=None):
    limpiar_pantalla()
    print("="*50)
    print("       ESTADÍSTICAS DEL SUPERMERCADO")
    print("="*50)
    
    # Total de productos
    print(f"Total de productos registrados: {len(productos)}")
    
    # Producto más caro
    if productos:
        mas_caro = max(productos.items(), key=lambda x: x[1]['precio'])
        print(f"Producto más caro: {mas_caro[1]['nombre']} (${mas_caro[1]['precio']})")
    
    # Stock bajo
    stock_bajo = [p for p in productos.values() if p['stock'] < 10]
    print(f"Productos con stock bajo (<10): {len(stock_bajo)}")
    
    print("\n--- Fin de estadísticas ---")
    pausar()