import os

def cargar_productos():
    productos = {}
    ruta = "data/productos.txt"
    
    try:
        with open(ruta, "r", encoding="utf-8") as f:
            for linea in f:
                if linea.strip():
                    cod, nombre, precio, stock = linea.strip().split(";")
                    productos[cod] = {
                        "nombre": nombre,
                        "precio": float(precio),
                        "stock": int(stock)
                    }
    except FileNotFoundError:
        pass
    return productos


def guardar_productos(productos):
    if not os.path.exists("data"):
        os.makedirs("data")
        print("Carpeta 'data' creada.")
    
    ruta = "data/productos.txt"
    try:
        with open(ruta, "w", encoding="utf-8") as f:
            for cod, data in productos.items():
                f.write(f"{cod};{data['nombre']};{data['precio']};{data['stock']}\n")
        print(f"Guardado correctamente en: {ruta}")   # ← Mensaje de debug
    except Exception as e:
        print(f"Error al guardar: {e}")

def agregar_producto(productos):
    cod = input("Ingrese código del producto (ej: P001): ").strip().upper()
    if cod in productos:
        print("Error: Ya existe un producto con ese código.")
        return
    
    nombre = input("Ingrese nombre del producto: ").strip()
    try:
        precio = float(input("Ingrese precio: "))
        stock = int(input("Ingrese stock inicial: "))
        if precio <= 0 or stock < 0:
            print("Error: Precio y stock deben ser positivos.")
            return
    except ValueError:
        print("Error: Ingrese valores numéricos válidos.")
        return
    
    productos[cod] = {"nombre": nombre, "precio": precio, "stock": stock}
    guardar_productos(productos)
    print(f"Producto {cod} agregado correctamente.")


def listar_productos(productos):
    if not productos:
        print("No hay productos registrados.")
        return
    
    print("\n--- LISTADO DE PRODUCTOS ---")
    print(f"{'Código':<8} {'Nombre':<25} {'Precio':<10} {'Stock':<8}")
    print("-" * 60)
    for cod, data in productos.items():
        print(f"{cod:<8} {data['nombre']:<25} ${data['precio']:<9.2f} {data['stock']:<8}")