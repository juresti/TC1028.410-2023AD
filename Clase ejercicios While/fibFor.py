def fibonacci(k):
    if (k < 1):
        return "Error. Valores deben de ser mayores a 0."
    else:
        if (k == 1) or (k == 2):
            return 1
        else:
            veces = k - 2
            pen = 1
            ult = 1
            for num in range(veces):
                nuevo = ult + pen
                pen = ult
                ult = nuevo
            return nuevo
def suma2(uno,dos):
    return uno + dos

def main():
    opcion = int(input("Dime que ejercicio quieres correr: "))
    if (opcion == 1):
        #Ejercicio 1
        print("Ejercicio 1")
        k = int(input("Dime el valor de k: "))
        res = fibonacci(k)
        print(f"El resultado fue {res}")
    elif (opcion == 2):
        #Ejercicio 2
        print("Ejercicio 2")
        var1 = int(input("Dime el primer valor: "))
        var2 = int(input("Dime el segundo valor: "))
        res = suma2(var1, var2)
        print(f"La suma es {res}")
    else:
        print("Opcion no valida")
