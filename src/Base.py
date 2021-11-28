from boneback import *

user = True
li = LinkedList()
queue = Queue()
stack = Stack()

while user == True:
    print("1 agregar")
    print("2 eliminar")
    print("3 comprar")
    print("4 vender")   
    print("5 buscar elemento")
    print("6 mostrar elementos")
    print("Inserte operacion a realizar")
    op = input()
    if op.isnumeric() == True:
        op = int(op)
        Operation(op,li)  
    else:          
        print("Error, no ha ingresado un numero")     
    print("Si desea realizar otra operacion, ingrese 1, para salir presione otro numero")       
    program = int(input())
    if program != 1:
        user = False
print("Programa finalizado") 