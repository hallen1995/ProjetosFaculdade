class Aluno:
    totalAlunos=0
    def __init__(self,nome,nota):
        Aluno.totalAlunos+=1
        self.nome=nome
        self.nota=nota
        self.ru=1000+Aluno.totalAlunos
        
    
    def info(self):
        print(f'Nome: {self.nome}; RU: {self.ru}; Nota: {self.nota};')

    def getNota(self):
        return self.nota


class Turma:
    def __init__(self,nome,limiteAlunos):
        self.nome=nome
        self.limiteAlunos=limiteAlunos
        self.listaAlunos=[]
    
    def addAluno(self,aluno):
        if len(self.listaAlunos) < self.limiteAlunos:
            self.listaAlunos.append(aluno)
            return True
        return False
    
    def mediaTurma(self):
        soma=0
        for aluno in self.listaAlunos:
            soma+=aluno.getNota()
        return soma/len(self.listaAlunos)
    
# a1 = Aluno('Mario,',90)
# a2 = Aluno('Carlos,',80)
# a3 = Aluno('Bob,',90)
# a4 = Aluno('Ted', 80)

t1 = Turma('Programação',4)
t1.addAluno(Aluno('Mario,',90))
t1.addAluno(Aluno('Carlos,',80))
t1.addAluno(Aluno('Bob,',90))
t1.addAluno(Aluno('Ted', 80))

print(t1.mediaTurma())  