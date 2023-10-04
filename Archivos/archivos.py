import os

print(os.getcwd())
os.chdir("C:\\Users\\L00423103\\OneDrive - Instituto Tecnologico y de Estudios Superiores de Monterrey\\Desktop")
print(os.getcwd())
print(os.listdir("."))

def imprimeArchivo(nombre):
    with open(nombre + ".txt","r") as miArchivo:
        for linea in miArchivo:
            print(linea)

def leeArchivo(nombre):
    with open(nombre + ".txt","r") as miArchivo:
        info = miArchivo.readlines()
    return info



imprimeArchivo("prueba")

def guardaEnArchivo(nombre):
    with open(nombre + ".txt","w") as miArchivo:
        miArchivo.write("Algo\n")
        miArchivo.write("Esta otra linea\n")
        miArchivo.writelines(["linea 3\n","linea 4\n"])
        