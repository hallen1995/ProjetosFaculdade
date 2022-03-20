#Condicional aninhas


print('Escolha o que deseja comprar:')
print('1 - Maçã')
print('2 - Laranja')
print('3 - Banana')
produto = int(input('Qual sua escolha?'))
qtd = int(input('Qual quantidade desejada?'))
if (produto == 1):
    pagar = qtd * 2.30
    print('Você comprou {} und maças. Total à pagar {} R$'. format(qtd, pagar))
elif (produto == 2):
    pagar = qtd * 3.6
    print('Você comprou {} und laranja. Total à pagar {} R$.'. format(qtd, pagar))
elif (produto == 3):
    pagar = qtd * 1.85
    print('Você comprou {} und banana. Total à pagar {} R$.'.format(qtd, pagar))
else:
    print('Produto inexistente!')