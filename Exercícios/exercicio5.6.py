#Altere o programa anterior para exibir os resultados no mesmo formato de uma tabuada: 2x1 = 2, 2x2 = 4, …
num = int(input('Digite um valor para tabuada: '))
mult = 1
while mult <= 10:
    print(f'{num} x {mult} = {mult*num}')
    mult += 1
