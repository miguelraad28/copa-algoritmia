import random
import time

cancha = [
  ["🤾","🤾"],
  ["🤾","🤾"],
]

contrincante = ""

puntos = {
  "Argentina": 0,
  "Contrincante": 0,
}

def ver_cancha():
    print(f"\nARGENTINA: {puntos['Argentina']} {contrincante}: {puntos['Contrincante']}")
    print("_________________________________________________________")
    print("|                                                       |")
    print("|             |             |             |             |")
    print("|_______________________________________________________|")
    print("|                                                       |")
    print("|             |     ",cancha[0][0],"     |     ",cancha[0][1],"     |             |")
    print("|_____________###############################___________|")
    print("|                                                       |")
    print("|             |     ",cancha[1][0],"     |     ",cancha[1][1],"     |             |")
    print("|_______________________________________________________|")
    print("|                                                       |")
    print("|             |             |             |             |")
    print("|_______________________________________________________|")

def tira_contrincante(tipo):
    ver_cancha()
    ver_cancha()
    print(f"\n¡{tipo} el contrincante!")
    donde = random.choice([1, 2])
    time.sleep(2)
    if donde == 1:
        cancha[1][0] = "🥎🤾"
    else:
        cancha[1][1] = "🥎🤾"
    
    validar_tiro(contrincante, donde, 1)
    ver_cancha()

def validar_tiro(equipo, tiro, jugador_que_tira):
    pega_en_red = random.choice([True]*1 + [False]*9)
    pega_fuera_de_cancha = random.choice([True]*1 + [False]*9)
    contrincante_falla = random.choice([True]*3 + [False]*7)

    if pega_en_red:
        print("\n¡El tiro pega en la red!")
        tira_contrincante("Saca")
    elif pega_fuera_de_cancha:
        print("\n¡El tiro pega fuera de la cancha!")
        tira_contrincante("Saca")
    elif contrincante_falla:
        if equipo == "Argentina":
            cancha[0][int(tiro) - 1] = "🥎🤾"
            cancha[1][int(jugador_que_tira) - 1] = "🤾"
        else:
            cancha[1][int(tiro) - 1] = "🥎🤾"
            cancha[0][int(jugador_que_tira) - 1] = "🤾"
        print("\n¡El contrincante falla el tiro!")
        if equipo == "Argentina":
            puntos["Argentina"] += 1
            seleccionar_donde_tirar(False, 1)
        else:
            puntos["Contrincante"] += 1
            tira_contrincante(False, 2)
    else:
        #Continua la jugada
        if equipo == "Argentina":
            cancha[0][int(tiro) - 1] = "🥎🤾"
            cancha[1][int(jugador_que_tira) - 1] = "🤾"
            tira_contrincante("Tira")
        else:
            cancha[1][int(tiro) - 1] = "🥎🤾"
            cancha[0][int(jugador_que_tira) - 1] = "🤾"
            seleccionar_donde_tirar(False, 1)

def seleccionar_donde_tirar(saque = False, jugador_inicial = 1):
    opciones_validas_de_tiro = ["1", "2"]
    print("1. Raquetear a la izquierda")
    print("2. Raquetear a la derecha")
    donde_tirar = input("\nElige una opción: ")
    
    
    if saque and jugador_inicial == 1:
        opciones_validas_de_tiro = ["2"]
    elif saque and jugador_inicial == 2:
        opciones_validas_de_tiro = ["1"]
      
    
    while donde_tirar not in opciones_validas_de_tiro:
        donde_tirar = input("\nElige una opción válida (Solo puedes tirar al lado opuesto de tu jugador seleccionado): ")
    
    validar_tiro("Argentina", donde_tirar, jugador_inicial)
    ver_cancha()

def elije_jugador_inicial():
    print("Elige con que jugador sacarás:")
    print("1. Jugador izquierda")
    print("2. Jugador derecha\n")
    jugador_inicial = input("Elige una opción: ")
    
    while jugador_inicial not in ["1", "2"]:
        jugador_inicial = input("Elige una opción válida: ")
        # 🎾
    if jugador_inicial == "1":
        cancha[1][0] = "🥎🤾"
    else:
        cancha[1][1] = "🥎🤾"
    return jugador_inicial

