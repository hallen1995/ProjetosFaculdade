#Dúvida 01
nota = 8.5
s1 = 'Você tirou {} de média na matéria de Português.' .format(nota)
print(s1)

#Como executar esse comando saindo 8.50 e não 8.5


#Dúvida 02
s1 = int(input('Digite um valor inteiro:'))
s2 = int(input('Digite um segundo valor inteiro:'))
soma = s1 + s2
print('A soma dos valores {} com {} = {}'.format(s1, s2, soma))

res = 'A soma dos valores %i com %i = %i'.format(s1, s2, s1 + s2))


#Dúvida 03
soma = 0
cont = 1
while (cont <= 5): #posso utilizar and?
    x = float(input('Digite a {} nota:'.format(cont)))
    soma = soma + x
    cont = cont + 1
media = soma / 5
print('Média final:{}'.format(media))

if media >= 7:
    print('O aluno foi aprovado com a média: {}.'.format(media))
else:
    print('O Aluno foi reprovado pela média: {}'. format(media))

    #Dentre as 5 notas, é possível puxar a nota número 4 se for abaixo de 7 ele já fique reprovado direto?

#Dúvida 04

