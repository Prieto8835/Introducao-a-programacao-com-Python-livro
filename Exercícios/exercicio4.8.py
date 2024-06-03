#Reescreva o Programa 4.4 e calcule a conta da operadora Tchau usando else.
plano = input('Qual é seu plano de celular? ')
if plano == 'falopouco':
    minutos_no_plano = 100
    extra = 0.20
    preço = 50
else:
    if plano == 'falomuito':
        minutos_no_plano = 500
        extra = 0.15
        preço = 99
    else:
        if plano != 'falopouco' and plano != 'falomuito':
            print('Desconheço esse plano! ')
if plano == 'falopouco' or plano == 'falomuito':
    minutos_consumidos = int(input('Quantos minutos você consumiu? '))
    print('Você vai pagar: ')
    print(f'Preço do plano {preço:.2f} ')
    suplemento = 0
    if minutos_consumidos > minutos_no_plano:
        suplemento = extra * (minutos_consumidos - minutos_no_plano)
    print(f'Suplemento R${suplemento:.2f} ')
    print(f'Total R${preço + suplemento:.2f} ')
