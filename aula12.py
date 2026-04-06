dias = int(input ("Escreva a quantidade de dias: "))
horas = int(input ("Escreva a quantidade de horas: "))
minutos = int(input ("Escreva a quantidade de minutos: "))
segundos= int(input ("Escreva a quantidade de segundos: "))

total_em_segundos = (dias * 86400) + (horas * 3600) + (minutos * 60) + segundos

print(f"\n O total convertido é de {total_em_segundos} segundos.") 
