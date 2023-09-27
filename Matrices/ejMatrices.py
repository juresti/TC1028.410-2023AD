def crearMatrizCeros(numRen,numCol):
    matriz = []
    for ren in range(numRen):
        renglon = [0] * numCol
        matriz.append(renglon)
    return matriz
        
def imprimirMatriz(matriz):
    for renglon in matriz:
        salida = ""
        for valor in renglon:
            salida += str(valor) + " "
        print(salida)
        
def tamanoMatriz(matriz):
    numRen = len(matriz)
    numCol = len(matriz[0])
    
    for renglon in matriz:
        if (len(renglon) != numCol):
            print("Los renglones deben de tener la misma cantidad de elementos")
            return -1,-1
    return numRen,numCol
