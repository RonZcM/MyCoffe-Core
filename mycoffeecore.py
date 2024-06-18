# Librerías--------------------------------------------------------------------------------------------------------------v
import os
import json
from datetime import datetime

# Función para limpiar la terminal---------------------------------------------------------------------------------------v
def limpiarterminal():
    os.system('cls' if os.name == 'nt' else 'clear')

# Imagenes con caracteres------------------------------------------------------------------------------------------------v
pantalla_principal = """
                                                                                                                .                   ▒▒▒▒▒▒▒▒
                                                                                                                .                 ▒▒▒      ▒▒▒
                                                                                                                .               ▒▒   ▒▒▒▒   ▒░▒
                                                                                                                .              ▒▒   ▒▒  ▒▒   ▒░▒                   
                                                                                                                .             ▒▒░▒      ▒▒   ▒░▒
                                                                                                                .              ▒▒░▒    ▒▒   ▒░▒
                                                                                                                .                ▒▒▒▒▒▒▒   ▒▒
                                                                                                                .                        ▒▒▒
                                                                                                                .         ▒▒▒▒       ▒▒                   
                                                                                                                .       ▒▒▒░░▒▒▒     ▒▒  ▓▓▓▓▓▓▓▓                   
                                                                                                                .     ▒▒     ▒▒▒    ▒▒▓▓▓▓▓░░░░░▓▓  ▓▓▓▓
                ▒█▀▀█ ░▀░ █▀▀ █▀▀▄ ▀█░█▀ █▀▀ █▀▀▄ ░▀░ █▀▀▄ █▀▀█      █▀▀█                                       .    ▒   ▒▒    ▒▒ ▓▓▒░░░░░░░░░█▓▒▓▓▓▓░░▓▓▓
                ▒█▀▀▄ ▀█▀ █▀▀ █░░█ ░█▄█░ █▀▀ █░░█ ▀█▀ █░░█ █░░█      █▄▄█                                       .  ▒▒  ▒ ▒▒   ▓▒▒░░▒░░░░░████▓▓▒▒▓░░░░░░▓▓
                ▒█▄▄█ ▀▀▀ ▀▀▀ ▀░░▀ ░░▀░░ ▀▀▀ ▀░░▀ ▀▀▀ ▀▀▀░ ▀▀▀▀      ▀░░▀                                       .  ░▒▒   ▒  ▓▓▓░▒░░░░░█████▓▓▒▒▒▒▓▓▓▓▓░░▓▓
                                                                                                                .    ▒▒▒▒  ▓▓░░░░░░███████▓▓▓▒▒▒▒▒▓   ▓▓░▓▓
                                                                                                                .         ▓▓░░░░░░███████▓▓▓▒▒▒▒▒▒▒▓   ▓░░▓▓
        ███╗░░░███╗██╗░░░██╗  ░█████╗░░█████╗░███████╗███████╗███████╗███████╗░█████╗░░█████╗░██████╗░███████╗  .        ▓▓░░░░░███████▓▓▓▒▒▒▒▒▒▒▒▒▓▓▓▓░░▓▓
        ████╗░████║╚██╗░██╔╝  ██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔════╝  .       ▓▓░░░░██████▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▓░░░░▓▓
        ██╔████╔██║░╚████╔╝░  ██║░░╚═╝██║░░██║█████╗░░█████╗░░█████╗░░█████╗░░██║░░╚═╝██║░░██║██████╔╝█████╗░░  .       ▓▓▓░████▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓
        ██║╚██╔╝██║░░╚██╔╝░░  ██║░░██╗██║░░██║██╔══╝░░██╔══╝░░██╔══╝░░██╔══╝░░██║░░██╗██║░░██║██╔══██╗██╔══╝░░  .        ▓▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓
        ██║░╚═╝░██║░░░██║░░░  ╚█████╔╝╚█████╔╝██║░░░░░██║░░░░░███████╗███████╗╚█████╔╝╚█████╔╝██║░░██║███████╗  .        ▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓
        ╚═╝░░░░░╚═╝░░░╚═╝░░░  ░╚════╝░░╚════╝░╚═╝░░░░░╚═╝░░░░░╚══════╝╚══════╝░╚════╝░░╚════╝░╚═╝░░╚═╝╚══════╝  .         ▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓
                                                                                                                .           ▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓
                                                                                                                .             ▓▓▓▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓
                                                                                                                .               ▓▓▓▓▓▓▒▒▒▒▒▓▓▓▓
                                                                                                                .                   ▓▓▓▓▓▓▓▓
.   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .
"""

