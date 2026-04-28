Nmin = int(input("Digite o valor mínimo"))
Nmax = int(input("Digite o valor máximo"))
for i in range(Nmin, Nmax + 1):
    resto = i % 2
    if resto == 0:
        print(i, " é par")
    else:
        print(i, " é ímpar")
print("Programa encerrado. Bons estudos!")

 