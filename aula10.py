a = input ("Digite o valor da variável a: ")
b = input ("Digite o valor da variável b: ")

print(f"Valores originais: a = {a}, b = {b}")

a,b = b,a #tuplas

print(f"Valores trocados: a = {a}, b = {b}") #usamos o f para colocar variáveis diretamente dentro de um texto de forma simples e organizada (f-strings)