pantalla_productos="""
                                                                                                                .                   ▒▒▒▒▒▒▒▒
        ███╗░░░███╗██╗░░░██╗  ░█████╗░░█████╗░███████╗███████╗███████╗███████╗░█████╗░░█████╗░██████╗░███████╗  .                 ▒▒▒      ▒▒▒
        ████╗░████║╚██╗░██╔╝  ██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔════╝  .               ▒▒   ▒▒▒▒   ▒░▒
        ██╔████╔██║░╚████╔╝░  ██║░░╚═╝██║░░██║█████╗░░█████╗░░█████╗░░█████╗░░██║░░╚═╝██║░░██║██████╔╝█████╗░░  .              ▒▒   ▒▒  ▒▒   ▒░▒
        ██║╚██╔╝██║░░╚██╔╝░░  ██║░░██╗██║░░██║██╔══╝░░██╔══╝░░██╔══╝░░██╔══╝░░██║░░██╗██║░░██║██╔══██╗██╔══╝░░  .             ▒▒░▒      ▒▒   ▒░▒
        ██║░╚═╝░██║░░░██║░░░  ╚█████╔╝╚█████╔╝██║░░░░░██║░░░░░███████╗███████╗╚█████╔╝╚█████╔╝██║░░██║███████╗  .              ▒▒░▒    ▒▒   ▒░▒
        ╚═╝░░░░░╚═╝░░░╚═╝░░░  ░╚════╝░░╚════╝░╚═╝░░░░░╚═╝░░░░░╚══════╝╚══════╝░╚════╝░░╚════╝░╚═╝░░╚═╝╚══════╝  .                ▒▒▒▒▒▒▒   ▒▒
                                                                                                                .                        ▒▒▒
                                                                                                                .         ▒▒▒▒       ▒▒
                                                                                                                .       ▒▒▒░░▒▒▒     ▒▒  ▓▓▓▓▓▓▓▓
                                                                                                                .     ▒▒     ▒▒▒    ▒▒▓▓▓▓▓░░░░░▓▓  ▓▓▓▓
                                                                                                                .    ▒   ▒▒    ▒▒ ▓▓▒░░░░░░░░░█▓▒▓▓▓▓░░▓▓▓
                                                                                                                .  ▒▒  ▒ ▒▒   ▓▒▒░░▒░░░░░████▓▓▒▒▓░░░░░░▓▓
        ▒█▀▄▀█ █▀▀█ █▀▀▄ █▀▀ ░░▀ █▀▀█    █▀▀▄ █▀▀    ▒█▀▀█ █▀▀█ █▀▀█ █▀▀▄ █░░█ █▀▀ ▀▀█▀▀ █▀▀█ █▀▀               .  ░▒▒   ▒  ▓▓▓░▒░░░░░█████▓▓▒▒▒▒▓▓▓▓▓░░▓▓
        ▒█▒█▒█ █▄▄█ █░░█ █▀▀ ░░█ █░░█    █░░█ █▀▀    ▒█▄▄█ █▄▄▀ █░░█ █░░█ █░░█ █░░ ░░█░░ █░░█ ▀▀█               .    ▒▒▒▒  ▓▓░░░░░░███████▓▓▓▒▒▒▒▒▓   ▓▓░▓▓
        ▒█░░▒█ ▀░░▀ ▀░░▀ ▀▀▀ █▄█ ▀▀▀▀    ▀▀▀░ ▀▀▀    ▒█░░░ ▀░▀▀ ▀▀▀▀ ▀▀▀░ ░▀▀▀ ▀▀▀ ░░▀░░ ▀▀▀▀ ▀▀▀               .         ▓▓░░░░░░███████▓▓▓▒▒▒▒▒▒▒▓   ▓░░▓▓
                                                                                                                .        ▓▓░░░░░███████▓▓▓▒▒▒▒▒▒▒▒▒▓▓▓▓░░▓▓
                                                                                                                .       ▓▓░░░░██████▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▓░░░░▓▓
                                                                                                                .       ▓▓▓░████▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓
                                                                                                                .        ▓▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓
                                                                                                                .        ▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓
                                                                                                                .         ▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓
                                                                                                                .           ▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓
                                                                                                                .             ▓▓▓▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓
                                                                                                                .               ▓▓▓▓▓▓▒▒▒▒▒▓▓▓▓
                                                                                                                .                   ▓▓▓▓▓▓▓▓
.   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .
"""
pantalla_facturas="""
                                                                                                                .                   ▒▒▒▒▒▒▒▒
        ███╗░░░███╗██╗░░░██╗  ░█████╗░░█████╗░███████╗███████╗███████╗███████╗░█████╗░░█████╗░██████╗░███████╗  .                 ▒▒▒      ▒▒▒
        ████╗░████║╚██╗░██╔╝  ██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔════╝  .               ▒▒   ▒▒▒▒   ▒░▒
        ██╔████╔██║░╚████╔╝░  ██║░░╚═╝██║░░██║█████╗░░█████╗░░█████╗░░█████╗░░██║░░╚═╝██║░░██║██████╔╝█████╗░░  .              ▒▒   ▒▒  ▒▒   ▒░▒
        ██║╚██╔╝██║░░╚██╔╝░░  ██║░░██╗██║░░██║██╔══╝░░██╔══╝░░██╔══╝░░██╔══╝░░██║░░██╗██║░░██║██╔══██╗██╔══╝░░  .             ▒▒░▒      ▒▒   ▒░▒
        ██║░╚═╝░██║░░░██║░░░  ╚█████╔╝╚█████╔╝██║░░░░░██║░░░░░███████╗███████╗╚█████╔╝╚█████╔╝██║░░██║███████╗  .              ▒▒░▒    ▒▒   ▒░▒
        ╚═╝░░░░░╚═╝░░░╚═╝░░░  ░╚════╝░░╚════╝░╚═╝░░░░░╚═╝░░░░░╚══════╝╚══════╝░╚════╝░░╚════╝░╚═╝░░╚═╝╚══════╝  .                ▒▒▒▒▒▒▒   ▒▒
                                                                                                                .                        ▒▒▒
                                                                                                                .         ▒▒▒▒       ▒▒
                                                                                                                .       ▒▒▒░░▒▒▒     ▒▒  ▓▓▓▓▓▓▓▓
                                                                                                                .     ▒▒     ▒▒▒    ▒▒▓▓▓▓▓░░░░░▓▓  ▓▓▓▓
                                                                                                                .    ▒   ▒▒    ▒▒ ▓▓▒░░░░░░░░░█▓▒▓▓▓▓░░▓▓▓
                                                                                                                .  ▒▒  ▒ ▒▒   ▓▒▒░░▒░░░░░████▓▓▒▒▓░░░░░░▓▓
        ▒█▀▄▀█ █▀▀█ █▀▀▄ █▀▀ ░░▀ █▀▀█    █▀▀▄ █▀▀    █▀▀ █▀▀█ █▀▀ ▀▀█▀▀ █░░█ █▀▀█ █▀▀█ █▀▀                      .  ░▒▒   ▒  ▓▓▓░▒░░░░░█████▓▓▒▒▒▒▓▓▓▓▓░░▓▓
        ▒█▒█▒█ █▄▄█ █░░█ █▀▀ ░░█ █░░█    █░░█ █▀▀    █▀▀ █▄▄█ █░░ ░░█░░ █░░█ █▄▄▀ █▄▄█ ▀▀█                      .    ▒▒▒▒  ▓▓░░░░░░███████▓▓▓▒▒▒▒▒▓   ▓▓░▓▓
        ▒█░░▒█ ▀░░▀ ▀░░▀ ▀▀▀ █▄█ ▀▀▀▀    ▀▀▀░ ▀▀▀    ▀░░ ▀░░▀ ▀▀▀ ░░▀░░ ░▀▀▀ ▀░▀▀ ▀░░▀ ▀▀▀                      .         ▓▓░░░░░░███████▓▓▓▒▒▒▒▒▒▒▓   ▓░░▓▓
                                                                                                                .        ▓▓░░░░░███████▓▓▓▒▒▒▒▒▒▒▒▒▓▓▓▓░░▓▓
                                                                                                                .       ▓▓░░░░██████▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▓░░░░▓▓
                                                                                                                .       ▓▓▓░████▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓
                                                                                                                .        ▓▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓
                                                                                                                .        ▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓
                                                                                                                .         ▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓
                                                                                                                .           ▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓
                                                                                                                .             ▓▓▓▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓
                                                                                                                .               ▓▓▓▓▓▓▒▒▒▒▒▓▓▓▓
                                                                                                                .                   ▓▓▓▓▓▓▓▓
.   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .
"""

