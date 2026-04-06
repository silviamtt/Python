a = input ("Digite o valor da variável a: ")
b = input ("Digite o valor da variável b: ")

print(f"Valores originais: \n a = {a}, b = {b}") #\n quebra de linha

aux = a 
a = b
b= aux

print(f"Valores trocados: a = {a}, b = {b}")