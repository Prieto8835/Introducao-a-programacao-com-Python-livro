#Escreva um programa que pergunte o salário do funcionário e calcule o valor do aumento. Para salários superiores a R$ 1.250,00, calcule um aumento de 10%.
#Para os inferiores ou iguais, de 15%.
salario = float(input('Digite seu salário R$ '))
antigo = salario
if salario > 1250:
    salario = (salario * 10 / 100) + salario
if salario <= 1250:
    salario = (salario * 15 / 100) + salario
print(f'Seu novo salário será de R${salario:.2f} tendo um aumento de R${salario - antigo:.2f} em relação ao salário inicial')

#código resposta do site, achei mais simples e funcional usando menas linhas pra resolver mesmo problema
'''salário = float(input("Digite seu salário: "))
pc_aumento = 0.15
if salário > 1250:
    pc_aumento = 0.10
aumento = salário * pc_aumento
print(f"Seu aumento será de: R$ {aumento:7.2f}")'''