# Variables globales de datos para almacenar productos y facturas--------------------------------------------------------v
productos = {}
facturas = []
next_id_factura = 1

# Función para guardar productos en un archivo JSON----------------------------------------------------------------------v
def guardar_productos():
    with open('productos.json', 'w') as file:
        json.dump(productos, file)
    print("       <<Productos guardados exitosamente>>")

# Función para cargar productos desde un archivo JSON--------------------------------------------------------------------v
def cargar_productos():
    global productos
    if os.path.exists('productos.json'):
        with open('productos.json', 'r') as file:
            productos = json.load(file)
        print("       <<Productos cargados exitosamente>>")
    else:
        productos = {}

# Función para guardar facturas en un archivo JSON-----------------------------------------------------------------------v
def guardar_facturas():
    with open('facturas.json', 'w') as file:
        json.dump(facturas, file)
    print("       <<Facturas guardadas exitosamente>>")

# Función para cargar facturas desde un archivo JSON---------------------------------------------------------------------v
def cargar_facturas():
    global facturas, next_id_factura
    if os.path.exists('facturas.json'):
        with open('facturas.json', 'r') as file:
            facturas = json.load(file)
        if facturas:
            next_id_factura = max(factura['id_factura'] for factura in facturas) + 1
        else:
            next_id_factura = 1
        print("       <<Facturas cargadas exitosamente.>>")
    else:
        facturas = []
        next_id_factura = 1

