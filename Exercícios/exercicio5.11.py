#Escreva um programa que pergunte o depósito inicial e a taxa de juros de uma poupança. Exiba os valores mês a mês para os 24 primeiros meses.
#Escreva o total ganho com juros no período.
inicial = float(input('Digite o valor de depósito inicial: R$'))
juros = float(input('Digite a taxa de juros da poupança: '))
meses = 0
novovalor = inicial
while meses < 24:
    novovalor += juros * novovalor / 100
    meses += 1
    print(f'Valor do mês {meses}: R${novovalor:5.2f} ')
print(f'O total foi de R${novovalor:.2f} com acréscimo de R${novovalor - inicial:.2f} em juros ')
