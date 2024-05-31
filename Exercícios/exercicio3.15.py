#Escreva um programa para calcular a redução do tempo de vida de um fumante. Pergunte a quantidade de cigarros 
#fumados por dia e quantos anos ele já fumou. Considere que um fumante perde 10 minutos de vida a cada cigarro,
#e calcule quantos dias de vida um fumante perderá. Exiba o total em dias.

cigarros = int(input('Quantida de cigarros diários: '))
anos = float(input('Quantidade de anos fumando: '))
print(f'Quantidade de dias perdidos: {anos * 365 * cigarros * 10 / (24 * 60):.2f}')