# Función para agregar un producto---------------------------------------------------------------------------------------v
def agregar_producto():
    while True:
        limpiarterminal()
        print(pantalla_productos)
        nombre = input("       Ingresa el nombre del producto: ")
        while True:
            try:
                precio = float(input(f"       Ingresa el precio del producto '{nombre}': "))
                if precio > 0:
                    break
                else:
                    print("       El precio debe ser un número positivo.")
            except ValueError:
                print("       Entrada no válida. Por favor, introduce un número válido.")

        productos[nombre] = {'nombre': nombre, 'precio': precio}
        print(f"\n       Producto agregado: {productos[nombre]['nombre']} - ${productos[nombre]['precio']:.2f}")
        print("\n")
        guardar_productos()

        continuar = input("       ¿Deseas agregar otro producto? (s/n): ").strip().lower()
        if continuar != 's':
            break

    menu()

# Función para mostrar los productos-------------------------------------------------------------------------------------v
def mostrar_productos():
    limpiarterminal()
    print(pantalla_productos)
    if productos:
        print("\n       Productos disponibles:\n")
        for producto in productos.values():
            print(f"       {producto['nombre']} - ${producto['precio']:.2f}")
    else:
        print("       No hay productos disponibles.")
    input("\n       Presiona Enter para continuar...")
    menu()

