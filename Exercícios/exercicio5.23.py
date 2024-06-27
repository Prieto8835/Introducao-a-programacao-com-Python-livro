#Escreva um programa que leia um número e verifique se é ou não um número primo.
#Para fazer essa verificação, calcule o resto da divisão do número por 2 e depois por todos os números ímpares até o número lido.
#Se o resto de uma dessas divisões for igual a zero, o número não é primo.
#Observe que 0 e 1 não são primos e que 2 é o único número primo que é par.
cont = primos = 1
num = int(input('Digite um valor para verificar se é primo: '))
if num < 0:
    print('Número INVÁLIDO! ')
elif num == 2:
    print(f'O número {num} é primo! ')
elif num != 2 and num % 2 == 0:
    print(f'O número {num} não é primo pois é divisível por 2! ')
#como ele não é num = 2 e não é par ele verifica os demais números, ou seja os ímpares
#daria para colocar condição também if num % 2 == 1 para averiguar se é ou não ímpar
else:
    while cont <= num:
        if num % cont == 0: 
            primos += 1
        #soma 2 ao cont para fazer a divisão pelos ímpares, já que cont tá como 1 inicialmente
        cont += 2
    #como primos começa com 1, se ele for divisível por 1 e ele mesmo vai somar 2 totalizando 3
    if primos == 3:
        print(f'O número {num} é primo pois só é divisível por 1 e ele mesmo! ')
    else:
        print(f'O número {num} mesmo sendo ímpar não é primo! ')
