from .Jogador import Jogador

class Impulsivo(Jogador):
    def __init__(self, nome):
        super().__init__(nome)
        
        
    def podeNegociarPropriedade(self, propriedade):
        return self.saldo >= propriedade.custoDeVenda