# Función para eliminar un producto-------------------------------------------------------------------------------------v
def eliminar_producto():
    limpiarterminal()
    print(pantalla_productos)
    if productos:
        print("\n       Productos disponibles para eliminar:")
        for producto in productos.values():
            print(f"       {producto['nombre']} - ${producto['precio']:.2f}")
        nombre = input("\n       Ingresa el nombre del producto que deseas eliminar: ")
        if nombre in productos:
            del productos[nombre]
            print(f"\n       Producto '{nombre}' eliminado exitosamente.")
            print("\n")
            guardar_productos()  
        else:
            print(f"       Producto '{nombre}' no encontrado.")
    else:
        print("       No hay productos disponibles.")
    input("\n       Presiona Enter para continuar...")
    menu()

# Función para crear una factura-----------------------------------------------------------------------------------------v
def crear_factura():
    global next_id_factura
    limpiarterminal()
    print(pantalla_facturas)
    cliente = input("       Ingrese el nombre del cliente: ")
    fecha = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    nueva_factura = {'id_factura': next_id_factura,'fecha' : fecha, 'cliente': cliente, 'items': [], 'total': 0.0}
    facturas.append(nueva_factura)
    next_id_factura += 1
    print(f"       Factura creada con ID: {nueva_factura['id_factura']}")
    print("\n")
    guardar_facturas()  
    input("\n       Presiona Enter para continuar...")
    menu()

# Función para agregar un producto a una factura-------------------------------------------------------------------------v
def agregar_producto_a_factura():
    while True:
        limpiarterminal()
        print(pantalla_facturas)
        try:
            id_factura = int(input("       ID de la factura: "))
            break
        except ValueError:
            print("       Entrada no válida. Por favor, introduce un número válido.")
            input("\n       Presiona Enter para continuar...")

    factura = buscar_factura(id_factura)
    if factura:
        if productos:
            while True:
                limpiarterminal()
                print(pantalla_facturas)
                print(f"       ID de la factura: {id_factura}")
                nombre_producto = input("       Nombre del producto: ")
                if nombre_producto in productos:
                    while True:
                        try:
                            limpiarterminal()
                            print(pantalla_facturas)
                            print(f"       ID de la factura: {id_factura}")
                            print(f"       Nombre del producto: {nombre_producto}")
                            cantidad = int(input("       Cantidad: "))
                            if cantidad > 0:
                                break
                            else:
                                print("       La cantidad debe ser un número entero positivo.")
                                input("\n       Presiona Enter para continuar...")

                        except ValueError:
                            print("       Entrada no válida. Por favor, introduce un número entero positivo.")
                            input("\n       Presiona Enter para continuar...")
                    
                    producto = productos[nombre_producto]
                    factura['items'].append((producto, cantidad))
                    factura['total'] += producto['precio'] * cantidad
                    print(f"       Producto {nombre_producto} agregado a la factura {id_factura}")
                    print("\n")
                    guardar_facturas()  

                    # Preguntar al usuario si desea agregar otro producto
                    continuar = input("       ¿Deseas agregar otro producto? (s/n): ").strip().lower()
                    if continuar != 's':
                        break
                else:
                    print(f"       Producto {nombre_producto} no encontrado. Por favor, introduce un producto existente.")
                    input("\n       Presiona Enter para continuar...")
        else:
            print("       No hay productos registrados.")
            input("\n       Presiona Enter para continuar...")
            menu()
    else:
        print(f"       Factura ID {id_factura} no encontrada.")
        input("\n       Presiona Enter para continuar...")
    menu()

# Función para buscar una factura----------------------------------------------------------------------------------------v
def buscar_factura(id_factura):
    for factura in facturas:
        if factura['id_factura'] == id_factura:
            return factura
    return None

# Función para mostrar las facturas--------------------------------------------------------------------------------------v
def mostrar_facturas():
    limpiarterminal()
    print(pantalla_facturas)
    if facturas:
        print("\n       Facturas generadas:")
        for factura in facturas:
            print(f"\n       Factura ID: {factura['id_factura']} - Cliente: {factura['cliente']}")
            print(f"       Fecha: {factura['fecha']}")
            print("       ------------------------------------")
            print("       Items:\n")
            for item, cantidad in factura['items']:
                print(f"       {item['nombre']} x{cantidad} - ${item['precio'] * cantidad:.2f}")
            print("       ------------------------------------")
            print(f"       Total: ${factura['total']:.2f}\n")
    else:
        print("       No hay facturas generadas.")
    input("\n       Presiona Enter para continuar...")
    menu()

