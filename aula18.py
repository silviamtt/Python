# 1. Capacidade do elevador
capacidade = float(input("Digite a capacidade máxima do elevador (kg): "))

# 2. Leitura do peso das 5 pessoas
p1 = float(input("Peso da pessoa 1: "))
p2 = float(input("Peso da pessoa 2: "))
p3 = float(input("Peso da pessoa 3: "))
p4 = float(input("Peso da pessoa 4: "))
p5 = float(input("Peso da pessoa 5: "))

# 3. Cálculo do peso total
peso_total = p1 + p2 + p3 + p4 + p5

# 4. Verificação
if peso_total <= capacidade:
    print(f"Peso total: {peso_total}kg. O elevador está LIBERADO para subir.")
else:
    print(f"Peso total: {peso_total}kg. Carga máxima EXCEDIDA!")