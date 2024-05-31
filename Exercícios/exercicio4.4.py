salario = float(input('Digite seu salário R$ '))
antigo = salario
if salario > 1250:
    salario = (salario * 10 / 100) + salario
if salario <= 1250:
    salario = (salario * 15 / 100) + salario
print(f'Seu novo salário será de R${salario:.2f} tendo um aumento de R${salario - antigo:.2f} em relação ao salário inicial')
