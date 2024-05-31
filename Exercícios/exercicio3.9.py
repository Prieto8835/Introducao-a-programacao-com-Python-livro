#Escreva um programa que leia a quantidade de dias, horas, minutos e segundos do usuário. Calcule o total 
#em segundos.

dias = int(input('Quantidade de dias: '))
horas = int(input('Quantidade de horas: '))
minutos = int(input('Quantidade de minutos: '))
segundos = int(input('Quantidade de segundos: '))
print(f'Total em segundos: {segundos + (minutos * 60) + (horas * 3600) + (dias * 24 * 3600)} segundos')
