numero = int(input("Numero factorial: "))
acumulador = 1
res = 1

for i in range(1, numero + 1):
    res = res * i
    #acumulador = acumulador + res
    
print(res)
   
    
