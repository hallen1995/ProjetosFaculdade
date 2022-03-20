#Condicional Elif


nome = input('Qual é seu nome?')
idade = int(input('Qual é sua idade?'))
if nome == 'Hallen':
    print('Olá, Hallen!')
elif idade < 18:
    print('Você não é o Hallen, você é de menor!')
elif 100 < idade:
    print('Você não é o Hallen, você talvez não exista')

