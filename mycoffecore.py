# Importación de librerías-----------------------------------------------------------------------------------v
import os   #Se importó esta librería para poder ocuparla después con la función de limpiar terminal




# Función para limpiar la terminal---------------------------------------------------------------------------v
def limpiarterminal():          #Función para limpiar cada vez que cambias entre pantallas/apartados
    os.system('cls' if os.name == 'nt' else 'clear') #Es cls para que funcione en windows y clear para otros





# Imagen con caracteres--------------------------------------------------------------------------------------v
taza = """
          ( (
           ) )
        ........         ¡BIENVENIDO A
        |      |]                 MY COFFEE CORE!
        \\      / 
         `----'
    """           #Las decoraciones con simbolos se guardan en variables tipo string para "comprimirlas"
                  #y no poner tanto texto en cada print que se quiera hacer




# Variables globales de datos para almacenar productos y facturas--------------------------------------------v
productos = {} #Un diccionario que almacena los productos disponibles. 
               #Cada producto se almacena con su nombre como clave y un diccionario con los detalles (nombre
               # y precio) como valor

facturas = [] #Una lista que almacena las facturas generadas. Cada factura es un diccionario que incluye el 
              #ID de la factura, el nombre del cliente, los ítems (productos y cantidades), y el total

next_id_factura = 1 #Es Un contador que lleva la cuenta del próximo ID de factura a asignar. 
                    #Se incrementa cada vez que se crea una nueva factura


# Función para agregar un producto---------------------------------------------------------------------------v
def agregar_producto():  #Esta función permite al usuario agregar un nuevo producto al diccionario productos
                         #Solicita el nombre y el precio del producto, y valida que el precio sea un número 
                         #positivo. Luego, agrega el producto al diccionario y vuelve al menú principal
    limpiarterminal()
    print(taza)
    nombre = input("Ingresa el nombre del producto: ")
    while True:     #Se inicia un bucle, el cual hace que se repita el input hasta que el usuario
                    #ingrese un dato correcto (en este caso, un numero flotante mayor a 0)
        try:
            precio = float(input(f"Ingresa el precio del producto '{nombre}': "))
            if precio > 0:
                break
            else:
                print("El precio debe ser un número positivo.")
        except ValueError:
            print("Entrada no válida. Por favor, introduce un número válido.")

    productos[nombre] = {'nombre': nombre, 'precio': precio}
    print(f"Producto agregado: {productos[nombre]['nombre']} - ${productos[nombre]['precio']:.2f}")
    menu()

# Función para mostrar los productos--------------------------------------------------------------------------v
def mostrar_productos():    #Esta función muestra todos los productos almacenados en el diccionario "productos"
                            #Si no hay productos, informa al usuario. Después de mostrar los productos, 
                            #espera a que el usuario presione Enter para volver al menú principal
    limpiarterminal()
    print(taza)
    if productos:
        print("\nProductos disponibles:")
        for producto in productos.values():
            print(f"{producto['nombre']} - ${producto['precio']:.2f}")
    else:
        print("No hay productos disponibles.")
    input("\nPresiona Enter para continuar...")
    menu()

# Función para crear una factura-----------------------------------------------------------------------------v
def crear_factura():    #Esta función crea una nueva factura. Solicita el nombre del cliente y crea un nuevo 
                        #diccionario para la factura con un ID único (utilizando next_id_factura), el nombre 
                        #del cliente, una lista de items vacia y un total de 0.0. La nueva factura se agrega 
                        #a la lista facturas, y se incrementa next_id_factura

    global next_id_factura
    limpiarterminal()
    print(taza)
    cliente = input("Ingrese el nombre del cliente: ")
    nueva_factura = {'id_factura': next_id_factura, 'cliente': cliente, 'items': [], 'total': 0.0}
    facturas.append(nueva_factura)
    next_id_factura += 1
    print(f"Factura creada con ID: {nueva_factura['id_factura']}")
    menu()

