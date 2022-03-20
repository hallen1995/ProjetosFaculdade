qkm = float(input('Quantos KM foram percorridos?'))
qd = float(input('Quantos dias o carro foi alugado?'))

preco = 60 * qd + 0.15 * qkm
print('Km = {}. Dias: {}' .format(qkm, qd))
print('Valor total a ser pago: {}' .format(preco))