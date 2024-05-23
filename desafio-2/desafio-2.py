equipos = {'Argentina': [], 'Australia': []}

# Función que recibe el equipo 'Argentina' 'Australia' y nombre que es el nombre de la jugadora ya existente en el array del equipo
def encontrar_indice_jugadora(equipo, nombre):
    for i, objeto in enumerate(equipos[equipo]):
        # Recorremos el array y buscamos una coincidencia con su nombre
            if objeto['nombre'] == nombre:
                indice = i
    # Retornamos el índice para usarlo posteriormente.
    return indice

# Función para sumar un pase a la jugadora en el array del equipo que llega como parámetro, el estado del pase_exitoso (1, 0 - True, False)
# Y el índice de la jugadora en el array de su equipo correspondiente.
def sumar_pase(equipo, pase_exitoso, indice):
    # Buscamos la jugadora en su equipo correspondiente
    jugadora = equipos[equipo][indice]
    # Le sumamos 1 al total de sus pases
    jugadora['cantidad_pases'] += 1
    # Y con un if ternario, si pase_exitoso es True, sumamos 1 en 'pases_bien' y de lo contrario, se lo sumamos 'a pases_mal'
    jugadora['pases_bien' if pase_exitoso else 'pases_mal'] += 1
    # Reemplazamos los nuevos valores de la jugadora en el array de su equipo
    equipos[equipo][indice] = jugadora

# Función de ordenamiento porcentual por pases exitosos
def ordenar_porcentualmente():
    # Recorremos los equipos y cada una de sus estadísticas, obteniendo el porcentaje de pases_bien realizados por cada jugadora
    for equipo in equipos:
        for estadistica in equipos[equipo]:
            estadistica['porcentaje'] = round(((estadistica['pases_bien'] / estadistica["cantidad_pases"]) * 100), 2)        
        # Y adicionalmente, ordenamos las estadísticas de cada jugadora por orden descendiente segun el procentaje de pases_bien
        ordeando_por_porcentaje = sorted(equipos[equipo], key=lambda x: x['porcentaje'], reverse=True)
        equipos[equipo] = ordeando_por_porcentaje

# Función inicial de ejecución del algoritmo
def contar_pases_y_efectividad():
    archivo_de_pases = open('./pases.txt', 'r')

    # Al abrir el archivo_de_pases, recorremos línea por línea
    for linea in archivo_de_pases:
        # Separando el registro del tipo 'Argentina;15;Agustina Albertario;0;53' por su ';'
        pase = linea.strip().split(';')
        # Verificamos que en su respectivo equipo (pase[0]) esté ya añadida la jugadora
        if not any(obj['nombre'] == pase[2] for obj in equipos[pase[0]]):
            # Si la jugadora no lo está, añadimos inicialmente un objeto con su número de camiseta (pase[1]) y su nombre (pase[2])
            # Y posteriormente añadimos los pases según corresponda.
            equipos[pase[0]].append({'numero': pase[1],'nombre': pase[2], 'cantidad_pases': 0, 'pases_bien': 0, 'pases_mal': 0, 'porcentaje': 0})
        
        # Para obtener el índice, enviamos el equipo al que pertenece (pase[0]) y el nombre de la jugadora (pase[2])
        indice = encontrar_indice_jugadora(pase[0], pase[2])
        
        # Adición del pase a la jugadora en su respectivo equipo
        # Le enviamos a que equipo corresponde, si el pase fue exitoso o no (pase[3] 0 o 1 convirtiéndolo a int) y el índice de la jugadora
        sumar_pase(pase[0], int(pase[3]), indice)

    ordenar_porcentualmente()

# Llamada inicial
contar_pases_y_efectividad()

print(equipos)