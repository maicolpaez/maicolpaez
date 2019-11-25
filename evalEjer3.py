#Dada una lista, 
# a. usando ciclo for recorra la lista, imprimiendo cada uno de sus elementos
# b. usando ciclo while recorra la lista, imprimiendo cada uno de sus elementos

#
print("\nImpresiones con for\n")
numeros=[1,2,3,4,5,6,7,8,9,10]
for i in (numeros):
    print(i, end=(" | "))
#
print("\n\nImpresiones con for\n")
numeros=[1,2,3,4,5,6,7,8,9,10]
for i in range(len(numeros)):
    print(numeros[i], end=(" | "))
#
print("\n\nImpresiones con while\n")
numeros=[1,2,3,4,5,6,7,8,9,10]
i = 0
while i < (len(numeros)):
    print(numeros[i], end=(" | "))
    i += 1
#
print("\n\nPrograma terminado")