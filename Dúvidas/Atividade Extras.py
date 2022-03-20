#Tu inicializa duas variáveis A e B, A é inicializada com o valor 5 e B
# é inicializada com o valor 4. Daí eu quero que tu troque o valor de ambas,
# A vai precisar receber o valor de B e B precisa receber o valor de A,
# daí imprime o resultado.

def printColuna(texto, tamanhoColuna):
    tamanho = len(texto)

    if tamanho > tamanhoColuna:
        print(texto[0:tamanhoColuna])
    else:
        sobra = tamanhoColuna - tamanho
        esquerda = int(sobra/2)
        direita = sobra-esquerda
        for i in range(esquerda):
            texto = ' '+texto

        for i in range(direita):
            texto = texto+' '

        print('|'+texto+'|')
        # print('|'+' '*esquerda + texto + ' '*direita+'|')


nome = input('Qual é seu nome?')
printColuna(nome, 30)