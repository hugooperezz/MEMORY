import random

# Método jugar que se encarga de desplegar el menú de bienvenida
def jugar():
    print("¡Bienvenido al juego MEMORY!")
    print("Pon a prueba tu memoria encontrando todas las parejas de cartas.")
    print("Elige el tamaño del tablero y empieza a jugar.")
    print("¡Buena suerte y que comience la diversión!")
    menu()

# Menú de selección de modo de juego
def menu():
    opcion = int(input("\nElige el modo de juego \n1-Persona VS Persona \n2-Persona VS Maquina \n3-Maquina VS Maquina\n"))
    match opcion:
        case 1:
            solicitar_tamaño_tablero(opcion)
        case 2:
            solicitar_tamaño_tablero(opcion)
        case 3:
            solicitar_tamaño_tablero(opcion)
        case _:
            print("Error: Opción no reconocida")

# Método para solicitar el tamaño del tablero y validar los valores
def solicitar_tamaño_tablero(opcion):
    while True:
        filas = int(input("Ingrese el número de filas (entre 2 y 6): "))
        columnas = int(input("Ingrese el número de columnas (entre 2 y 6): "))
        if 2 <= filas <= 6 and 2 <= columnas <= 5:
            if (filas * columnas) % 2 == 0:
                tablero_real = crear_tablero_no_ocultar(filas, columnas)
                tablero_oculto = crear_tablero_oculto(filas, columnas)
                match opcion:
                    case 1:
                        PersonaVSPersona(tablero_real, tablero_oculto, filas, columnas)
                    case 2:
                        PersonaVSMaquina(tablero_real, tablero_oculto, filas, columnas)
                    case 3:
                        MaquinaVSMaquina(tablero_real, tablero_oculto, filas, columnas)
                    case _:
                        print("Error: Opción no reconocida")
                
                break
            else:
                print("Error: El número total de posiciones debe ser par. Intente de nuevo.")
        else:
            print("Error: Tamaño no válido. Elija un valor entre 2 y 6.")

# Método que crea un tablero oculto con emojis para simular las cartas boca abajo
def crear_tablero_oculto(filas, columnas):
    tablero = [["⬜" for _ in range(columnas)] for _ in range(filas)]
    print("\nTabla de resultados (oculto):")
    for fila in tablero:
        print(" ".join(fila))
    return tablero

# Método para crear el tablero desordenado con emojis (tablero real)
def crear_tablero_no_ocultar(filas, columnas):
    emojis = ["🐶", "🐱", "🐭", "🐹", "🐰", "🦊", "🐻", "🐼", "🐨", "🐯", "🦁", "🐮", "🐷", "🐸", "🐵"]
    num_pares = (filas * columnas) // 2
    cartas = emojis[:num_pares] * 2
    random.shuffle(cartas)
    tablero_real = [cartas[i * columnas:(i + 1) * columnas] for i in range(filas)]
    print("\nTablero de resultados (real):")
    for fila in tablero_real:
        print(" ".join(fila))
    return tablero_real

# Método que verifica si todas las parejas han sido encontradas
def todas_las_parejas_encontradas(tablero_oculto):
    for fila in tablero_oculto:
        if "⬜" in fila:
            return False
    return True

# Método para mostrar el tablero actual
def mostrar_tablero(tablero):
    for fila in tablero:
        print(" ".join(fila))
        
# Método para iniciar la partida en modo Persona vs Persona
def PersonaVSPersona(tablero_real, tablero_oculto, filas, columnas):
    jugadores = ["Jugador 1", "Jugador 2"]
    puntajes = {jugadores[0]: 0, jugadores[1]: 0}
    turno = 0  # 0 para Jugador 1, 1 para Jugador 2

    while not todas_las_parejas_encontradas(tablero_oculto):
        print("\n")
        print("\n")
        print("\nTablero actual:")
        mostrar_tablero(tablero_oculto)
        
        print(f"\nTurno de {jugadores[turno]}")
        condicion = True
        while condicion:
            fila1, col1 = solicitar_coordenadas(filas, columnas, tablero_oculto)
            fila2, col2 = solicitar_coordenadas(filas, columnas, tablero_oculto)
            if (fila1 == fila2 and col1 == col2):
                print("Error: No puedes seleccionar dos veces la misma carta.")
            else:
                condicion = False
        
        # Mostrar temporalmente las cartas seleccionadas
        tablero_oculto[fila1][col1] = tablero_real[fila1][col1]
        tablero_oculto[fila2][col2] = tablero_real[fila2][col2]
        mostrar_tablero(tablero_oculto)

        if tablero_real[fila1][col1] == tablero_real[fila2][col2]:
            print("¡Encontraste una pareja!")
            puntajes[jugadores[turno]] += 2
        else:
            print("No es una pareja. Las cartas se ocultan de nuevo.")
            tablero_oculto[fila1][col1] = "⬜"
            tablero_oculto[fila2][col2] = "⬜"
            turno = 1 - turno  # Cambia el turno

    mostrar_resultados_finales_PersonaVSPersona(puntajes)

# Método para solicitar las coordenadas de las cartas
def solicitar_coordenadas(filas, columnas, tablero_oculto, es_maquina = False):
    if es_maquina:
        while True:
            fila = random.randint(0,filas - 1)
            col = random.randint(0, columnas - 1)
            if tablero_oculto[fila][col] == "⬜":
                return fila, col
    else:
        while True:
            fila = int(input(f"Selecciona la fila (0 a {filas - 1}): "))
            col = int(input(f"Selecciona la columna (0 a {columnas - 1}): "))
            if 0 <= fila < filas and 0 <= col < columnas and tablero_oculto[fila][col] == "⬜":
                return fila, col
            else:
                print("Coordenadas no válidas o carta ya descubierta. Intente de nuevo.")

