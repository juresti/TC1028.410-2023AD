def cambiaE(pal):
    nueva = ""
    for letra in pal:
        if (letra == "e"):
            nueva += letra.upper()
        else:
            nueva += letra
    return nueva

def miSwap(pal):
    """Funcion que recibe una palabra y regresa otra
        en donde las minusculas fueron cambiadas por
        mayusculas y viceverza"""
    pass

def listaPersonas(numPer):
    lista = []
    for num in range(1,numPer + 1):
        nombre = input(f"Dime el nombre de la persona {num}: ")
        lista += [nombre] #lista.append(nombre)
    return lista
