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

def mismoTamano(mat1,mat2):
    nr1,nc1 = tamanoMatriz(mat1)
    nr2,nc2 = tamanoMatriz(mat2)
    
    bandera = True
    if (nr1 != nr2):
        print("Son diferentes en el numero de renglones")
        bandera = False
    if (nc1 != nc2):
        print("Son diferentes en el numero de columnas")
        bandera = False
    if (-1 in [nr1,nr2,nc1,nc2]):
        print("Error en alguna de las matrices")
        bandera = False
    return bandera

    