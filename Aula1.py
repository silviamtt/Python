

#nome = "Jonas"
#idade = 22
#valor = 51.34
#print(nome, "de", idade, "anos", "tem R$", valor)

nome = str(input("informe seu nome:"))
nasc = int(input("informe ano de nascimento:"))
hoje = int(input("informe ano atual"))
idade = hoje - nasc
print("Olá, %s" % nome)
print("você possui em torno de %d anos de idade" % idade)


