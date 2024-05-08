# Desafío 1.
# Escribir un programa que simule una serie de pases en un partido de hockey entre Argentina y Australia.

# Importamos random para generar números aleatorios y os validar existencia de archivos y su eliminación
import random
import os

# Matriz de equipos con sus respectivas jugadoras - Cada elemento del array es un equipo
# equipos["Argentina"] = Argentina - Cada elemento del array es una tupla con el nombre de la jugadora y su número
# equipos["Australia"] = Australia - Cada elemento del array es una tupla con el nombre de la jugadora y su número

equipos = {
    "Argentina":[
        ("Luciana Aymar", 8),
        ("Delfina Merino", 19),
        ("Carla Rebecchi", 32),
        ("Agustina Albertario", 15),
        ("Florencia Habif", 6),
        ("Noel Barrionuevo", 12),
        ("Sofía Toccalino", 2),
        ("Victoria Sauze", 24),
        ("Eugenia Trinchinetti", 17),
        ("Julieta Jankunas", 23)
    ],
    "Australia":[
        ("Jodie Kenny", 32),
        ("Emily Chalker", 23),
        ("Madison Fitzpatrick", 3),
        ("Brooke Peris", 4),
        ("Savannah Fitzpatrick", 19),
        ("Karri McMahon", 21),
        ("Ambrosia Malone", 11),
        ("Jocelyn Bartram", 1),
        ("Gabrielle Nance", 10),
        ("Madi Ratcliffe", 14)
    ],
}

# Función de validación de existencia del archivo o su creación
def crear_archivo():
    if not os.path.exists('./pases.txt'):
        open('./pases.txt', 'x').close()
        print("Archivo de pases creado correctamente\n")
    else:
        print("\nEl archivo de pases ya existe\n")

    # Mostramos el menu para Seleccionar una nueva opción o salir
    mostrar_menu(2)

# La eliminación del archivo verifica su existencia y lo elimina
def eliminar_archivo():
    if os.path.exists('./pases.txt'):
        os.remove('./pases.txt')
        print("Archivo de pases eliminado correctamente")
    else:
        print("El archivo de pases no existe")
        
    # Mostramos el menu para Seleccionar una nueva opción o salir
    mostrar_menu(2)

# Lee, recorre e imprime todas las líneas del archivo de pases
# pases_desde_hasta por defeto es False, es una variable enviada desde la función leer_pases_especificos
# en caso de seleccionarse un rango de pases a leer. Por defecto es False, haciendo que se lean todos los pases
def leer_pases (pases_desde_hasta = False):
    archivo_de_pases = os.path.exists('./pases.txt')
    # En el caso de no existir el archivo, le indicamos al usuario
    if not archivo_de_pases:
        print("\nNo se encontró el archivo de pases\n")
    else:
        archivo_de_pases = open('./pases.txt', 'r')
        pases = archivo_de_pases.readlines()
        
        # En el caso de que no haya pases en el archivo, se lo indicamos al usuario
        if len(pases) == 0:
            print("No hay pases para mostrar\n")
            
        # Y acá tenemos el caso de seleccion de Leer todos los pases
        if not pases_desde_hasta:
            print("Leyendo archivo de pases...\n")
        else:
            # En caso de haber un rango de pases a leer, segmentamos el array de pases en los indicados
            print("\nLeyendo pases desde el ", pases_desde_hasta[0], " hasta el ",  pases_desde_hasta[1], "...\n")
            # pases_desde_hasta es una dupla indicando desde qué pase hasta qué pase leer
            pases = pases[pases_desde_hasta[0] - 1:pases_desde_hasta[1]]

        # Sea la opción de mostrarlos todos, o un segmento, al final recorremos el array de pases e imprimimos cada uno de ellos
        for pase in pases:
            print(pase)
    # Cerramos el archivo para evitar conflictos
    archivo_de_pases.close()
    # Mostramos el menu para Seleccionar una nueva opción o salir
    mostrar_menu(2)

# Esta función es llamada en la selección de terminal de Leer pases desde y hasta un número específico
def leer_pases_especificos():
    # Donde mientras el número de pases a leer inicialmente sea menor a 0, se le solicitará al usuario que ingrese un número mayor a 0
    pases_from = int(input("Ingrese desde qué pase quiere leer: "))
    while pases_from <= 0:
        pases_from = int(input("El número de pase debe ser mayor a 0.\n Ingrese desde qué pase quiere leer: \n"))

    # Y mientras el número de pases a leer finalmente sea menor al inicial, se le solicitará al usuario que ingrese un número mayor al inicial
    pases_to = int(input("Ingrese hasta qué pase quiere leer: "))
    while pases_to < pases_from:
        pases_to = int(input("El número de pase debe ser mayor al de inicio.\n Ingrese hasta qué pase quiere leer: \n"))

    # Creamos una tupla en la que guardamos el rango de numeros de pases a leer y ejecutamos leer_pases enviándola
    pases_desde_hasta = (pases_from, pases_to)
    leer_pases(pases_desde_hasta)
    
