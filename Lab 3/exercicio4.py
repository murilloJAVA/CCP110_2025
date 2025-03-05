codigo = int(input("Digite o código do produto:"))
quant = int(input("Digite a quantidade do produto:"))

if codigo == 1:
    result1 = 6 * quant
    print(f"Total: R$ {result1:.2f}")

elif codigo == 2:
    result2 = 6.5 * quant
    print(f"Total: R$ {result2:.2f}")

elif codigo == 3:
    result3 = 5 * quant
    print(f"Total: R$ {result3:.2f}")

elif codigo == 4:
    result4 = 3 * quant
    print(f"Total: R$ {result4:.2f}")

elif codigo == 5:
    result5 = 2 * quant
    print(f"Total: R$ {result5:.2f}")


