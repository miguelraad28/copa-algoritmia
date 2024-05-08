# Importamos random para generar números aleatorios y os validar existencia de archivos y su eliminación
import random
import os

# Matriz de equipos con sus respectivas jugadoras - Cada elemento del array es un equipo
# equipos[0] = Argentina - Cada elemento del array es una tupla con el nombre de la jugadora y su número
# equipos[1] = Australia - Cada elemento del array es una tupla con el nombre de la jugadora y su número
equipos = [
    [
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
    [
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
]

def crear_archivo():
    if not os.path.exists('./pases.txt'):
        open('./pases.txt', 'x').close()
        print("Archivo de pases creado correctamente\n")
    else:
        print("\nEl archivo de pases ya existe\n")
        
    mostrar_menu(2)

def eliminar_archivo():
    if os.path.exists('./pases.txt'):
        os.remove('./pases.txt')
        print("Archivo de pases eliminado correctamente")
    else:
        print("El archivo de pases no existe")
        
    mostrar_menu(2)

def escribir_pase(pase, archivo_de_pases):
    archivo_de_pases.write(pase + "\n")
    return archivo_de_pases

def leer_pases_especificos():
    pases_from = int(input("Ingrese desde qué pase quiere leer: "))
    while pases_from <= 0:
        pases_from = int(input("El número de pase debe ser mayor a 0.\n Ingrese desde qué pase quiere leer: \n"))

    pases_to = int(input("Ingrese hasta qué pase quiere leer: "))
    while pases_to < pases_from or pases_to <= 0:
        pases_to = int(input("El número de pase debe ser mayor al de inicio.\n Ingrese hasta qué pase quiere leer: \n"))

    pases_desde_hasta = (pases_from, pases_to)
    leer_pases(pases_desde_hasta)

def leer_pases (pases_desde_hasta = False):
    archivo_de_pases = os.path.exists('./pases.txt')

    if not archivo_de_pases:
        print("\nNo se encontró el archivo de pases\n")
    else:
        archivo_de_pases = open('./pases.txt', 'r')
        pases = archivo_de_pases.readlines()
        if len(pases) == 0:
            print("No hay pases para mostrar\n")
        if not pases_desde_hasta:
            print("Leyendo archivo de pases...\n")
        else:
            print("\nLeyendo pases desde el ", pases_desde_hasta[0], " hasta el ",  pases_desde_hasta[1], "...\n")
            pases = pases[pases_desde_hasta[0] - 1:pases_desde_hasta[1]]


        for pase in pases:
            print(pase)

    archivo_de_pases.close()
    mostrar_menu(2)
        
def simulacion_de_pases():
    archivo_de_pases = open('./pases.txt', 'a')
    
    n = 1
    while n <= 50000:
        equipo = random.choice([0,1])
        exito = random.choice([0,1])
        jugadora = random.choice(equipos[equipo])
        minuto = random.randint(0, 70)
        
        if equipo == 0:
            team_name = 'Argentina'
        else:
            team_name = 'Australia'
        
        pase = f"{team_name};{jugadora[1]};{exito};{jugadora[0]};{minuto}"
        
        escribir_pase(pase, archivo_de_pases)
        
        n += 1

    archivo_de_pases.close()
    print("\nSe han creado exitosamente 50.000 pases\n")
    mostrar_menu(2)

menu_opciones = [
    [
        {"etiqueta": "Crear archivo de pases", "funcion": crear_archivo},
        {"etiqueta": "Leer archivo de pases", "funcion": leer_pases},
        {"etiqueta": "Escribir simulación de pases (50.000)", "funcion": simulacion_de_pases},
        {"etiqueta": "Eliminar archivo de pases", "funcion": eliminar_archivo},
        {"etiqueta": "Salir", "funcion": print},
    ],
    [
        {"etiqueta": "Leer todos los pases", "funcion": leer_pases},
        {"etiqueta": "Leer pases desde y hasta un número específico", "funcion": leer_pases_especificos},
        {"etiqueta": "Volver atrás", "funcion": False},
        {"etiqueta": "Salir", "funcion": print},
    ],
    [
        {"etiqueta": "Seleccionar otra opción", "funcion": print},
        {"etiqueta": "Salir", "funcion": print},
    ]
]

opcion = 0
menu = 0

def mostrar_menu(menu = 0):
    for i, opcion in enumerate(menu_opciones[menu], start=1):
        print(f"{i}. {opcion['etiqueta']}")
    
    print("\n")
    opcion = int(input(''))
    print("\n")

    while opcion < 1 or opcion > len(menu_opciones[menu]):
        print('Opción inválida')
        mostrar_menu(menu)
        
    if menu == 1 and opcion == 3:
        mostrar_menu(0)
    elif menu == 2 and opcion == 1:
        mostrar_menu(0)
    elif menu == 0 and opcion == 2:
        mostrar_menu(1)
    else:
        menu_opciones[menu][opcion - 1]['funcion']()
    
    return (opcion, menu)

print("\nSimulación de pases de juego de hockey femenino\nArgentina vs. Australia\n")
mostrar_menu()
