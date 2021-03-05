from .Jogador import Jogador

class Cauteloso(Jogador):
    def __init__(self, nome):
        super().__init__(nome)
        
    def podeNegociarPropriedade(self, propriedade):
        return (self.saldo - propriedade.custoDeVenda) >= 80 and self.saldo >= propriedade.custoDeVenda