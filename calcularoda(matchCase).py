from os import system

class calculadora:
    def __init__(self):
        pass

    def suma(self):
        system("cls")
        print("Sumar")
        num1 = float(input("Primer numero: "))
        num2 = float(input("Segundo numero: "))
        print("Total: ",num1+num2)

    def resta(self):
        system("cls")
        print("Restar")
        num1 = float(input("Primer numero: "))
        num2 = float(input("Segundo numero: "))
        print("Total: ",num1-num2)

    def multiplicar(self):
        system("cls")
        print("Multiplicar")
        num1 = float(input("Primer numero: "))
        num2 = float(input("Segundo numero: "))
        print("Total: ",num1*num2)

    def dividir(self):
        system("cls")
        print("Dividir")
        num1 = float(input("Primer numero: "))
        num2 = float(input("Segundo numero: "))
        print("Total: ",num1/num2)

    def potencia(self):
        system("cls")
        print("Potencia")
        num1 = float(input("Numero a Potenciar: "))
        num2 = float(input("Elevado a: "))
        print("Total: ",num1**num2)

system("cls")
CALC = calculadora()

respuesta = input("Calduladora Python\n\n¿Que desea Hacer?\nSumar: 1\nRestar: 2\nMultiplicar: 3\nDividir: 4\nPotenciar: 5\nSalir: Cualquier otra tecla\n\nSu Respuesta es: ")

while respuesta == "1" or respuesta=="2" or respuesta=="3" or respuesta=="4" or respuesta=="5":
    match respuesta:
        case "1":
            CALC.suma()
        case "2":  
            CALC.resta()
        case "3": 
            CALC.multiplicar()
        case "4":
            CALC.dividir()
        case "5":
            CALC.potencia()
    
    respuesta = input("\n¿Que desea Hacer?\nSumar: 1\nRestar: 2\nMultiplicar: 3\nDividir: 4\nPotenciar: 5\nSalir: Cualquier otra tecla\n\nSu Respuesta es: ")

if respuesta != "1" and respuesta !="2" and respuesta !="3" and respuesta !="4" and respuesta !="5":
    system("cls")
    print("Gracias por usar esta APP!")