ano = int(input("Insira o ano atual: "))
nasc = int(input("Insira seu ano de nascimento: "))
idade = ano - nasc

if idade >= 18:
    print("Você pode tirar CNH!")
