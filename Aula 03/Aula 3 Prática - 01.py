print(2 + 2 < 4)
print(7 // 3 == 1 + 1)  #igualdade se usa ==
print(3**2 + 4**2 == 25) #expondencial
print(2 + 4 + 6 > 12)


#1387 é divisível por 19?
#31 é par?
#O menor valor entre: 34, 29 e 31 é menor do que 30?

print(min(34, 29, 31))

numero = float(input('Digite o valor para saber se é par:'))
resto = numero % 2
if resto == 0:
    print('Valor é par!')
else:
    print('Valor não é par!')
