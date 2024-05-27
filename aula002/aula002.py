class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    def imprimir(self):
        print(self.nome,' Tem', 
              self.idade, ' ano(s)')
    def getIdade(self):
        return self.idade
    def setIdade(self, idade):
        self.idade = idade
p = Pessoa('Katia', 30)
p.imprimir()

#Herança
class Profissional(Pessoa):
    def __init__(self, nome, idade, profissao):
        super().__init__(nome, idade)
        self.profissao = profissao
    def imprimir(self):
        super().imprimir()
        print('\t e trabalha como ', self.profissao)

#Polimorfismo
p = Profissional('Cleverson', 40, 'Estudante')
p.imprimir()