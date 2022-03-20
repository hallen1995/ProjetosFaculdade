print('Olá Mundo!')

#Concatenação de Strings:

s1 =  'Lógica de programação'
s1 = s1 + 'e algorítmos.'
print(s1)

#Repetindo strings na concatenação:

s1 = 'A' + '-' * 10 + 'B'
print(s1)

#Composição
nota = 8.5
s1 = 'Você tirou %.2f de média na matéria de Português.' % nota
print(s1)

#######################

nota = 8.5
disciplina = 'algoritmos'
s1 = 'Você tirou %.2f de média na matéria de %s.' % (nota, disciplina)
print(s1)

nota = 8.5
disciplina = 'algoritmos'
s1 = 'Você tirou {} de média na matéria de {}'.format(nota, disciplina)
print(s1)

#Fatiamento de Strings
#são usados [] para determinar Strings que você quer.

s1 = 'Lógica de programação de Algoritmos'
print(s1[10:21])


#Tamanho de String (Length)
# usamos a funçaõ chamada de len

s1 = 'Lógica de programação de algoritmos'
tamanho = len(s1)
print(tamanho)

#Função de Entrada
# input('mensagem')
idade = input('Qual sua idade?')
print(idade)

nome = input('Qual seu nome?')
print('Olá {}, seja bem vindo!'.format(nome))

#Convertendo dados de entrada
nota = float(input('Qual nota você recebeu na disciplina?'))
print('Você tirou {} na disciplina!'.format(nota))

#Atividade

s1 = int(input('Digite um valor inteiro:'))
s2 = int(input('Digite um segundo valor inteiro:'))
soma = s1 + s2
print('A soma dos valores {} com {} = {}'.format(s1, s2, soma))
res = ('A soma dos valores %i com %i = %i' %(s1, s2, s1 + s2))
print(res)
