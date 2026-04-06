# Entrada dos 3 valores solicitados
op = int(input("Digite a opção (1 para Retângulo, 2 para Triângulo): "))
base = float(input("Digite o valor da base: "))
altura = float(input("Digite o valor da altura: "))

# Estrutura de Controle Condicional
if op == 1:
    area = base * altura
    print(f"A área do Retângulo é: {area:.2f}")
else:
    if op == 2:
        area = (base * altura) / 2
        print(f"A área do Triângulo é: {area:.2f}")
    else:
        print("Opção inválida! Use apenas 1 ou 2.")