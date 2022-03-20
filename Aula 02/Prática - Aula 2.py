#Função de Saída
#print('mensagem')
#input('mensagem')

#Atividade expressões algebricas
print(1 + 2 + 3 + 4 + 5)
print((23 + 19 + 31) / 3)
print(403 // 73)
print(403 % 73)
print(2**10)
print(abs(54 - 57))
print(min(34, 29, 31))

a = 3
b = 4
c = (a * a) + (b * b)
print(c)

#Atividades Strings
s1 = 'ant'
s2 = 'bat'
s3 = 'cod'

print(s1 + ' ' +  s2 + ' ' + s3)
print((s1 + ' ') * 10)
print(s1 + (s2 + ' ') * 2 + (s3 + ' ')  * 3)
print((s1 + ' ' + s2 + ' ') * 7)
print((s2 + s2 + s3 + ' ') * 4)

#Atividade 01

produto = float(input('Digite o valor do produto:'))
desconto = float(input('Digite o valor do desconto:'))
res = produto * (desconto / 100)
print('Valor final do produto é : {} R$'.format(produto - res))

#Atividade 02
carro = 60
km = 0.15
rodado = float(input('Quantos Km foi percorrido durante o tempo do aluguel?'))
dias = int(input('Quantos dias que o carro foi alugado?'))
valor = (dias * carro) + (km * rodado)
print('Com base nas informações, foram rodados {} Km no período de {} dias de aluguel'.format (rodado, dias))
print('Diante o preço {} e a quantidade de {} dias o valor a ser {}'.format(km, dias, valor))

#Atividade 02.1
km = int(input('Quantos Km foram percorridos?'))
dias = int(input('Quantos dias ele foi alugado?'))

preco = km * 0.15 + dias * 60
print('Km = {}. Dias {}'.format (km, dias))
print('O Valor a ser pago será de: {}'.format(preco))

#Atividade 03
frase = input('Digite uma frase:')
tam = len(frase)

frase2 = frase[:int(tam/2)]
print(frase2[6:])