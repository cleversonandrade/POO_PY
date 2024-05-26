#Criando Classe Pessoa
class Pessoa:
    def __init__(self, nome, ender):
        self.set_nome(nome)
        self.set_ender(ender)

    def set_nome(self, nome):
        self.nome = nome

    def set_ender(self, ender):
        self.ender= ender

    def get_nome(self):
        return self.nome
    
    def get_ender(self):
        return self.ender
    
#Instanciando uma Classe
pessoa1 = Pessoa('Cleverson', 'Rua: Lamartine Ferreira Leite')
pessoa2 = Pessoa('Jessica', 'Rua: Lamartine Ferreira Leite')

print(f'Nome {pessoa1.get_nome()}, Endereco: {pessoa1.get_ender()}')
print(f'Nome {pessoa2.get_nome()}, Endereco: {pessoa2.get_ender()}')