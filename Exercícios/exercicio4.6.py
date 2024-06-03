#Escreva um programa que pergunte a distância que um passageiro deseja percorrer em km. Calcule o preço da passagem, cobrando R$ 0,50 por km para viagens de até de 200 km, 
#e R$ 0,45 para viagens mais longas.
distancia = int(input('Qual distância da viagem em Km? '))
if distancia <= 200:
    print(f'Valor a ser cobrado será R${0.50 * distancia:.2f} ')
else:
    print(f'Valor a ser cobrado será R${0.45 * distancia:.2f} ')