def elije_contrincante():
    contrincantes = ["Francia", "Paises Bajos", "Japon", "China"]
    print("¡Bienvenido a la final de tenis de los juegos olímpicos!\n")
    print("Elige a tu contrincante:")
    print(f"1. {contrincantes[0]}")
    print(f"2. {contrincantes[1]}")
    print(f"3. {contrincantes[2]}")
    print(f"4. {contrincantes[3]}\n")
    opcion = input("Elige una opción: ")
    print("")
    
    while opcion not in ["1", "2","3","4"]:
      contrincante = input("\nElige una opción válida: \n")
      # 🎾
    
    contrincante = contrincantes[int(opcion) - 1]
    
    return contrincante

preguntas = [
  {  "pregunta": "¿Quién ha ganado más títulos de Grans Slam en la historia del tenis masculino?",
    "respuestas": ["Novak Djokovic", "Roger Federer", "Rafael Nadal", "Pete Sampras"],
    "respuesta_correcta": "Novak Djokovic"},
    {"pregunta": "¿En qué superficie se juega el torneo de Wimbledon?",
     "respuestas": ["Arcilla", "Césped", "Dura", "Moqueta"],
     "respuesta_correcta": "Césped"},
        {"pregunta": "¿Cómo se llama el golpe que se realiza con el dorso de la mano dominante hacia delante?",
     "respuestas": ["Drive", "Volea", "Revés", "Slice"],
     "respuesta_correcta": "Revés"},
        {"pregunta": "¿Cuál es la puntuación mínima para ganar un juego, sin contar el 'deuce'?",
     "respuestas": ["3", "4", "5","6"],
     "respuesta_correcta": "4"},
        {"pregunta": "¿Cómo se llama el área desde donde se sirve en el tenis?",
     "respuestas": ["Red", "Línea de fondo", "Línea de servicio", "Cuadro de servicio"],
     "respuesta_correcta": "Cuadro de servicio"},
        {"pregunta": "¿Cuál de los siguientes no es un torneo de Grand Slam?",
     "respuestas": ["Abierto de Australia", "Roland Garros", "Abierto de Canadá", "US Open"],
     "respuesta_correcta": "Abierto de Canadá"},
        {"pregunta": "¿En qué año se introdujo el 'tie-break' en Wimbledon?",
     "respuestas": ["1970", "1971", "1972", "1973"],
     "respuesta_correcta": "1973"},
        {"pregunta": "¿Qué significa el término 'deuce' en un juego de tenis?",
     "respuestas": ["Igualdad a 30", "Igualdad a 40", "Ventaja para el receptor", "Juego ganado"],
     "respuesta_correcta": "Igualdad a 40"},
        {"pregunta": "¿Cómo se llama el golpe que se realiza sin que la pelota toque el suelo?",
     "respuestas": ["Saque", "Volea", "Dropshot", "Passing shot"],
     "respuesta_correcta": "Volea"},
        {"pregunta": "¿Qué jugador o jugadora ha ganado más títulos de Grand Slam en la historia del tenis femenino?",
     "respuestas": ["Steffi Graff", "Serena Williams", "Margaret Court", "Martina Navratilova"],
     "respuesta_correcta": "Margaret Court"},
]



def empezarCuestionario():
    print('')
    print('Veamos cuánto sabes de tenis!')
    print('')
    aciertos = 0
    errores = 0
    for pregunta in preguntas:
        print(pregunta["pregunta"])
        print('Opciones')
        i = 1
        for respuesta in pregunta["respuestas"]:
            print(i , '-' , respuesta)
            i =  i+1
        opcion = int(input("Seleccione una opción: "))
        if opcion >= 5 or opcion <1:
            print('Opción inválida, por favor seleccione una opción válida')
            opcion = int(input("Seleccione una opción: "))
        if pregunta["respuestas"][opcion-1] == pregunta["respuesta_correcta"]:
            print('Acertaste!')
            aciertos = aciertos + 1
        else:
            print('Te equivocaste!')
            errores = errores + 1
    print('')
    print('')
    if aciertos > 5:
        print('Bien, parece que sabes algo de tenis')
    if aciertos >= 8:
        print('Bueno parece que sabés bastate sobre tenis!')
    elif aciertos == 10:
        print('Basado, acaso sos tenista profesional? Respondiste todo bien!')
    elif aciertos <=5:
        print('Bueno andas medio flojo con el tenis, pero podes volver a intentarlo!')
    print('')
    print('Respuestas correctas: ', aciertos)
    print('Respuestas incorrectas: ', errores)



empezarCuestionario()

print("\nAhora un pequeño partido de tenis para relajarnos\n")

contrincante = elije_contrincante()
num = elije_jugador_inicial()
ver_cancha()
seleccionar_donde_tirar(True, int(num))