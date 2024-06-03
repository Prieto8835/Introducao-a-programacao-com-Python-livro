#Escreva um programa para aprovar o empréstimo bancário para compra de uma casa. O programa deve perguntar o valor da casa a comprar, o salário e a quantidade de anos a pagar.
#O valor da prestação mensal não pode ser superior a 30% do salário. Calcule o valor da prestação como sendo o valor da casa a comprar dividido pelo número de meses a pagar.
casa = float(input('Qual valor da casa? R$' ))
salario = float(input('Qual seu salário? R$' ))
anos = int(input('Em quantos anos deseja pagar? '))
prestacao = casa / (anos * 12)
if prestacao > 30 * salario / 100:
    print(f'Valor da prestação é de R${prestacao:.2f}, 30% de seu salário é equivalente a {30 * salario / 100:.2f} e infelizmente o empréstimo foi negado! ')
else:
    print('Parabéns, empréstimo aprovado! ')
