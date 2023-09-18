def cuentaRango4en4(inicio,fin):
    for num in range(inicio,fin+1,4):
        print(num)

def cuentaRangoDiv7(inicio,fin):
    contador = 0
    for num in range(fin,inicio-1,-1):
        res = num % 7
        if (res == 0):
            contador += 1
            print(num)
    return contador

def main():
    print("Vamos a contar para atras y te digo divisibles entre 7")
    inicio = int(input("Dime en donde inicia el rango: "))
    fin = int(input("Dime donde termina el rango: "))
    cuantos = cuentaRangoDiv7(inicio,fin)
    print(f"Fueron {cuantos} divisibles entre 7")

def quieresContinuar():
    opcion = input("Dime si quieres continuar (si/no): ")
    while (opcion.lower() != "si"):
        print(f"Me dijiste: {opcion}")
        opcion = input("Dime si quieres continuar (si/no): ")
    print("ya me dijo que si")
