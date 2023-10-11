def creaMatriz(numRen,numCol):
    matriz = []
    for _ in range(numRen):
        renglon = ["."] * numCol
        matriz.append(renglon)
    return matriz

def imprimeMatriz(matriz):
    for renglon in matriz:
        linea = ""
        for dato in renglon:
            linea += dato + " "
        print(linea)

def preguntaUsuario(tablero):
    print("\n Aqui esta el tablero")
    imprimeMatriz(tablero)
    ren = int(input("\nEn que renglon quieres tirar? "))
    col = int(input("En que columna quieres tirar? "))
    return ren,col

def anotarTiro(ren,col,ficha,tablero):
    tablero[ren][col] = ficha
    return tablero

def gato():
    print("Vamos a empezar el juego de gato!!! \n")
    tablero = creaMatriz(3,3)
    imprimeMatriz(tablero)
    
    for num in range(9):
        ren,col = preguntaUsuario(tablero)
        if (num % 2 == 0):
            anotarTiro(ren,col,"O",tablero)
        else:
            anotarTiro(ren,col,"X",tablero)
    
gato()
    