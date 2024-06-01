# time está importado con la finalidad de una mejor UX, ya que se pueden hacer esperas de tiempo
# para que el usuario pueda ver el resultado de la pateada, a dónde fué el balón
# mensajes de euforia y mientras la computadora "Países Bajos" "piensa" a dónde patear
import time
# random se importa para que Países Bajos pueda patear a un lugar aleatorio
import random

# Matriz que representa el arco de fútbol
arco = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
]

# Diccionario que contiene los marcadores de cada equipo
marcadores = {
    'argentina': [],
    'paises_bajos': [],
}

async def cambia_equipo(equipo):
    # Según el equipo que haya pateado, le toca al contrario.
    equipo = 'paises_bajos' if equipo == 'argentina' else 'argentina'
    imprimir_arco(MS)
    
    # Si el equipo que patea, volvemos a la función del flujo inicial, donde se solicita al usuario un número
    if equipo == 'argentina':
        await selecciona_tiro_argentina()
    else:
        # Si el equipo que patea es países bajos, le hacemos saber al usuario, y hacemos una espera
        # de 2 segundos mientras Países bajos "piensa" a donde patear
        print("PATEA PAÍSES BAJOS")
        await asyncio.sleep(2)
        num = random.randint(1, 9)
        # Ejecutamos la pateada y repetimos flujo.
        await patear('paises_bajos', num)

async def patear(equipo, num):
    fila = (num - 1) // 3
    columna = (num - 1) % 3
    
    # Por una cuestión visual, si el número pateado es 2, 5 u 8, se ataja en el mismo lugar así la manito sale junto al balón
    if num_pateada in [2,5,8]:
        num_atajada = num_pateada
    
    fila_atajada = (num_atajada - 1) // 3
    columna_atajada = (num_atajada - 1) % 3
    
    exito = True
    
    if num_pateada in [2,5,8] or num_pateada == num_atajada:
        exito = False
    
    if num_pateada == num_atajada:
        arco[fila_pateada][columna_pateada] = '🧤⚽'
    else: 
        arco[fila_pateada][columna_pateada] = '⚽'
        arco[fila_atajada][columna_atajada] = '🧤'

    actualizar_marcador(equipo, exito)
    imprimir_arco(MS)

    # Volvemos a poner el número en la posición del arco
    arco[fila_pateada][columna_pateada] = num_pateada
    arco[fila_atajada][columna_atajada] = num_atajada

    # Un par de mensajes de eufória del partido Jeje.
    if exito and equipo == 'argentina':
        print("⚽¡GOL DE ARGENTINAAAAAAA VAMOOOOOOOOOOS 🍻🍾🎆🎇!")
    elif not exito and equipo == 'argentina':
        print('AAAA CASI METEMOS GOOOL 😭😭😭')
    elif exito and equipo == 'paises_bajos':
        print("Daaale loco no puede ser que nos metieron gol 😡😡")
    elif not exito and equipo == 'paises_bajos':
        print("Uff por poco nos meten gol 😅😅")

    # Esperamos 3 segundos para que el usuario pueda ver el resultado del tiro
    await asyncio.sleep(3)
    
    # Cambio de equipo
    await cambia_equipo(equipo)

def actualizar_marcador(equipo, exito):
    exito = "🟩" if exito else "🟥"
    marcadores[equipo].append(exito)

def ver_contador():
    tiros_argentina = ''.join(marcadores['argentina'])
    faltantes_argentina = 5 - len(marcadores['argentina'])
    tiros_argentina = tiros_argentina + ''.join('⬜' * faltantes_argentina)
    
    # Sumamos los cuadraditos 🟩 o 🟥 de los tiros ya realizados
    tiros_paises_bajos = ''.join(marcadores['paises_bajos'])
    faltantes_paises_bajos = 5 - len(marcadores['paises_bajos'])
    tiros_paises_bajos = tiros_paises_bajos + ''.join('⬜' * faltantes_paises_bajos)

    print("\nARGENTINA    vs.    PAÍSES BAJOS")
    print(tiros_argentina, "        ",tiros_paises_bajos)
  
def imprimir_arco():
    ver_contador()
    print("___________________________________________")
    print("|                                         |")
    print("|     ", arco[0][0], "     |     ", arco[0][1], "     |     ", arco[0][2], "     |")
    print("|_________________________________________|")
    print("|                                         |")
    print("|     ", arco[1][0], "     |     ", arco[1][1], "     |     ", arco[1][2], "     |")
    print("|_________________________________________|")
    print("|                                         |")
    print("|     ", arco[2][0], "     |     ", arco[2][1], "     |     ", arco[2][2], "     |")
    print("|                                         |")

# Validación de que sea un número entero
def validar_input(num):
    try:
        num_int = int(num)
        return num_int
    except ValueError:
        # Si no es número, devuelve -1 (no ingresando al rango de 1 a 9)
        return -1

# Función para permitir al usuario ingresar a dónde quiere patear
async def selecciona_tiro_argentina():
    num = input("PATEA ARGENTINA: Ingrese el número de tiro: ")

    # Validez de número entero
    num_pateada = validar_input(num)
    
    # Mientras sea menor a 1 o mayor a 9 vuelve a solicitar
    while num_pateada < 1 or num_pateada > 9:
        print("\nIngrese un número válido entre 1 y 9\n")
        num = input("\nPATEA ARGENTINA 🦿: Ingrese el número de tiro: ")
        num_pateada = validar_input(num)
    
    # Pateamos, enviandole el equipo que patea, y a dónde (num_int)
    await patear('argentina', num_int)

# Inicialización del programa
imprimir_arco()
selecciona_tiro_argentina()