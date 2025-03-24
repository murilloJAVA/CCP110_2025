codigo = int(input("Digite o codigo de origem desse produto: "))

if codigo == 1:
    print("Produto do Sul")

elif codigo == 2:
    print("Produto do Norte")

elif codigo == 3:
    print("Produto do Leste")

elif codigo == 4:
    print("Produto do Oeste") 

elif codigo == 5 or codigo == 6:
    print("Produto do Nordeste")

elif codigo >= 7 and codigo <= 9:
    print("Produto do Sudeste")

elif codigo >=10 and codigo <=20:
    print("Produto do Centro-Oeste")

elif codigo >=25 and codigo <= 30:
    print("Produto do Nordeste")