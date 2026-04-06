print("--- Calculadora de Volume ---")
print("1 - Lata de Óleo (Cilíndrica)")
print("2 - Caixa de Papelão (Retangular)")

opcao = input("Escolha a opção (1 ou 2): ")

if opcao == "1":
    raio = float(input("Digite o raio da lata: "))
    altura = float(input("Digite a altura da lata: "))
    volume = 3.14159 * (raio ** 2) * altura
    print(f"O volume da lata de óleo é: {volume:.2f}")

else:
    if opcao == "2":
        altura = float(input("Digite a altura da caixa: "))
        largura = float(input("Digite a largura da caixa: "))
        comprimento = float(input("Digite o comprimento da caixa: "))
        volume = altura * largura * comprimento
        print(f"O volume da caixa de papelão é: {volume:.2f}")
    else:
        print("Opção inválida!")