#Escreva um programa que exiba uma lista de opções (menu): adição, subtração, divisão, multiplicação e sair.
#Imprima a tabuada da operação escolhida.
#Repita até que a opção saída seja escolhida.
while True:
    tabuada = número = 1
    opção = int(input('[1] Adição \n[2] Subtração \n[3] Multiplicação \n[4] Divisão \n[5] Sair \nSua opção: '))
    if opção == 1:
        número = int(input('Tabuada de ADIÇÃO do número: '))
        while tabuada <= 10:
            print(f'{número} + {tabuada} = {número + tabuada}' )
            tabuada += 1
        print('-~' * 15)
    elif opção == 2:
        número = int(input('Tabuada de SUBTRAÇÃO do número: '))
        while tabuada <= 10:
            print(f'{número} - {tabuada} = {número - tabuada}')
            tabuada += 1
        print('-~' * 15)
    elif opção == 3:
        número = int(input('Tabuada de MULTIPLICAÇÃO do número: '))
        while tabuada <= 10:
            print(f'{número} x {tabuada} = {número * tabuada}')
            tabuada += 1
        print('-~' * 15)
    elif opção == 4:
        número = int(input('Tabuada de DIVISÃO do número: '))
        while tabuada <= 10:
            print(f'{número} / {tabuada} = {número / tabuada:.2f}')
            tabuada += 1
        print('-~' * 15)
    elif opção == 5:
        print('Fim do programa! ')
        break
    else:
        print('Opção incorreta! ')

#resposta do exercício:
while True:
    print("""

Menu
----
1 - Adição
2 - Subtração
3 - Divisão
4 - Multiplicação
5 - Sair

""")
    opção = int(input("Escolha uma opção:"))
    if opção == 5:
        break
    elif opção >= 1 and opção < 5:
        n = int(input("Tabuada de:"))
        x = 1
        while x <= 10:
            if opção == 1:
                print(f"{n} + {x} = {n + x}")
            elif opção == 2:
                print(f"{n} - {x} = {n - x}")
            elif opção == 3:
                print(f"{n} / {x} = {n / x:5.4f}")
            elif opção == 4:
                print(f"{n} x {x} = {n * x}")
            x = x + 1
    else:
        print("Opção inválida!")