#Reescreva o Programa 5.1 de forma a continuar executando até que o valor digitado seja 0. Utilize repetições aninhadas.
while True:
    cédulas = 0
    atual = 50
    valor = int(input('Digite o valor a pagar: '))
    if valor == 0:
        print('Fim do programa! ')
        break
    apagar = valor
    while True:
        if atual <= apagar:
            apagar -= atual
            cédulas += 1
        else:
            print(f'{cédulas} cédula(s) de R${atual:.2f} ')
            if apagar == 0:
                break
            if atual == 50:
                atual = 20
            elif atual == 20:
                atual = 10
            elif atual == 10:
                atual = 5
            elif atual == 5:
                atual = 1
            cédulas = 0