# Generación randomizada de pases
def simulacion_de_pases():
    # Apertura del archivo de pases en modo escritura
    archivo_de_pases = open('./pases.txt', 'w')
    
    n = 1
    # Mientras n sea menor a 50.000 generamos un nuevo pase
    while n <= 50000:
        # Seleccionando de manera random el equipo
        equipo = random.choice(['Argentina','Australia'])
        # Seleccionando de manera random el éxito del pase (0 no exitoso, 1 exitoso)
        exito = random.choice([0,1])
        # Seleccionamos del diccionario equipos el equipo randomizado anteriormente la jugadora (una tupla)
        jugadora = random.choice(equipos[equipo])
        # Y randomizamos el minuto del partido de la ejecución del pase, entre 0 y 70
        minuto = random.randint(0, 70)
        
        # Creamos el respectivo string con todos los datos del pase
        # jugadora[1] siendo el número de camiseta y jugador[0] el nombre de la jugadora
        pase = f"{equipo};{jugadora[1]};{jugadora[0]};{exito};{minuto}"
        
        # Escribimos en el archivo el pase con un salto de linea
        archivo_de_pases.write(pase + "\n")
    
        n += 1

    # Cerramos el archivo para evitar conflictos
    archivo_de_pases.close()
    print("\nSe han creado exitosamente 50.000 pases\n")
    # Mostramos el menu para Seleccionar una nueva opción o salir
    mostrar_menu(2)

# Matriz de opciones de menú
# menu_opciones[0] = Hace referencia al menu inicial/principal del programa
# menu_opciones[1] = Hace referencia al menu de lectura de pases
# menu_opciones[2] = Hace referencia al menu de opciones de salida o de una nueva selección (menú auxiliar)
# En estos arrays de menúes contamos con la etiqueta de texto y la función a ejecutar en caso de seleccionar la opción
menu_opciones = [
    [
        {"etiqueta": "Crear archivo de pases", "funcion": crear_archivo},
        {"etiqueta": "Escribir simulación de pases (50.000)", "funcion": simulacion_de_pases},
        {"etiqueta": "Leer archivo de pases", "funcion": leer_pases},
        {"etiqueta": "Eliminar archivo de pases", "funcion": eliminar_archivo},
        {"etiqueta": "Salir", "funcion": print},
    ],
    [
        {"etiqueta": "Leer todos los pases", "funcion": leer_pases},
        {"etiqueta": "Leer pases desde y hasta un número específico", "funcion": leer_pases_especificos},
        {"etiqueta": "Volver atrás", "funcion": print},
        {"etiqueta": "Salir", "funcion": print},
    ],
    [
        {"etiqueta": "Seleccionar otra opción", "funcion": print},
        {"etiqueta": "Salir", "funcion": print},
    ]
]

opcion = 0
menu = 0

# Si el valor de menu no viene como parámetro en la ejecución de la función, su valor por defecto será 0
def mostrar_menu(menu = 0):
    # Recorremos del menu_opciones el array en la posición del menu seleccionado
    # e imprimimos cada una de sus etiquetas con el número
    for i, opcion in enumerate(menu_opciones[menu], start=1):
        print(f"{i}. {opcion['etiqueta']}")
    
    # Solicitud de input de opción
    print("\n")
    opcion = int(input(''))
    print("\n")

    # Mientras la opción seleccionada sea menor a 1 o mayor a la cantidad de opciones del menú, se le solicitará al usuario que ingrese una opción válida
    while opcion < 1 or opcion > len(menu_opciones[menu]):
        print('Opción inválida')
        mostrar_menu(menu)
        
    # Casos específicos de Salida o nueva selección de menú entre las opciones, mostrando un menú especifico necesario.
    if menu == 1 and opcion == 3:
        mostrar_menu(0)
    elif menu == 2 and opcion == 1:
        mostrar_menu(0)
    elif menu == 0 and opcion == 3:
        mostrar_menu(1)
    else:
        # En caso de no ser una opción de salida o nueva selección de menú, ejecutamos la función de la opción seleccionada
        menu_opciones[menu][opcion - 1]['funcion']()
        


# Ejecución inicial del menú principal
print("\nSimulación de pases de juego de hockey femenino\nArgentina vs. Australia\n")
mostrar_menu()
