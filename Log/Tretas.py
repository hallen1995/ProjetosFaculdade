def dimensoesObjeto():
    while True:
        try:
            comprimentoO = float(input('Digite o comprimento do objeto (em cm):'))
            larguraO = float(input('Digite o lagura do objeto (em cm):'))
            alturaO = float(input('Digite o altura do objeto (em cm):'))
            dimensaoO = comprimentoO * larguraO * alturaO
            print('O Volume do objeto é (em cm³): {:.2f}'.format(dimensaoO))
            if dimensaoO < 1000:
                return 10
            elif (dimensaoO >= 1000) and (dimensaoO < 10000):
                return 20
            elif (dimensaoO >= 10000) and (dimensaoO < 30000):
                return 30
            elif (dimensaoO >= 30000) and (dimensaoO < 100000):
                return 50
            else:
                print('Não aceitamos objetos tão pesados')
                continue
        except ValueError:
            print('Você digitou alguma dimensão do objeto com valor não numérico')
            continue
#------------FIM DA FUNÇÃO DIMENSÕES -------------# #
#
# -------------COMEÇO DA FUNÇÃO PESO---------------#

def pesoObjeto():
    while True:
        try:
            pesoO = float(input('Digite o peso do objeto (em kg):'))
            if pesoO < 0.1:
                return 1
            elif (pesoO >= 0.1) and (pesoO < 1):
                return 1.5
            elif (pesoO >= 1) and (pesoO < 10):
                return 2
            elif (pesoO >= 10) and (pesoO < 30):
                return 3
            else:
                print('Não aceitamos objetos tão pesados')
                print('Entre com o peso desejado novamente')
            continue
        except ValueError:
            print('Você digitou peso do objeto com valor não numérico')
            continue

#---------------FIM DA FUNÇÃO PESO ---------------#
#
#-------------COMEÇO DA FUNÇÃO ROTA---------------#
def rotaObjeto():
    while True:
        rotaO = input('Selecione a rota: '
                      '\nRS - De Rio de Janeiro até São Paulo '         
                      '\nSR - De São Paulo até Rio de Janeiro'         
                      '\nBS - De Brasília até SãoPaulo'         
                      '\nSB - De São Paulo até Brasília'         
                      '\nBR - De Brasília até Rio de Janeiro'         
                      '\nRB - Rio de Janeiro até Brasília'         
                      '\n>>')
        rotaO = rotaO.upper()
        if rotaO == 'RS':
            return 1
        elif rotaO == 'SR':
            return 1
        elif rotaO == 'BS':
            return 1.2
        elif rotaO == 'SB':
            return 1.2
        elif rotaO == 'BR':
            return 1.5
        elif rotaO == 'RB':
            return 1.5
        else:
            print('Você digitou uma rota que não existe')
            print('Por Favor entre com a rota desejada novamente')
        continue
# ---------------FIM DA FUNÇÃO ROTA ---------------#
# #-------------------INICIO DO PROGRAMA--------------------

print('Bem Vindo a Companhia de Logística Hallen Victor de Alencar Barreto S.A')
dimensao = dimensoesObjeto()
peso = pesoObjeto()
rota = rotaObjeto()
total = dimensao * peso * rota
print('Total a pagar(R$): {:.2f} (dimensões: {} * peso: {} * rota: {}'.format(total, dimensao, peso, rota))