def jugar ():
    print("¡Bienvenido al juego MEMORY!")
    print("Pon a prueba tu memoria encontrando todas las parejas de cartas.")
    print("Elige el tamaño del tablero y empieza a jugar.")
    print("¡Buena suerte y que comience la diversión!")
    filas = int(input("Introduce las filas del tablero: "))
    columnas = int(input("Introduce las columnas del tablero: "))
    crear_tablero(filas,columnas)


#Metodo para crear el tablero
def crear_tablero (filas, columnas):
    #Identifico que las medidas introducidas para crear el tablero son correctas
    if filas * columnas % 2 != 0:
        print("Error: no se puede realizar este tablero con las medidas introducidas")
    else:
        #Bucle for para crear el tablero
        tablero = []
        for _ in range(filas):
            fila = ["*"] * columnas
            tablero.append(fila)

#Metodo para mostrar el tablero
def mostrar_tablero(tablero):
    for fila in tablero:
        print("* " * len(fila))

jugar()