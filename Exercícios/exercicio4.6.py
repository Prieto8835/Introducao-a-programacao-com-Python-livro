distancia = int(input('Qual distância da viagem em Km? '))
if distancia <= 200:
    print(f'Valor a ser cobrado será R${0.50 * distancia:.2f} ')
else:
    print(f'Valor a ser cobrado será R${0.45 * distancia:.2f} ')
