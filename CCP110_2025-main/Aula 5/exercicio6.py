contador = 0 
somador = 0
while True:
    n = int(input("Digite um numero ou 0 para parar: "))
    if n == 0:
        break
    contador = contador + 1
    somador = somador + n 

print(f"Numeros digitados: {contador}")
print(f"Soma dos numeros: {somador}")
print(f"Media dos numeros: {somador/contador:.2f}")