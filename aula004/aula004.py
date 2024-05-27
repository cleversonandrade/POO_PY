from datetime import date
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    # Um método de classe para criar 
    # um  objeto Pessoa através do ano de nascimento.
    @classmethod
    def apartir_ano_nascimento(cls, nome, ano):
        return cls(nome, date.today().year - ano)
    # Método Estático: verificar se é maior de idade.
    @staticmethod
    def eh_maior_de_idade(idade):
        return idade >= 18
pessoa1 = Pessoa('Maria', 32)
pessoa2 = Pessoa.apartir_ano_nascimento('Ana', 1983)
print(pessoa1.idade)
print(pessoa2.idade)
#Imprimir o resultado
print(Pessoa.eh_maior_de_idade(17))
