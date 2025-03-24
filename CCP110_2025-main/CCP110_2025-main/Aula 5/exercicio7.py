contador = 0 
somador = 0
while True:
    n = int(input("Digite 10 números: "))
    if n >= 10:
        break
    contador = contador + 1
    somador = somador + n 

print(f"Numeros digitados: {contador}")
print(f"Soma dos numeros: {somador}")


