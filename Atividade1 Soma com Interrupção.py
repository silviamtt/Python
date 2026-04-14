soma = 0

while True:
    numero = float(input("Digite um número (ou 0 para sair): "))
    
    # Verifica se o usuário digitou 0 para interromper o laço
    if numero == 0:
        break
    
    soma += numero

print(f"A soma total dos números inseridos é: {soma}")