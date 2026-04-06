salario_atual = float(input("Digite o salário mensal atual: R$"))
percentual_reajuste = float(input("Digite o percentual de reajuste: "))

valor_aumento = salario_atual * (percentual_reajuste /100)
novo_salario = salario_atual + valor_aumento

print(f"O valor do aumento é: R$ {valor_aumento:.2f}") #usamos :.2f para formatar com duas casas decimais
print(f"O valor do novo salário é: R$ {novo_salario:.2f}")