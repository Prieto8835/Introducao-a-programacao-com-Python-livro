#Escreva um programa que pergunte o valor inicial de uma dívida e o juro mensal. Pergunte também o valor mensal que será pago. 
#Imprima o número de meses para que a dívida seja paga, o total pago e o total de juros pago.
inicial = float(input('Valor inicial da dívida R$'))
juros = float(input('Valor dos juros mensais em porcentagem: '))
pago = float(input('Valor mensal a ser pago R$'))
meses = juros_total = 0
valor_inicial = inicial
if inicial * juros / 100 >= pago:
    print('Essa dívida nunca será quitada pois a taxa de juros é maior que o valor mensal a ser adicionado! ')
else: 
    while inicial > 0:
        #soma de juros total
        juros_total += inicial * juros / 100
        #saber quanto falta para quitar a dívida
        inicial += (inicial * juros / 100) - pago   
        #se ainda tiver um valor a ser quitado mostra quanto falta, caso contrário mostrará que está quitada 
        if inicial > 0:
            print(f'Valor restante do mês {meses + 1} é de R${inicial:.2f} ')
        else: 
            print('Dívida quitada! ')
        meses += 1
    print(f'Foram necessários {meses - 1} meses para quitar a dívida com valor total pago de R${juros_total + valor_inicial:.2f} e acumulo de juros de R${juros_total:.2f} ')
