
# asyncio está importado con la finalidad de una mejor UX, ya que se pueden hacer esperas de tiempo
# para que el usuario pueda ver el resultado de la pateada, a dónde fué el balón
# mensajes de euforia y mientras la computadora "Países Bajos" "piensa" a dónde patear
import asyncio
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

# Variable global que indica si estamos en modo muerte súbita o no
# Debemos declararla global ya que no estámos modificando alguna propiedad de un diccionario o lista,
# por lo que si no es mutable, no se puede modificar dentro de las funciones (A diferencia de marcadores o arco)
global modo_muerte_subita
modo_muerte_subita = False

# Función dedicada a iniciar un nuevo ciclo sin importar que equipo pateó por última vez
async def iniciar_muerte_subita():
    # Cambiamos el valor global de modo_muerte_subita para ciertos condicionales que están al rededor de la app.
    global modo_muerte_subita
    modo_muerte_subita = True
    # Iniciamos la muérte súbita, nuevamente Argentina inicia a patear
    imprimir_arco()
    await selecciona_tiro_argentina()

# Función para en base al último equipo que pateó, cambiar al otro equipo
async def cambia_equipo(equipo):
    # Si num == -1 significa que algún equipo ya ganó el partido o se inicia el ciclo de muerte súbita
    # De esta forma cortamos el flujo del juego (Y en caso de ser muerte súbita se inicia el ciclo con la llamada a la función iniciar_muerte_subita())
    num = await verificar_ganador()
    if num == -1: 
        return

    # Según el equipo que haya pateado, le toca al contrario.
    equipo = 'paises_bajos' if equipo == 'argentina' else 'argentina'
    imprimir_arco()
    
    # Si el equipo que patea, volvemos a la función del flujo inicial, donde se solicita al usuario un número
    if equipo == 'argentina':
        await selecciona_tiro_argentina()
    else:
        # Si el equipo que patea es países bajos, le hacemos saber al usuario, y hacemos una espera
        # de 2 segundos mientras Países bajos "piensa" a donde patear
        print("\nPATEA PAÍSES BAJOS")
        await asyncio.sleep(2)
        num = random.randint(1, 9)
        # Ejecutamos la pateada y repetimos flujo.
        await patear('paises_bajos', num)

# Esta función se encarga de verificar el ganador
async def verificar_ganador():
    # Se utiliza la ejecución de este if para ver el ganador en caso de estar en modo muerte súbita
    if modo_muerte_subita:
        # Nos interesa saber si hay ganador en muerte súbita cuando ya ambos equipos patearon, así que primero validamos eso.
        if len(marcadores["argentina"]) and len(marcadores["paises_bajos"]):
            # Si ambos fallaron o ambos metieron gol, se reinician los marcadores y se inicia otro ciclo de muerte súbita
            if marcadores["argentina"][0] == '🟩' and marcadores["paises_bajos"][0] == '🟩' or marcadores["argentina"][0] == '🟥' and marcadores["paises_bajos"][0] == '🟥':
                marcadores["argentina"] = []
                marcadores["paises_bajos"] = []
                print("\n💀💀 Otra ronda más!!! 😨😧")
                await asyncio.sleep(2)
                await iniciar_muerte_subita()
                return -1

            elif marcadores["argentina"][0] == '🟩' and marcadores["paises_bajos"][0] == '🟥':
                # En caso de que Argentina haya metido gol y Países Bajos no, se muestra el mensaje de ganador
                print("\n🎊🙌🏻🎇🎆🍾🍻 ¡¡GANA ARGENTINA LA MUERTE SÚBITA!! 🍻🎆🍾🎇🙌🏻")
                # Al retornar -1 y no llamar a la función iniciar_muerte_subita(), el programa finaliza con este mensaje.
                return -1

            elif marcadores["paises_bajos"][0] == '🟩' and marcadores["argentina"][0] == '🟥':
                # En caso de que Países Bajos haya metido gol y Argentina no, se muestra el mensaje de ganador
                print("\n💢 Gana Países Bajos la muerte súbita pero porque compraron al árbitro 💲")
                # Al retornar -1 y no llamar a la función iniciar_muerte_subita(), el programa finaliza con este mensaje.
                return -1
    else:
        # En caso de no estar en muerte súbita, se verifica si ya hay un ganador del partido
        faltantes_argentina = 5 - len(marcadores['argentina'])
        goles_argentina = sum(1 for x in marcadores["argentina"] if x == '🟩')

        faltantes_paises_bajos = 5 - len(marcadores['paises_bajos'])
        goles_paises_bajos = sum(1 for x in marcadores["paises_bajos"] if x == '🟩')

        if faltantes_argentina + goles_argentina < goles_paises_bajos:
            # Validación si ya Argentina no tiene posibilidad de ganarle a países bajos
            print("💢 Gana Países Bajos pero porque compraron al árbitro 💲")
            # El return del -1 es para cortar el flujo del juego
            return -1

        elif faltantes_paises_bajos + goles_paises_bajos < goles_argentina:
            # Validación si ya Países Bajos no tiene posibilidad de ganarle a países bajos
            print("🎊🙌🏻🎇🎆🍾🍻 ¡¡GANA ARGENTINA!! 🍻🎆🍾🎇🙌🏻")
            # El return del -1 es para cortar el flujo del juego
            return -1

        elif len(marcadores["argentina"]) == 5 and len(marcadores["paises_bajos"]) == 5:
            # Reiniciamos los contadores para la muerte súbita
            marcadores["argentina"] = []
            marcadores["paises_bajos"] = []
            # Inicio de cilo de muerte súbita
            print("\n\n☠️ ¡Inicia la muerte súbita! ☠️\n")
            await iniciar_muerte_subita()
            # El return del -1 es para cortar el flujo del juego
            # En este caso, es previamente llamada a la función iniciar_muerte_subita() para empezar un ciclo de muerte súbita
            return -1

