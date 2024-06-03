#Escreva um programa que calcule o preço a pagar pelo fornecimento de energia elétrica. Pergunte a quantidade de kWh consumida e o tipo de instalação:
#R para residências, I para indústrias e C para comércios. Calcule o preço a pagar de acordo com a tabela a seguir.
#+---------------------------------------+
#|   Preço por tipo e faixa de consumo   |
#+---------------------------------------+
#| Tipo        | Faixa (kWh)   | Preço   |
#+=======================================+
#| Residencial | Até 500       | R$ 0,40 |
#|             | Acima de 500  | R$ 0,65 |
#+---------------------------------------+
#| Comercial   | Até 1000      | R$ 0,55 |
#|             | Acima de 1000 | R$ 0,60 |
#+---------------------------------------+
#| Industrial  | Até 5000      | R$ 0,55 |
#|             | Acima de 5000 | R$ 0,60 |
#+---------------------------------------+

kwh = int(input('Quantos kWh foram consumidos? '))
tipo = int(input(f'Qual tipo de instalação? \n[1] Residêncial \n[2] Industrial \n[3] Comercial \nSua resposta: '))
#foi colocado essa condição para verificar um valor inválido no começo para evitar que o programa faça todas as outras verificações sem necessidade.
if tipo not in [1, 2, 3]:
    print('Opção inválida! Por favor selecione um valor entre 1 e 3 ')
if tipo == 1:
    if kwh <= 500:
        valor = 0.40
    else:
        valor = 0.65
if tipo == 2:
    if kwh <= 1000:
        valor = 0.55
    else:
        valor = 0.60
if tipo == 3:
    if kwh <= 5000:
        valor = 0.55
    else:
        valor = 0.60
print(f'Valor a ser pago será de R${valor * kwh:.2f}')
#else:
#    print('Opção inválida! Por favor selecione um valor de 1 a 3 ')

#segunda opção de código também correta porém achei mais claro e objetivo para futuras modificações o primeiro código escrito
'''if tipo not in [1, 2, 3]:
    print('Opção inválida! Por favor selecione um valor entre 1 e 3 ')
if kwh <= 500 and tipo == 1:
    print('Preço a pagar será de R$ 0,40 ')
elif kwh > 500 and tipo == 1:
    print('Preço a pagar será de R$ 0,65 ')
elif kwh <= 1000 and tipo == 2:
    print('Preço a pagar será de R$ 0,55 ')
elif kwh > 1000 and tipo == 2:
    print('Preço a pagar será de R$ 0,60 ')
elif kwh <= 5000 and tipo == 3:
    print('Preço a pagar será de R$ 0,55 ')
else:
    print('Preço a pagar será de R$ 0,60 ')'''