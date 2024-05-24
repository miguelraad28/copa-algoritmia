
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

async def cambia_equipo(equipo):
    equipo = 'paises_bajos' if equipo == 'argentina' else 'argentina'
    imprimir_arco()

    if not verificar_ganador():
        if equipo == 'argentina':
            await selecciona_tiro_argentina()
        else:
            print("PATEA PAÍSES BAJOS")
            await asyncio.sleep(2)
            num = random.randint(1, 9)
            await patear('paises_bajos', num)
    else:
        equipo_ganador = verificar_ganador()
        if equipo_ganador == 'paises_bajos':
            print("PAISES BAJOS ES EL GANADOR DEL PARTIDO Y DE LAS OLIMPIADAS 2024! 🏆")
        else:
            print("ARGENTINA ES EL GANADOR DEL PARTIDO Y DE LAS OLIMPIADAS 2024! 🏆")

async def patear(equipo, num):
    fila = (num - 1) // 3
    columna = (num - 1) % 3
    
    # Validar que el número esté dentro del rango esperado
    if num < 1 or num > 9:
        print("Número inválido")
        return
    
    # Actualizar la posición en el arco con "⚽️"
    arco[fila][columna] = "⚽️"
    
    exito = True
    if num in [2,5,8]:
        exito = False
    actualizar_marcador(equipo, exito)
    imprimir_arco()
    arco[fila][columna] = num
    # TODO: menu para continuar y mostrar el arco quitando la pelota de la posición
    if exito and equipo == 'argentina':
        print("¡GOL DE ARGENTINAAAAAAA VAMOOOOOOOOOOS 🍻🍾🎆🎇!")
    elif not exito and equipo == 'argentina':
        print('AAAA CASI METEMOS GOOOL 😭😭😭')
    elif exito and equipo == 'paises_bajos':
        print("Daaale loco no puede ser que nos metieron gol 😡😡")
    elif not exito and equipo == 'paises_bajos':
        print("Uff por poco nos meten gol 😅😅")

    await asyncio.sleep(3)
    
    await cambia_equipo(equipo)

def actualizar_marcador(equipo, exito):
    if exito:
        marcadores[equipo].append("🟩")
    else:
        marcadores[equipo].append("🟥")

def ver_contador():
    tiros_argentina = ''.join(marcadores['argentina'])
    tiros_paises_bajos = ''.join(marcadores['paises_bajos'])
    faltantes_argentina = 5 - len(marcadores['argentina'])
    faltantes_paises_bajos = 5 - len(marcadores['paises_bajos'])
    print()
    print("ARGENTINA    vs.    PAÍSES BAJOS")
    print(tiros_argentina + ''.join(["⬜"] * faltantes_argentina), "        ",tiros_paises_bajos + ''.join(["⬜"] * faltantes_paises_bajos))
  
def imprimir_arco():
    ver_contador()
    print("___________________________________________")
    for i in range(3):
        print("|                                         |")
        print("|     ", arco[i][0], "     |     ", arco[i][1], "     |     ", arco[i][2], "     |")
        if i < 2:
            print("|_________________________________________|")
    print("|                                         |")

def validar_input(value):
    try:
        num_int = int(value)
        return num_int
    except ValueError:
        return -1

async def selecciona_tiro_argentina():
    num = input("PATEA ARGENTINA: Ingrese el número de tiro: ")

    num_int = validar_input(num)

    while num_int < 1 or num_int > 9:
        print("Ingrese un número válido entre 1 y 9")
        num = input("PATEA ARGENTINA: Ingrese el número de tiro: ")
        num_int = validar_input(num)
        
    await patear('argentina', num_int)

def verificar_ganador():
    goles_argentina = sum(1 for x in marcadores['argentina'] if x == "🟩")
    fallos_argentina = sum(1 for x in marcadores['argentina'] if x == "🟥")
    goles_paises_bajos = sum(1 for x in marcadores['paises_bajos'] if x == "🟩")
    fallos_paises_bajos = sum(1 for x in marcadores['paises_bajos'] if x == "🟥")
    tiros_argentina = len(marcadores['argentina'])
    tiros_paises_bajos = len(marcadores['paises_bajos'])

    if goles_argentina >= 3 and fallos_paises_bajos >= 3:
        return 'argentina'
    elif goles_paises_bajos >= 3 and fallos_argentina >= 3:
        return 'paises_bajos'

    if tiros_argentina >= 5 and tiros_paises_bajos >= 5:
        if goles_argentina > goles_paises_bajos:
            return 'argentina'
        elif goles_paises_bajos > goles_argentina:
            return 'paises_bajos'
        else:
            for i in range(5, max(tiros_argentina, tiros_paises_bajos)):
                if i < tiros_argentina and i < tiros_paises_bajos:
                    if marcadores['argentina'][i] == "🟩" and marcadores['paises_bajos'][i] == "🟥":
                        return 'argentina'
                    elif marcadores['argentina'][i] == "🟥" and marcadores['paises_bajos'][i] == "🟩":
                        return 'paises_bajos'
    return None 

imprimir_arco()
asyncio.run(selecciona_tiro_argentina())