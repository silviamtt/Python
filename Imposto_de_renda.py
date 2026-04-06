print("CALCULADORA DE IRRF 2026")
salario = float(input("Digite o valor do salário mensal bruto (R$): "))

# 1. Determinar a alíquota base e a dedução usando a Tabela Progressiva
if salario <= 2428.80:
    aliquota = 0.0
    deducao = 0.0
elif salario <= 2826.65:
    aliquota = 7.5
    deducao = 182.16
elif salario <= 3751.05:
    aliquota = 15.0
    deducao = 394.16
elif salario <= 4664.68:
    aliquota = 22.5
    deducao = 675.49
else:
    aliquota = 27.5
    deducao = 908.73

imposto_base = (salario * (aliquota / 100)) - deducao

# Se o imposto base for negativo, arredonda para zero
if imposto_base < 0:
    imposto_base = 0.0

# 2. Aplicar a Nova Regra de Isenção (Lei vigente para 2026)
if salario <= 5000.00:
    imposto_final = 0.0
    explicacao = "Isento (Nova regra de isenção até R$ 5.000)"
elif salario <= 7350.00:
    # Aplica o redutor linear oficial estipulado pelo governo para a faixa de transição
    reducao = 978.62 - (0.133145 * salario)
    imposto_final = imposto_base - reducao
    
    # Impede que a redução gere um imposto negativo
    if imposto_final < 0:
        imposto_final = 0.0
        
    explicacao = f"Tributado na fonte (Com redução extra de R$ {reducao:.2f})"
else:
    imposto_final = imposto_base
    explicacao = "Tributado na fonte (Sem redução extra, tabela padrão)"

salario_liquido = salario - imposto_final

# 3. Exibir os resultados formatados
print("RESULTADO FINAL")
print(f"Salário Bruto: R$ {salario:.2f}")
print(f"Alíquota Base Aplicada: {aliquota}%")
print(f"Situação: {explicacao}")
print(f"Valor Exato do Desconto (IRRF): R$ {imposto_final:.2f}")
print(f"Salário Líquido Final: R$ {salario_liquido:.2f}")
