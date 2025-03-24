maior = 0 
for x in range(6):
    n = int(input("Digite seis números: "))
    if n > maior:
        maior = n

print("Maior número digitado: ", maior)