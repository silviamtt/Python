while True:
    num = int(input("Digite um valor para a tabuada"))
    if num == 0:
        print("Programa encerrado. Bons estudos!")
        break
    Nmin = int(input("Digite o valor mínimo da tabuada"))
    Nmax = int(input("Digite o valor máximo da tabuada"))
    print("Tabuada do ", num, " de ", Nmin, " até ", Nmax)
    for i in range(Nmin, Nmax + 1):
        print(num, " x ", i, " = ", num * i)      
    print("Fim da tabuada")