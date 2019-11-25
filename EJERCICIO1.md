#Cree una función que reciba como argumentos dos números y retorne el mayor de estos números, luego haga el llamadoa la función y guarde su valor de retorno en una variable e imprima ese valor porconsola 

def numero_mayor (num1, num2):
    if num1>num2:
        may1=num1
        return may1
    elif num2>num1:
        may2=num2
        return may2
    elif num2==num1:
        return False
numero1 = int (input("\nIgrese Nº 1 >> "))
numero2 = int (input("Igrese Nº 2 >> ")) 
aux = (numero_mayor(numero1, numero2))
if aux:
    print(aux)
else:
    print("no hay mayor")
