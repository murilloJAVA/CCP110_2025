ultimo = int(input("Digite o último digito da contagem: \n"))

x = 0
while x <= ultimo:
    if x % 2 == 1:
        print(x)
    x = x + 1