# Función para agregar un producto a una factura-------------------------------------------------------------v
def agregar_producto_a_factura(): #Esta función permite al usuario agregar un producto existente a una factura
                                  #específica. Primero, busca la factura utilizando su ID. Si la factura existe
                                  #permite al usuario agregar un producto por su nombre y la cantidad deseada, 
                                  #actualizando la lista de ítems y el total de la factura

    limpiarterminal()
    print(taza)
    id_factura = int(input("ID de la factura: "))
    factura = buscar_factura(id_factura)
    if factura:
        while True:
            nombre_producto = input("Nombre del producto: ")
            if nombre_producto in productos:
                while True:             #Igualmente, se ocupa la misma dinamica de poner un ciclo hasta
                                        #que el usuario introduzca un dato correcto
                    try:
                        cantidad = int(input("Cantidad: "))
                        if cantidad > 0:
                            break
                        else:
                            print("La cantidad debe ser un número entero positivo.")
                    except ValueError:
                        print("Entrada no válida. Por favor, introduce un número entero positivo.")
                producto = productos[nombre_producto]
                factura['items'].append((producto, cantidad))
                factura['total'] += producto['precio'] * cantidad
                print(f"Producto {nombre_producto} agregado a la factura {id_factura}")
                break
            else:
                print(f"Producto {nombre_producto} no encontrado. Por favor, introduce un producto existente.")
    else:
        print(f"Factura ID {id_factura} no encontrada.")
    menu()

# Función para buscar una factura----------------------------------------------------------------------------v
def buscar_factura(id_factura): #Esta función busca una factura en la lista facturas por su ID
                                #Si encuentra la factura, la devuelve, de lo contrario, devuelve otro resultado
    for factura in facturas:
        if factura['id_factura'] == id_factura:
            return factura
    return None

# Función para mostrar las facturas--------------------------------------------------------------------------v
def mostrar_facturas(): #Esta función muestra todas las facturas generadas almacenadas en la lista facturas
                        #Para cada factura, muestra el ID, el nombre del cliente, los ítems y el total. 
                        #Si no hay facturas, informa al usuario.
                        
    limpiarterminal()
    print(taza)
    if facturas:
        print("\nFacturas generadas:")
        for factura in facturas:
            print(f"\nFactura ID: {factura['id_factura']} - Cliente: {factura['cliente']}")
            print("Items:")
            for item, cantidad in factura['items']:
                print(f"{item['nombre']} x{cantidad} - ${item['precio'] * cantidad:.2f}")
            print(f"Total: ${factura['total']:.2f}\n")
    else:
        print("No hay facturas generadas.")
    input("\nPresiona Enter para continuar...")
    menu()

# Función para salir del programa----------------------------------------------------------------------------v
def salir(): #Esta función es para salir del programa (no es la gran cosa, pero se ve bien)
    limpiarterminal()
    print("Saliendo del programa...")
    exit() #Aquí ocupamos una función por defecto, la cual cierra el archivo y te devuelve al directorio

# Función principal del menú---------------------------------------------------------------------------------v
def menu(): #Esta función es para que el usuario pueda navegar en el programa, es la parte principal del mismo
            #ya que aquí puedes escoger que hacer (cada opción te lleva a una pantalla distinta con su función)

    while True: #Misma dinamica, se repite el ciclo para que el usuario introduzca bien su elección
                #(el ciclo en este caso no termina, ya que se interrumpe al ejecutar una función dentro de las
                #elecciones)
                
        limpiarterminal()
        print(taza)
        print("¿Qué desea hacer?\n1. Agregar producto\n2. Mostrar productos\n3. Crear factura\n4. Agregar producto a factura\n5. Mostrar facturas\n6. Salir")
        seleccion = input("\nSeleccione una opción: ")

        if seleccion == "1":
            agregar_producto()
        elif seleccion == "2":
            mostrar_productos()
        elif seleccion == "3":
            crear_factura()
        elif seleccion == "4":
            agregar_producto_a_factura()
        elif seleccion == "5":
            mostrar_facturas()
        elif seleccion == "6":
            salir()
        else:
            print("Selección inválida")
            input("\nPresiona Enter para continuar...")

# Bloque para ejecutar el programa---------------------------------------------------------------------------v
menu()
