print ("***************MAYOR O MENOR DE EDAD***********************")
print ("FORO MAXIMO DE 10 PERSONAS!!!!!!!!!!!")
print ("INGRESANDO LA CANTIDAD DE PERSONAS PRESENTES")
cantidad = int(input("N° PERSONAS: "))
contador = 0
menor = 0
while cantidad > 10:
    print ("ERROR!!!!!!!!!")
    print ("CAPACIDAD MAXIMA DE 10 PERSONAS")
    cantidad = int(input("N° PERSONAS: "))
    
for i in range (1, cantidad +1):
    edad = int(input(f"Ingrese la edad de la persona {i}: "))
    if edad >= 18:
        print ("Es mayor de edad")
        contador = contador + 1
    else:
        print ("Es menor de edad")
        menor = menor + 1
        
   

print (f"Hay {contador} personas mayores de edad")
print (f"Hay {menor} personas menores de edad")
