# print(type("Olá Mundo!"))
# print("Olá Mundo!")

class Jogador:
    def jogar(self):
        print('Método jogar foi inicializado')

j1 = Jogador()
j1.jogar()  

# -------------------------------------------

class Pessoa:
    def __init__(self,nome,idade):
        self.nome = nome
        self.idade = idade

    def apresentar(self):
        print(f'Olá meu nome é {self.nome} e minha idade é {self.idade} anos')
    
p1 = Pessoa('Mario', 25)
p1.apresentar()

p2 = Pessoa('Card', 22)
p2.apresentar()

# -------------------------------------------

class Cliente(Pessoa):
    quantidadeClientes=0  #Variável estática static, devido entra no corpo da class
    def __init__(self, nome, idade):
        super().__init__(nome, idade)
        Cliente.quantidadeClientes+=1
        self.cadastro=1000+Cliente.quantidadeClientes
    
    def apresentar(self):
        super().apresentar()
        print(f'e sou cliente de cadastro: {self.cadastro}')
    
c1 = Cliente('Ted', 25)
c2 = Cliente('Toud', 10)

c1.apresentar()
c2.apresentar()


# -------------------------------------------

class Funcionario(Pessoa):
    # pass
    def __init__(self, nome, idade, cadastro):
        self.nome=nome
        self.idade=idade
        self.cadastro=cadastro
X    def apresentar(self):
        print(f'Olá sou o(a) funcionário(a) {self.nome}, minha idade é {self.idade} e nº de cadastro é {self.cadastro}!')

f1 = Funcionario('Pitty', 21, 1001)
f2 = Funcionario('Carlos', 25, 1002)

f1.apresentar()
f2.apresentar()




