#Altere o programa anterior de forma a perguntar também o valor depositado mensalmente. Esse valor será depositado no início de cada mês,
#e você deve considerá-lo para o cálculo de juros do mês seguinte.
inicial = float(input('Digite o valor de depósito inicial: R$'))
juros = float(input('Digite a taxa de juros da poupança em porcentagem: '))
adicional = float(input(f'Digite um valor para adicionar nesse mês: R$'))
meses = 0
novovalor = inicial
while meses < 24:    
    novovalor += adicional + juros * novovalor / 100
    meses += 1
    print(f'Valor do mês {meses}: R${novovalor:.2f} ')
print(f'O total foi de R${novovalor:.2f} com acréscimo de R${novovalor - inicial:.2f} em juros ')
