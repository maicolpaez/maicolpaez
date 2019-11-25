#Cree una función que reciba el nombre de una persona como argumento y retorne el número de sus letras, halla llamado a lafunciñon y guarde su valor de retorno en una variable he imprima el valor por consola.

cont=0
print()
def recorre_nombre (nombre):
    for i in range(len(nombre)):
        print(nombre[i], end = (" | "))
    
        cont=i + 1
    print("\n")
    return cont;
         
nombre1=input("Digite nombre >>  ")

print (recorre_nombre(nombre1))
