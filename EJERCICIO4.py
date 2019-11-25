                             #En una empresa se requiere un sistema de información que registre sus nuevos usuarios. 
#Cada vez que un usuario se registra debe introducir los siguientes datos: documento, nombres, 
#apellidos, edad, peso, estatura. 
#Cree un sistema de información que reciba los datos de registro de cada cliente porteclado, 
#luego de realizado el registro el sistema debe mostrar al usuario el mensaje “Registro exitoso”.
#Si el usuario desea consultar su registro debe poder hacerlo a través de su documento. 

usuarios={}
preg12="SI"
ingr=1
cont=0

print("\nBienvenido!!! Nuestros Servicios son de Calidad")

while preg12=="SI":
    
    while ingr==1:
        print ("\nDigite Datos para Ingresar Nuevo Usuario \n")
    
        idPaciente = input ("Identificación >>  ")
        nombre= input("Nombre       >>  ")
        apellido= input("Apellido   >>  ")    
        edad= input("Edad       >>  ")
        peso=input("Peso        >>   ")
        talla= input("Talla     >>  ")
    
        print("\nRegistro exitoso!!!")
            
        ingr=int(input("\n1. Para Ingresar otro usuario\n2. Para Continuar      >>  "))
        
        usuarios[idPaciente] ={"nombre":nombre, "Apellido":apellido, "edad":edad, "peso":peso, "estatura":talla }
    
    menu=("\nDigite segun solicitud\n\n")
    menu+=("a. Para Imprimir Diccionario\n")
    menu+=("b. Para Consultar\n")
    menu+=("c. Para Continuar\n")
    
    print(menu)
    preg=(input("Digite >>>    "))    
           
    if preg=="a":
             
        for key in usuarios:                        #Forma correcta de imprimir diccionarios
            print (key, ":" ,usuarios[key])

    if preg== "b":
        idPaciente = input ("id para consultar >> ")
        
        consulta =usuarios[idPaciente]
        print("Paciente consultado >>>  ",consulta)
           
    preg12=(input("\nDigite SI para Reanudar Operación\nDigite NO para Salir    >>  ")).upper() 


    print("\nGRACIAS POR UTILIZAR NUESTROS SERVICIOS ")

