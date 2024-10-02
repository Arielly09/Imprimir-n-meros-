numero = 12345 
contador = 0

if numero < 0:
    numero = -numero

while numero > 0:
    numero //= 10  
    contador += 1  

print("O número de dígitos é:", contador)
