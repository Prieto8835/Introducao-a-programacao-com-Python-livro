#Modifique o programa anterior para imprimir de 1 até o número digitado pelo usuário, mas, dessa vez, apenas os números ímpares.
#primeiro método eu somo de 2 em 2
fim = int(input('Digite o último número a imprimir: '))
x = 1
while x <= fim:
    print(x)
    x += 2

#segundo método verifico antes se o valor é ímpar
último = int(input('Digite o último número a imprimir: '))
x = 1
while x <= último:
    if x % 2 == 1:
        print(x)
    x += 1
