#Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado pelo usuário, assim 
#como a quantidade de dias pelos quais o carro foi alugado. Calcule o preço a pagar, sabendo que o carro 
#custa R$ 60 por dia e R$ 0,15 por km rodado.

distancia = float(input('Distância percorrida em Km: '))
dias = int(input('Dias que o carro ficou alugado: '))
print(f'Valor total gasto é de R${(60 * dias) + (0.15 * distancia):.2f}')
