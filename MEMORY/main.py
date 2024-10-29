import random

#Metodo jugar que se encarga de desplegar el menu de biemvenida
def jugar():
    print("¡Bienvenido al juego MEMORY!")
    print("Pon a prueba tu memoria encontrando todas las parejas de cartas.")
    print("Elige el tamaño del tablero y empieza a jugar.")
    print("¡Buena suerte y que comience la diversión!")
    solicitar_tamaño_tablero()

#Metodo para comprobar que los tamaños son los correctos
def solicitar_tamaño_tablero():
    while True:
        filas = int(input("Ingrese el número de filas (entre 2 y 6): "))
        columnas = int(input("Ingrese el número de columnas (entre 2 y 6): "))
        if 2 <= filas <= 6 and 2 <= columnas <= 5:
            if (filas * columnas) % 2 == 0:
                crear_tablero_oculto(filas, columnas)
                crear_tablero_no_ocultar(filas,columnas)
                break
            else:
                print("El número total de posiciones debe ser par. Intente de nuevo.")
        else:
            print("Tamaño no válido. Elija un valor entre 2 y 6.")

#Metodo que se encarga dde crear y mostrar un tablero con emojis simulando que las cartas estan boca abajo
def crear_tablero_oculto(filas, columnas):
    tablero = []
    emoji = "⬜"
    
    print("\nTabla de resultados:")
    for i in range(filas):
        tablero = [emoji] * columnas 
        print(" ".join(tablero))  
        
#Metodo para crear el tablero desordenado con emojis
def crear_tablero_no_ocultar(filas, columnas):
    # Lista de emojis
    emojis = ["🐶", "🐱", "🐭", "🐹", "🐰", "🦊", "🐻", "🐼", "🐨", "🐯", "🦁", "🐮", "🐷", "🐸", "🐵"]
    
    # Número de parejas necesarias
    num_pares = (filas * columnas) // 2
    
    # Crear una lista de cartas con pares de emojis
    cartas = (emojis[:num_pares] * 2)  # Duplicar los emojis para crear pares
    random.shuffle(cartas)  # Mezclar las cartas aleatoriamente

    # Imprimir el tablero
    print("\nTablero de resultados:")
    for i in range(filas):
        fila = cartas[i * columnas:(i + 1) * columnas]  
        print(" ".join(fila)) 

#Inicio del juego
jugar()