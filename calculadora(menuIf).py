from os import system

#Calculadora Basica
class clcd:
    def __init__(self):
        pass

    def suma(self):
        print("Suma\n")
        numero1=int(input("Primer Numero: "))
        numero2=int(input("Segundo Numeor: "))
        numero3=numero1+numero2
        print("Total: ",numero3)
    
    def resta(self):
        print("Resta\n")
        numero1=int(input("Primer Numero: "))
        numero2=int(input("Segundo Numeor: "))
        numero3=numero1-numero2
        print("Total: ",numero3)

    def multiplicar(self):
        print("Multiplicacion\n")
        numero1=int(input("Primer Numero: "))
        numero2=int(input("Segundo Numeor: "))
        numero3=numero1*numero2
        print("Total: ",numero3)

    def dividir (self):
        print("Divicion\n")
        numero1=int(input("Primer Numero: "))
        numero2=int(input("Segundo Numeor: "))
        numero3=numero1/numero2
        print("Total: ",numero3)


opcion=int(input("\n\nPara sumar ingresa 1\nPara restar ingresa 2\nPara multiplicar ingresa 3\nPara Dividir ingresa 4\nCualquier otra tecla para salir\n"))
CLCD = clcd()
if opcion== int(1):
    system("cls")
    CLCD.suma()
elif opcion ==int(2):
    system("cls")
    CLCD.resta()
elif opcion ==int(3):
    system("cls")
    CLCD.multiplicar()
elif opcion ==int(4):
    system("cls")
    CLCD.dividir()
