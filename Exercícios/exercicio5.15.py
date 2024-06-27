#screva um programa para controlar uma pequena máquina registradora. Você deve solicitar ao usuário que digite o código do produto e a quantidade comprada. 
#Utilize a tabela de códigos a seguir para obter o preço de cada produto:
#Código Preço
#1      0,50
#2      1,00 
#3      4,00
#5      7,00
#9      8,00
#Seu programa deve exibir o total das compras depois que o usuário digitar 0.
#Qualquer outro código deve gerar a mensagem de erro “Código inválido”.
cont = total = 0
while True:
    print('Digite o código do produto:\n[1] R$0,50\n[2] R$1,00\n[3] R$4,00\n[5] R$7,00\n[9] R$8,00\n[0] Sair' )
    código = int(input('Sua opção: '))
    valor = 0
    if código == 0:
        break
    elif código == 1:
        valor = 0.5
    elif código == 2:
        valor = 1      
    elif código == 3:
        valor = 4      
    elif código == 5:
        valor = 7       
    elif código == 9:
        valor = 8
    else:
        print('Código inválido! ')
    if valor != 0:
        qntd = int(input('Digite a quantidade desse produto: '))
        cont += qntd
        total += valor * qntd
print(f'Quantidade de produtos comprados foi de {cont} itens totalizando R${total:.2f} gastos ')
    