# Función para salir del programa----------------------------------------------------------------------------------------v
def salir():
    limpiarterminal()
    print("       Saliendo del programa...")
    exit()

# Función para eliminar una factura--------------------------------------------------------------------------------------v
def eliminar_factura():
    limpiarterminal()
    print(pantalla_facturas)
    if facturas:
        while True:
            try:
                id_factura = int(input("       ID de la factura que deseas eliminar: "))
                break
            except ValueError:
                print("       Entrada no válida. Por favor, introduce un número válido.")
                input("\n       Presiona Enter para continuar...")
                menu()

        factura = buscar_factura(id_factura)
        if factura:
            facturas.remove(factura)
            print(f"       Factura ID {id_factura} eliminada exitosamente.")
            guardar_facturas() 
        else:
            print(f"       Factura ID {id_factura} no encontrada.")
        input("\n       Presiona Enter para continuar...")
        menu()
    else:
        print("       No hay facturas generadas.")
        input("\n       Presiona Enter para continuar...")
        menu()

# Función para mostrar una factura----------------------------------------------------------------------------------------v
def mostrar_factura():
    limpiarterminal()
    print(pantalla_facturas)
    if facturas:
        while True:
            try:
                id_factura = int(input("       ID de la factura que deseas mostrar: "))
                break
            except ValueError:
                print("       Entrada no válida. Por favor, introduce un número válido.")
                input("\n       Presiona Enter para continuar...")
                menu()

        factura = buscar_factura(id_factura)
        if factura:
            limpiarterminal()
            print(pantalla_facturas)
            print(f"       Factura ID {id_factura} - Cliente: {factura['cliente']}")
            print(f"       Fecha: {factura['fecha']}")
            print("       ------------------------------------")
            print("\n       Items:\n")
            for item, cantidad in factura['items']:
                print(f"       {item['nombre']} x{cantidad} - ${item['precio'] * cantidad:.2f}")
            print("       ------------------------------------")
            print(f"        Total: ${factura['total']:.2f}\n")
            input("\n       Presiona Enter para continuar...")
        else:
            print(f"       Factura ID {id_factura} no encontrada.")
            input("\n       Presiona Enter para continuar...")
            menu()
    else:
        print("       No hay facturas generadas.")
        input("\n       Presiona Enter para continuar...")
        menu()

# Función principal del menú----------------------------------------------------------------------------------------------v
def menu():
    limpiarterminal()
    while True:
        limpiarterminal()
        print(pantalla_principal)
        print("                                                         ¿Qué desea hacer?")
        print("\n       1. Agregar producto        2. Mostrar productos        3. Eliminar producto        4. Crear factura        5. Agregar producto a factura       \n       6. Mostrar facturas        7. Mostrar Factura         8. Eliminar Factura           9. Salir")
        seleccion = input("\n       Seleccione una opción: ")

        match seleccion:
            case "1":
                agregar_producto()
            case "2":
                mostrar_productos()
            case "3":
                eliminar_producto()
            case "4":
                crear_factura()
            case "5":
                agregar_producto_a_factura()
            case "6":
                mostrar_facturas()
            case "7":
                mostrar_factura()
            case "8":
                eliminar_factura()
            case "9":
                salir()
            case _:
                print("       Selección inválida")
                input("\n       Presiona Enter para continuar...")

# Bloque para ejecutar el programa---------------------------------------------------------------------------------------v
limpiarterminal()
print(pantalla_principal)
cargar_productos() #Carga el archivo json que guarda el diccionario de productos con los valores
cargar_facturas() #Carga el archivo json que guarda las facturas con los diccionarios de factura
input("\n       Presione ENTER para continuar...")
menu() #Ejecuta el programa, comenzando con el menú
