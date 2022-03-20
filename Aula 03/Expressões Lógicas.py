#Expressão lógicas


# not

x = 10
y = 1
res = not x > y
print(res)

# and

x = 10
y = 1
res = x > y and x == y
print(res)

# or

x = 10
y = 1
res = (x > y) or (x == y)
print(res)


#Atividade Not/And/Or

n1 = float(input('Digite a nota da 1ª matéria:'))
n2 = float(input('Digite a nota da 2ª matéria:'))
n3 = float(input('Digite a nota da 3ª matéria:'))
if n1 >= 7 and n2 >= 7 and n3 >= 7:
    print('Você foi aprovado em todas as matérias!')
else:
    print('Você não foi aprovado em todas as matérias!')