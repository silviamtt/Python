while True:
    # 1. Peça um número ao usuário
    try:
        numero = int(input("Digite um número para ver a tabuada: "))
    except ValueError:
        print("Por favor, digite um número inteiro válido.")
        continue

    # 2. Mostre a tabuada deste número
    print(f"\nTabuada do {numero}:")
    for i in range(1, 11):
        resultado = numero * i
        print(f"{numero} x {i} = {resultado}")
    
    # 3. Pergunte se o usuário deseja continuar
    # Usamos .strip().upper() para aceitar "s", "S", " sim " etc.
    continuar = input("\nDeseja exibir outra tabuada? (S/N): ").strip().upper()
    
    # 4 e 5. Verificação para continuar ou encerrar
    if continuar != "S" and continuar != "SIM":
        print("Programa encerrado. Bons estudos!")
        break