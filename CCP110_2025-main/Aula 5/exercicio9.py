while True:
    n = int(input("Digite um numero positivo: "))
    if n > 0:
        break

soma = 0 
for x in range (1, n + 1):
    soma = soma + 1 / x
    print(f"1/{x} = {1 / x:.2f} - Soma: {soma:.2f}")

print(f"Soma: {soma:.2f}")