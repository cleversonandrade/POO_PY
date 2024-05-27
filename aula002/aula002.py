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
