from boneback import *

user = True
li = LinkedList()
queue = Queue()
hist = Stack()

while user == True:
    print("1. Agregar")
    print("2. Eliminar")
    print("3. Comprar")
    print("4. Vender")
    print("5. Buscar elemento")
    print("6. Mostrar elementos")
    print("Inserte operacion a realizar: ", end='')
    op = int(input())
    hist.push(op)

    try:
        Operation(op, li)
    except:
        print("Error, no ha ingresado un numero")
    print("Si desea realizar otra operacion, ingrese 1, para salir presione otro numero")
    program = int(input())
    if program != 1:
        user = False
print("Programa finalizado")

print("Usted Ingreso los siguientes elementos:")
if hist.isEmpty():
    print("No ingreso ninguna operacion.")
else:
    for i in range(hist.size()):
        if i == 1:
            print("1. Agregar")
        elif i == 2:
            print("2. Eliminar")
        elif i == 3:
            print("3. Comprar")
        elif i == 4:
            print("4. Vender")
        elif i == 5:
            print("5. Buscar elemento")
        elif i == 6:
            print("6. Mostrar elementos")
