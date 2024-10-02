import math

numero = 29 
primo = True

if numero <= 1:
    primo = False
else:
    divisor = 2
    while divisor <= math.isqrt(numero):
        if numero % divisor == 0:
            primo = False
            break
        divisor += 1

if primo:
    print(f"{numero} é um número primo.")
else:
    print(f"{numero} não é um número primo.")
