#Faça um programa que calcule o aumento de um salário. Ele deve solicitar o valor do salário e a porcentagem
#do aumento. Exiba o valor do aumento e do novo salário.

salario = float(input('Digite o salário: R$'))
aumento = float(input('Porcentagem de aumento: '))
print(f'Aumento de R${salario * aumento / 100:.2f} totalizando novo salário de R${(salario * aumento / 100) + salario:.2f}')
