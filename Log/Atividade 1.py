nome = 'Hallen Victor de Alencar Barreto'
ru = '1606837'
print(nome + ' - RU:' + ru)
p1 = 0   #Entrada da compra abaixo do valor onde resulta em 0% de desconto
p2 = 5   #Entrada de 5% de desconto
p3 = 10  #Entrada de 10% de desconto
p4 = 15  #Entrada de 15% de desconto
print('Bem Vindo a loja do Hallen Victor de Alencar Barreto!')
valor = float(input('Entre com o valor do produto:'))
qtd = float(input('Entre com a quantidade do produto:'))
total = valor * qtd

while (qtd <=0): #While para quando for digitado um valor abaixo de 0 ser refeita a pergunta ao cliente.
    print('Bem Vindo a loja do Hallen Victor de Alencar Barreto!')
    valor = float(input('Entre com o valor do produto:'))
    qtd = float(input('Entre com a quantidade do produto:'))
if (qtd <= 1 or qtd <= 9):  #Caso digite entre 1 a 9 ele excutará o programa, caso valor contrário pulará próxima instrução.
    print('O Valor do produto sem desconto:{:.2f}.'.format(total))
    print('O Valor do produto com desconto:{:.2f}. (desconto 0%)'.format(total))
elif (qtd <= 10 or qtd <= 99): #Caso digite entre 10 a 99 ele excutará o programa, caso valor contrário pulará próxima instrução.
    print('O Valor do produto sem desconto:{:.2f}'.format(total))
    print('O Valor do produto com desconto:{:.2f}. (desconto 5%)'.format(total - (total * p2 / 100)))
elif (qtd <= 100 or qtd <= 999): #Caso digite entre 100 a 999 ele excutará o programa, caso valor contrário pulará próxima instrução.
    print('O Valor do produto sem desconto:{:.2f}'.format(total))
    print('O Valor do produto com desconto:{:.2f}. (desconto 10%)'.format(total - (total * p3 / 100)))
elif (qtd >= 1000): #Caso digite valor igual ou maior que 1000 ele executará o programa.
    print('O Valor do produto sem desconto:{:.2f}'.format(total))
    print('O Valor do produto com desconto:{:.2f}. (desconto 15%)'.format(total - (total * p4 / 100)))