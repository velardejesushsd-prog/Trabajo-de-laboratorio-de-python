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
        print(f"Guardado correctamente en: {ruta}")
    except Exception as e:
        print(f"Error al guardar: {e}")


def agregar_producto(productos):
    cod = input("Ingrese código del producto (ej: P001): ").strip().upper()
    if cod in productos:
        print("Error: Ya existe un producto con ese código.")
        return
    
    nombre = input("Ingrese nombre del producto: ").strip()
    if not nombre or nombre.isdigit():   # ← Validación mejorada
        print("Error: El nombre no puede estar vacío ni ser solo números.")
        return
    
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


def modificar_producto(productos):
    cod = input("Ingrese código del producto a modificar: ").strip().upper()
    if cod not in productos:
        print("Producto no encontrado.")
        return
    
    p = productos[cod]
    print(f"Producto actual: {p['nombre']} - ${p['precio']} - Stock: {p['stock']}")
    
    nombre = input("Nuevo nombre (Enter para mantener): ").strip()
    if nombre:
        p['nombre'] = nombre
    
    try:
        precio_str = input("Nuevo precio (Enter para mantener): ").strip()
        if precio_str:
            precio = float(precio_str)
            if precio > 0:
                p['precio'] = precio
    except ValueError:
        print("Precio inválido, se mantiene el anterior.")
    
    try:
        stock_str = input("Nuevo stock (Enter para mantener): ").strip()
        if stock_str:
            stock = int(stock_str)
            if stock >= 0:
                p['stock'] = stock
    except ValueError:
        print("Stock inválido, se mantiene el anterior.")
    
    guardar_productos(productos)
    print("Producto modificado correctamente.")


def eliminar_producto(productos):
    cod = input("Ingrese código del producto a eliminar: ").strip().upper()
    if cod not in productos:
        print("Producto no encontrado.")
        return
    
    confirmar = input(f"¿Eliminar {productos[cod]['nombre']}? (S/N): ").strip().upper()
    if confirmar == "S":
        del productos[cod]
        guardar_productos(productos)
        print("Producto eliminado correctamente.")
    else:
        print("Eliminación cancelada.")