# Método para mostrar los resultados finales
def mostrar_resultados_finales_PersonaVSPersona(puntajes):
    print("\n¡Juego terminado!")
    print("Puntajes finales:")
    for jugador, puntaje in puntajes.items():
        print(f"{jugador}: {puntaje} puntos")
    if puntajes["Jugador 1"] > puntajes["Jugador 2"]:
        print("¡Jugador 1 gana!")
    elif puntajes["Jugador 1"] < puntajes["Jugador 2"]:
        print("¡Jugador 2 gana!")
    else:
        print("¡Es un empate!")

#Metodo PersonaVSMaquina
def PersonaVSMaquina(tablero_real, tablero_oculto, filas, columnas):
    jugadores = ["Jugador 1", "Maquina"]
    puntajes = {jugadores[0]: 0, jugadores[1]: 0}
    turno = 0  # 0 para Jugador 1, 1 para la Maquina

    while not todas_las_parejas_encontradas(tablero_oculto):
        print("\nTablero actual:")
        mostrar_tablero(tablero_oculto)
        
        print(f"\nTurno de {jugadores[turno]}")
        # Determina si el turno es del jugador humano o de la máquina
        es_maquina = (turno == 1)

        condicion = True
        while condicion:
            fila1, col1 = solicitar_coordenadas(filas, columnas, tablero_oculto, es_maquina)
            fila2, col2 = solicitar_coordenadas(filas, columnas, tablero_oculto, es_maquina)
            if (fila1 == fila2 and col1 == col2):
                print("Error: No puedes seleccionar dos veces la misma carta.")
            else:
                condicion = False
        
        # Mostrar temporalmente las cartas seleccionadas
        tablero_oculto[fila1][col1] = tablero_real[fila1][col1]
        tablero_oculto[fila2][col2] = tablero_real[fila2][col2]
        mostrar_tablero(tablero_oculto)

        if tablero_real[fila1][col1] == tablero_real[fila2][col2]:
            print("¡Encontraste una pareja!")
            puntajes[jugadores[turno]] += 2
        else:
            print("No es una pareja. Las cartas se ocultan de nuevo.")
            tablero_oculto[fila1][col1] = "⬜"
            tablero_oculto[fila2][col2] = "⬜"
            turno = 1 - turno  # Cambia el turno

    mostrar_resultados_finales_PersonaVSMaquina(puntajes)

# Método para mostrar los resultados finales del modo PersonaVSMaquina
def mostrar_resultados_finales_PersonaVSMaquina(puntajes):
    print("\n¡Juego terminado!")
    print("Puntajes finales:")
    for jugador, puntaje in puntajes.items():
        print(f"{jugador}: {puntaje} puntos")
    if puntajes["Jugador 1"] > puntajes["Maquina"]:
        print("¡Jugador 1 gana!")
    elif puntajes["Jugador 1"] < puntajes["Maquina"]:
        print("¡Maquina gana!")
    else:
        print("¡Es un empate!")

#Metodo de MaquinaVSMaquina
def MaquinaVSMaquina (tablero_real, tablero_oculto, filas, columnas):
    jugadores = ["Maquina 1", "Maquina 2"]
    puntajes = {jugadores[0]: 0, jugadores[1]: 0}
    turno = 0  # 0 para Jugador 1, 1 para la Maquina

    while not todas_las_parejas_encontradas(tablero_oculto):
        print("\nTablero actual:")
        mostrar_tablero(tablero_oculto)
        
        print(f"\nTurno de {jugadores[turno]}")

        condicion = True
        while condicion:
            fila1, col1 = solicitar_coordenadas_MaquinaVSMaquina(filas, columnas, tablero_oculto)
            fila2, col2 = solicitar_coordenadas_MaquinaVSMaquina(filas, columnas, tablero_oculto)
            if (fila1 == fila2 and col1 == col2):
                print("Error: No puedes seleccionar dos veces la misma carta.")
            else:
                condicion = False
        
        # Mostrar temporalmente las cartas seleccionadas
        tablero_oculto[fila1][col1] = tablero_real[fila1][col1]
        tablero_oculto[fila2][col2] = tablero_real[fila2][col2]
        mostrar_tablero(tablero_oculto)

        if tablero_real[fila1][col1] == tablero_real[fila2][col2]:
            print("¡Encontraste una pareja!")
            puntajes[jugadores[turno]] += 2
        else:
            print("No es una pareja. Las cartas se ocultan de nuevo.")
            tablero_oculto[fila1][col1] = "⬜"
            tablero_oculto[fila2][col2] = "⬜"
            turno = 1 - turno  # Cambia el turno

    mostrar_resultados_finales_MaquinaVSMaquina(puntajes)

#Metodo que introduce las cordenadas random para las 2 maquinas
def solicitar_coordenadas_MaquinaVSMaquina(filas, columnas, tablero_oculto):
    while True:
        fila = random.randint(0,filas - 1)
        col = random.randint(0, columnas - 1)
        if tablero_oculto[fila][col] == "⬜":
            return fila, col

# Método para mostrar los resultados finales del modo PersonaVSMaquina
def mostrar_resultados_finales_MaquinaVSMaquina(puntajes):
    print("\n¡Juego terminado!")
    print("Puntajes finales:")
    for jugador, puntaje in puntajes.items():
        print(f"{jugador}: {puntaje} puntos")
    if puntajes["Maquina 1"] > puntajes["Maquina 2"]:
        print("Maquina 1 gana!")
    elif puntajes["Maquina 1"] < puntajes["Maquina 2"]:
        print("¡Maquina 2 gana!")
    else:
        print("¡Es un empate!")
# Inicio del juego
jugar()
