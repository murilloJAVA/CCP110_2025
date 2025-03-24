prod1 = float(input("Digite o valor do primeiro produto: "))
prod2 = float(input("Digite o valor do segundo produto: "))
prod3 = float(input("Digite o valor do terceiro produto: "))
valor = (prod1 + prod2 + prod3)
total1 = 20
total2 = 10

if (valor) >= 500:
    result = (total1 / 100) * valor  
    print(f"Desconto: {result:.2f}")

elif (valor) < 500:
    result = (total2 / 100) * valor
    print(f"Desconto: {result:.2f}")