async def patear(equipo, num):
    # Identificámos en qué lugar de la matriz se encuentra el número ingresado por el usuario
    fila = (num - 1) // 3
    columna = (num - 1) % 3
    
    # Actualizar la posición en el arco con "🏑" para mostrarle visualmente al usuario a dónde fué el balón/disco
    arco[fila][columna] = "🏑"
    
    # El éxito del tiro siempre será True, a menos que se haya seleccionado 2, 5 u 8
    exito = True
    if num in [2,5,8]:
        exito = False

    # Actualizamos el marcador y mostramos el arco con el nuevo marcador y mostrándo a dónde se pateó
    actualizar_marcador(equipo, exito)
    imprimir_arco()

    # Volvemos a poner el número en la posición del arco
    arco[fila][columna] = num

    # Un par de mensajes de eufória del partido Jeje.
    if exito and equipo == 'argentina':
        print("🏑¡GOL DE ARGENTINAAAAAAA VAMOOOOOOOOOOS 🍻🍾🎆🎇!")
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
    # Si estamos en muerte súbita, modificamos los tiros que tiene cada equipo
    tiros_por_equipo = 1 if modo_muerte_subita else 5
    
    # Sumamos los cuadraditos 🟩 o 🟥 de los tiros ya realizados
    tiros_argentina = ''.join(marcadores['argentina'])
    # Y con la diferencia de 5 o 1 (depende si esta en muerte súbita),
    # completamos con cuadraditos vacíos ⬜
    faltantes_argentina = tiros_por_equipo - len(marcadores['argentina'])
    # El join se utiliza para concatenar los elementos de la lista en un string
    tiros_argentina = tiros_argentina + ''.join('⬜' * faltantes_argentina)
    
    # Sumamos los cuadraditos 🟩 o 🟥 de los tiros ya realizados
    tiros_paises_bajos = ''.join(marcadores['paises_bajos'])
    # Y con la diferencia de 5 o 1 (depende si esta en muerte súbita),
    # completamos con cuadraditos vacíos ⬜
    faltantes_paises_bajos = tiros_por_equipo - len(marcadores['paises_bajos'])
    # El join se utiliza para concatenar los elementos de la lista en un string
    tiros_paises_bajos = tiros_paises_bajos + ''.join('⬜' * faltantes_paises_bajos)

    print("\nARGENTINA    vs.    PAÍSES BAJOS")
    # Pequeño if ternario para ajustar el print de los marcadores.
    print(tiros_argentina, "        ",tiros_paises_bajos) if not modo_muerte_subita else print("  ",tiros_argentina, "                  ",tiros_paises_bajos)

# La función imprimir_arco() se encarga de mostrar el arco con los contadores de tiros por equipo
def imprimir_arco():
    # Llama al contador
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
    num = input("\nPATEA ARGENTINA: Ingrese el número de tiro: ")

    # Validez de número entero
    num_int = validar_input(num)
    
    # Mientras sea menor a 1 o mayor a 9 vuelve a solicitar
    while num_int < 1 or num_int > 9:
        print("Ingrese un número válido entre 1 y 9")
        num = input("\nPATEA ARGENTINA: Ingrese el número de tiro: ")
        num_int = validar_input(num)
    
    # Pateamos, enviandole el equipo que patea, y a dónde (num_int)
    await patear('argentina', num_int)

# Inicialización del programa
imprimir_arco()
asyncio.run(selecciona_tiro_argentina())