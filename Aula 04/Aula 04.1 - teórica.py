soma = 0
cont = 1
while (cont <= 5):
    x = float(input('Digite a {} nota:'.format(cont)))
    soma = soma + x
    cont = cont + 1
media = soma / 5
print('Média final:{}'.format(media))

if media >= 7:
    print('O aluno foi aprovado com a média: {}.'.format(media))
else:
    print('O Aluno foi reprovado pela média: {}'. format(media))


soma = 0
cont = 1
while (cont <= 5):
    x = float(input('Digite a {} nota:'.format(cont)))
    soma += x
    cont += 1
media = soma / 5
print('Média final:{}'.format(media))