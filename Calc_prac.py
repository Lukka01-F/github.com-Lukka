def calculadora(num1, num2, operador):
    respuesta = ""
    while respuesta != "salir":

        
        numero= int(input("Introduce el primer número: "))
        print("----------------------------------------------------------------------")
        calc=input("Introduce la operacion que deseas realizar(+, -, *, /): ")
        print("----------------------------------------------------------------------")
        numero2= int(input("Introduce el segundo número: "))
        print("----------------------------------------------------------------------")
        if calc == "+":
            resultado = numero + numero2
            print(resultado)
        elif calc == "-":
            resultado = numero- numero2
            print(resultado)
        elif calc == "*":
            resultado = numero * numero2
            print(resultado)
        elif calc == "/":
            if numero2 == 0:
                print("No se puede dividir por cero")
            elif numero == 0:
                print("No se puede dividir por cero")
            else:
                resultado= numero/ numero2
                print(resultado)
        else:
            print("operacion no valida")
            break
        print("----------------------------------------------------------------------")    
        respuesta = input(" desea continuar o salir : ")
        print("----------------------------------------------------------------------")
    print("Calculo terminado")
if __name__ == "__main__":
    calculadora(10, 5, "+")