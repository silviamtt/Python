# Leitura dos dados de entrada
salario_atual = float(input("Digite o salário mensal atual: R$ "))
percentual_reajuste = float(input("Digite o percentual de reajuste (ex: 10 para 10%): "))

# Cálculo do novo salário
reajuste = salario_atual * (percentual_reajuste / 100)
novo_salario = salario_atual + reajuste

# Exibição do resultado
print(f"\nO valor do reajuste é: R$ {reajuste:.2f}")
print(f"O novo salário é: R$ {novo_salario:.2f}")