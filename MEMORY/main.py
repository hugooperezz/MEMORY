import random

def jugar():
    print("¡Bienvenido al juego MEMORY!")
    print("Pon a prueba tu memoria encontrando todas las parejas de cartas.")
    print("Elige el tamaño del tablero y empieza a jugar.")
    print("¡Buena suerte y que comience la diversión!")
    solicitar_tamaño_tablero()

def solicitar_tamaño_tablero():
    while True:
        filas = int(input("Ingrese el número de filas (entre 2 y 6): "))
        columnas = int(input("Ingrese el número de columnas (entre 2 y 6): "))
        if 2 <= filas <= 6 and 2 <= columnas <= 6:
            if (filas * columnas) % 2 == 0:
                crear_tablero(filas,columnas)
            else:
                print("El número total de posiciones debe ser par. Intente de nuevo.")
        else:
            print("Tamaño no válido. Elija un valor entre 2 y 6.")


def crear_tablero(filas, columnas):
    tablero = []
    for _ in range(filas):
        fila = []
        for _ in range(columnas):
            fila.append("X")
        tablero.append(fila)

    mostrar_tablero(tablero)

def mostrar_tablero(tablero):
    for fila in tablero:
        print(" ".join(fila))

# Inicia el juego
jugar()
