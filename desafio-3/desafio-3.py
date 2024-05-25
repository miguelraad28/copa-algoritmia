
import asyncio
import random

arco = [
  [1,2,3],
  [4,5,6],
  [7,8,9],
]

marcadores = {
  'argentina': [],
  'paises_bajos': [],
}

async def iniciar_muerte_subita():
    imprimir_arco(True)
    await selecciona_tiro_argentina(True)
    if len(marcadores["argentina"]):
        tiro_argentina = marcadores["argentina"][0]
    if len(marcadores["paises_bajos"]):
        tiro_paises_bajos = marcadores["paises_bajos"][0]

    while tiro_paises_bajos == '🟥' and tiro_argentina == '🟥' or tiro_paises_bajos == '🟩' and tiro_argentina == '🟩':
        marcadores["argentina"] = []
        marcadores["paises_bajos"] = []
        print("Otra ronda más!!!")
            # await asyncio.sleep(2)
        await iniciar_muerte_subita()

    if marcadores["paises_bajos"][0] == '🟩' and marcadores["argentina"][0] == '🟥':
        print("Gana Países Bajos pero porque compraron al árbitro >:V")
    elif marcadores["paises_bajos"][0] == '🟥' and marcadores["argentina"][0] == '🟩':
        print("GANA ARGENTINAAAAA")

async def cambia_equipo(equipo, MS):
    # num = -1 es que alguien gano - num = -2 van a muerte súbita
    num = await verificar_ganador(MS)
    if num == -1: 
        return

    # Según el equipo que haya pateado, le toca al contrario.
    equipo = 'paises_bajos' if equipo == 'argentina' else 'argentina'
    imprimir_arco(MS)
    
    # Si el equipo que patea, volvemos a la función del flujo inicial, donde se solicita al usuario un número
    if equipo == 'argentina':
        await selecciona_tiro_argentina(MS)
    else:
        # Si el equipo que patea es países bajos, le hacemos saber al usuario, y hacemos una espera
        # de 2 segundos mientras Países bajos "piensa" a donde patear
        print("PATEA PAÍSES BAJOS")
        # await asyncio.sleep(2)
        num = 2#random.randint(1, 9)
        # Ejecutamos la pateada y repetimos flujo.
        await patear('paises_bajos', num, MS)
#####

async def verificar_ganador(MS):
    if MS and len(marcadores["argentina"]) and len(marcadores["paises_bajos"]):
        
    else:
        faltantes_argentina = 5 - len(marcadores['argentina'])
        goles_argentina = sum(1 for x in marcadores["argentina"] if x == '🟩')
        faltantes_paises_bajos = 5 - len(marcadores['paises_bajos'])
        goles_paises_bajos = sum(1 for x in marcadores["paises_bajos"] if x == '🟩')
        if faltantes_argentina + goles_argentina < goles_paises_bajos:
            print("Gana Países Bajos pero porque compraron al árbitro >:V")
            return -1
        elif faltantes_paises_bajos + goles_paises_bajos < goles_argentina:
            print("GANA ARGENTINA :D")
            return -1
        elif len(marcadores["argentina"]) == 5 and len(marcadores["paises_bajos"]) == 5:
            marcadores["argentina"] = []
            marcadores["paises_bajos"] = []
            await iniciar_muerte_subita()
            return -1

async def patear(equipo, num, MS):
    fila = (num - 1) // 3
    columna = (num - 1) % 3
    
    # Actualizar la posición en el arco con "⚽️" para mostrarle visualmente al usuario a dónde fué el balón/disco
    arco[fila][columna] = "⚽️"
    
    # El éxito del tiro siempre será True, a menos que se haya seleccionado 2, 5 u 8
    exito = True
    if num in [2,5,8]:
        exito = False

    # Actualizamos el marcador y mostramos el arco con el nuevo marcador y mostrándo a dónde se pateó
    actualizar_marcador(equipo, exito)
    imprimir_arco(MS)

    # Volvemos a poner el número en la posición del arco
    arco[fila][columna] = num

    # Un par de mensajes de eufória del partido Jeje.
    if exito and equipo == 'argentina':
        print("¡GOL DE ARGENTINAAAAAAA VAMOOOOOOOOOOS 🍻🍾🎆🎇!")
    elif not exito and equipo == 'argentina':
        print('AAAA CASI METEMOS GOOOL 😭😭😭')
    elif exito and equipo == 'paises_bajos':
        print("Daaale loco no puede ser que nos metieron gol 😡😡")
    elif not exito and equipo == 'paises_bajos':
        print("Uff por poco nos meten gol 😅😅")

    # Esperamos 3 segundos para que el usuario pueda ver el resultado del tiro
    # await asyncio.sleep(3)
    
    # Cambio de equipo
    await cambia_equipo(equipo, MS)

def actualizar_marcador(equipo, exito):
    exito = "🟩" if exito else "🟥"
    marcadores[equipo].append(exito)

def ver_contador(MS = False):
    tiros_por_equipo = 1 if MS else 5
    
    tiros_argentina = ''.join(marcadores['argentina'])
    faltantes_argentina = tiros_por_equipo - len(marcadores['argentina'])
    tiros_argentina = tiros_argentina + ''.join('⬜' * faltantes_argentina)
    
    tiros_paises_bajos = ''.join(marcadores['paises_bajos'])
    faltantes_paises_bajos = tiros_por_equipo - len(marcadores['paises_bajos'])
    tiros_paises_bajos = tiros_paises_bajos + ''.join('⬜' * faltantes_paises_bajos)
    print("\nARGENTINA    vs.    PAÍSES BAJOS")
    print(tiros_argentina, "        ",tiros_paises_bajos)

def imprimir_arco(MS = False):
    ver_contador(MS)
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
async def selecciona_tiro_argentina(MS = False):
    num = input("PATEA ARGENTINA: Ingrese el número de tiro: ")

    # Validez de número entero
    num_int = validar_input(num)
    
    # Mientras sea menor a 1 o mayor a 9 vuelve a solicitar
    while num_int < 1 or num_int > 9:
        print("Ingrese un número válido entre 1 y 9")
        num = input("PATEA ARGENTINA: Ingrese el número de tiro: ")
        num_int = validar_input(num)
    
    # Pateamos, enviandole el equipo que patea, y a dónde (num_int)
    await patear('argentina', num_int, MS)

# Inicialización del programa
imprimir_arco()
asyncio.run(selecciona_tiro_argentina())