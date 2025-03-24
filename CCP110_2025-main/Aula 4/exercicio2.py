a = int(input("Digite o valor de a: "))
b = int(input("Digite o valor de b: "))
c = int(input("Digite o valor de c: "))

if a > b and a > c:
    if (b > c):
        print(a, b, c)

    else:
        print(a, c, b)

elif b > a and b > c:
    if a > c:
        print(b, a, c)

    else:
        print(b, c, a)

elif c > a and c > b:
    if a > b:
        print(c, a, b)

    else:
        print(c, b, a)