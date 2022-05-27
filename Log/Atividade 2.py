def alinhar(texto, tamanhoColuna, caracter): #Def utilizada para alinha a String de acordo com a quantidade de caracteres existentes.
    tamanho = len(texto)
    if tamanho > tamanhoColuna:
        print(texto[0:tamanhoColuna])
    else:
        sobra = tamanhoColuna - tamanho
        esquerda = int(sobra/2)
        direita = sobra-esquerda
        texto = esquerda*caracter+texto+direita*caracter
    return texto
soma = 0  #Entrada Soma = 0 antes do While True para acumular todas as somatórias duruante a execução do programa.
nome = 'Hallen Victor de Alencar Barreto'
ru = '1606837'
print(nome + ' - RU:' + ru)
print('Bem Vindo a Lanchonete do Hallen Victor de Alencar Barreto') #Começo da execução do programa.
while True:  #A utlização da Def Alinhar para centralizar todos as Strings
    print(alinhar('Cardápio', 58, '*'))
    print('|'+alinhar('Código', 10, ' ')+'|'+alinhar('Descrição', 30, ' ')+'|'+alinhar('Valor', 10, ' ')+'|')
    print('|'+alinhar('100', 10, ' ')+'|'+alinhar('Cachorro Quente', 30, ' ')+'|'+alinhar('9,00', 10, ' ')+'|')
    print('|'+alinhar('101', 10, ' ')+'|'+alinhar('Cachorro Quente Duplo', 30, ' ')+'|'+alinhar('11,00', 10, ' ')+'|')
    print('|'+alinhar('102', 10, ' ')+'|'+alinhar('X-Egg', 30, ' ')+'|'+alinhar('12,00', 10, ' ')+'|')
    print('|'+alinhar('103', 10, ' ')+'|'+alinhar('X-Salada', 30, ' ')+'|'+alinhar('12,00', 10, ' ')+'|')
    print('|'+alinhar('104', 10, ' ')+'|'+alinhar('X-Bacon', 30, ' ')+'|'+alinhar('14,00', 10, ' ')+'|')
    print('|'+alinhar('105', 10, ' ')+'|'+alinhar('X-Tudo', 30, ' ')+'|'+alinhar('17,00', 10, ' ')+'|')
    print('|'+alinhar('200', 10, ' ')+'|'+alinhar('Refrigerante Lata', 30, ' ')+'|'+alinhar('5,00', 10, ' ')+'|')
    print('|'+alinhar('201', 10, ' ')+'|'+alinhar('Chá Gelado', 30, ' ')+'|'+alinhar('4,00', 10, ' ')+'|')
    codigo = int(input('Entre com o código desejado:'))
    if codigo == 100: #início das condições if e elif para analisar qual código foi utilizado pelo cliente.
        soma += 9
        print('Você pediu um Cachorro Quente no valor de 9 R$.')
    elif codigo == 101:
        soma += 11
        print('Você pediu um Cachorro Quente Duplo no valor de 11 R$.')
    elif codigo == 102:
        soma += 12
        print('Você pediu um X-Egg no valor de 12 R$.')
    elif codigo == 103:
        soma += 12
        print('Você pediu um X-Salada no valor de 12 R$.')
    elif codigo == 104:
        soma += 14
        print('Você pediu um X-Bacon no valor de 14 R$.')
    elif codigo == 105:
        soma += 17
        print('Você pediu um X-Tudo no valor de 17 R$.')
    elif codigo == 200:
        soma += 5
        print('Você pediu um Refrigerante Lata no valor de 5 R$.')
    elif codigo == 201:
        soma += 4
        print('Você pediu um Chá Gelado no valor de 4 R$.')
    else:   #utilização do Else para caso seja digitado o codigo diferente do cardápio ele acusará Opção inválida e recomeçará o programa.
        print('Opção inválida')
        continue
        print('Deseja pedir mais alguma coisa?')
        print('1 - Sim')
        print('0 - Não')
        codigo2 = input('>>')
    if codigo2 == '1':  # if para caso o cliente deseja compra mais alguma coisa, ele retornará ao início do programa.
        continue
    else:
        print('O total a ser pago é: {}R$.'. format(soma))  #else e break utilizado para encerrar a compra do cleinte e mostrar o valor t0otal a ser pago.
        break