s1 = 'ant'
s2 = 'bat'
s3 = 'cod'
print(s1 + ' ' + s2 + ' ' + s3)
print(10 * (s1 + ' '))
print(s1 + ' s1'*5 + (2 * (s2 +' ')) + (2 * (s3 + ' ' )))
print(7 * (s1 + ' ' + s2 + ' '))
print(5 * (s2 + s2 + s3 + ' '))

preco = float(input('Digite o preço do produto:'))
p = float(input('Digite o porcentual de desconto (0-100) :'))
desconto = preco * (p / 100)
final = preco - desconto
print('O preço do produto é de {}. Desconto de {}%' .format(preco, p))
print('Valor calculado do desconto: {}. Valor final do produto: {}' .format(desconto, final ))