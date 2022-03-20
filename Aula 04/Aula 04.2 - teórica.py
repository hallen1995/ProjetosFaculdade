
x = int(input('Digite um valor que seja maior que zero entre (0 a 5):'))
while (x <= 0 and x <=5):
    x = int(input('Digite um valor que seja maior que zero:'))
print('Você digitou {}. Encerrando o programa...!'. format(x))

if x == 1:
    print('Você ganhou 10% de desconto!')
elif x == 2:
    print('Você ganhou 20% de desconto!')
elif x == 3:
    print('Você ganhou 30% de desconto!')
elif x == 4:
    print('Você ganhou 40% de desconto!')
elif x == 5:
    print('Você ganhou 50% de desconto!')


