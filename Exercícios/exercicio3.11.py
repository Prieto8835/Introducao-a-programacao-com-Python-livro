#Faça um programa que solicite o preço de uma mercadoria e o percentual de desconto. Exiba o valor do 
#desconto e o preço a pagar.

preço = int(input('Preço do produto: R$'))
desconto = int(input('Porcentagem de desconto: '))
print(f'Valor do desconto R${preço * desconto / 100:.2f} e o preço a pagar será R${preço - (preço * desconto / 100):.2f}')
