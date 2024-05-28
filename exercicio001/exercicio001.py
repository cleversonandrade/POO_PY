class Veiculo:
    def __init__(self, nome, velocidade_max, quilometro_por_litro):
        self.nome = nome
        self.velocidade_max = velocidade_max
        self.quilometro_por_litro = quilometro_por_litro
    
    def to_str(self):
        print(f'Nome = {self.nome}')
        print(f'velocidade_max = {self.velocidade_max}')
        print(f'Quilometros percorridos por litro = {self.quilometro_por_litro}')

modelo_carro = Veiculo('Monza', 180, 10)
modelo_carro.to_str()

class Onibus(Veiculo):
    pass

onibus_escolar = Onibus('Scania', 120, 8)
onibus_escolar.to_str()