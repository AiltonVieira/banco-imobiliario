from .Jogador import Jogador

class Exigente(Jogador):
    def __init__(self, nome):
        super().__init__(nome)
              
    def podeNegociarPropriedade(self, propriedade):
        return propriedade.valorDeAluguel > 50 and self.saldo >= propriedade.custoDeVenda