#senha = int(input("Digite sua senha: "))

#if senha >= 0 and senha <= 10:
 #   print("número aceito")

#else:
 #  senha = int(input("Digite sua senha: "))


n = int(input("Digite um número entre 0 e 10: "))

while n < 0 or n > 10:
    print("Número inválido!")
    n = int(input("Digite um número entre 0 e 10"))

print("número aceito")