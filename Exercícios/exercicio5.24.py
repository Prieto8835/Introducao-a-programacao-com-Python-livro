#Modifique o programa anterior de forma a ler um número n. Imprima os n primeiros números primos.
qntd = int(input('Quantos números primos gostaria de imprimir na tela? '))
primos = divisor = cont = 1
num = 3
if qntd < 0:
    print('Valor inválido! ')
#imprimi o primeiro número primo, sendo o 2 único par primo
elif qntd >= 1:
    print(f'1° número primo: {num - 1}')
#enquanto não tiver a quantidade de números primos requisitada
while cont < qntd:
    #para que faça verificação de números primos, pegando o num e dividindo pelo divisor, caso seja somente por 1 e ele mesmo soma 1 a primos
    while divisor <= num:
        if num % divisor == 0:
            primos += 1
        #para dividir apenas pelos ímpares
        divisor += 2
    if primos == 3:
        print(f'{cont + 1}° número primo: {num}')
        #caso seja primo aí sim é somado 1 ao contador
        cont += 1
    #somado 2 ao num para ir pro próximo valor a ser analisado
    num += 2
    #precisa-se voltar aos padrões esses valores para não dar erro e na comparação usar números errados
    primos = divisor = 1
