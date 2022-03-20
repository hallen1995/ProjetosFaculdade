


x = 1
while (x <= 5):
    print(x)
    x = x + 1

x = 0
while (x <= 99):
    print(x)
    x = x + 1

x = 0
while (x < 100):
    print(x)
    x = x + 1

inicial = int(input('Qual valor desejar iniciar a contagem?'))
final = int(input('Qual valor deseja encerrar a contagem?'))
x = inicial
while (x <= final):
    if (x % 2 == 0):
        print(x)
    x = x +1