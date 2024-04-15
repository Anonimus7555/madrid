print("*****INFORMACION DEL COMPRADOR*****")
nombre = input("Ingrese sus nombres completos: ")
apellido = input("Ingrese sus apellidos completos: ")
edad = int(input("Ingrese su edad: "))
genero = input("Ingrese a que genero pertenece: ")
correo = input("Ingrese su correo: ")

print("Cargando datos.............")

for i in range(0, 6):
    print(i)
    
diccionario={
    "nombre" : nombre,
    "apellido" : apellido,
    "edad" : edad,
    "género" : genero,
    "correo" : correo    
}
print(diccionario)

print("Ingrese la cantidad de cuotas pendientes a pagar!!!!!!")
cuotas = int(input("Cantidad de cuotas a pagar: "))
while(cuotas > 6):
    print("Valor ingresado erroneo!!!!")
    cuotas = int(input("Cantidad de cuotas a pagar: "))
  
for i in range(1, cuotas + 1):
    pago = int(input(f"Monto de la cuota {i}: "))