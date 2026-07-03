def cargar_productos ():
    productos = {}
    try:
        with open('data/productos.txt', 'r ' ) as f:
            for linea in f:
                if linea.strip():
                    cod, nombre, precio, stock = linea.strip().split(';')
                    productos[cod] = {
                        'nombre' : nombre,
                        'precio' : float(precio),
                        'stock'  : int(stock)
                    }

    except FileNotFoundError:
        pass
    return productos
                    




def guardar_productos(productos):
    with open('data/productos.txt', 'w') as f:
        for cod, data in productos.items():
            f.write(f'{cod}; {data['nombre']}; data[{'precio'}]; data [{'stock'}]\n')
