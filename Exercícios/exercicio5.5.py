#Reescreva o programa anterior para escrever os 10 primeiros múltiplos de 3.
#primeiro método comoço com x valendo 3 e somo 3 até chegar ao 30
x = 3
while x <= 30:
    print(x)
    x += 3
    
print('-^'*30)

#segundo método verifico os múltiplos de 3 e caso seja, mostra na tela até chegar no 30
x = cont = 3
while cont <= 12:
    if x % 3 == 0:
        print(x)
        cont += 1   
    x += 1
