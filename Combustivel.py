# Leitura dos dados de entrada
preco_litro = float(input("Digite o preço do litro do combustível: R$ "))
desempenho = float(input("Digite o desempenho do veículo (km/l): "))
distancia = float(input("Digite a distância entre as cidades (km): "))

# Processamento dos cálculos
litros_gastos = distancia / desempenho
custo_total = litros_gastos * preco_litro

# Exibição dos resultados
print(f"\n--- Resumo da Viagem ---")
print(f"Total de combustível gasto: {litros_gastos:.2f} litros")
print(f"Custo total da viagem: R$ {custo_total:.2f}")