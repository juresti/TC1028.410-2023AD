def imprimePersonasWhile(lista):
    cont = 0
    limite = len(lista) - 1
    while (cont <= limite):
        print(lista[cont])
        cont += 1

def imprimePersonasForPos(lista):
    for pos in range(len(lista)):
        print(lista[pos])

def guardaNombreEdad(cuantas):
    lista = []
    for num in range(1,cuantas + 1):
        nombre = input(f"{num}. Dime el nombre: ")
        edad = int(input(f"{num}. Dime la edad: "))
        lista.append((nombre,edad))
    return lista
