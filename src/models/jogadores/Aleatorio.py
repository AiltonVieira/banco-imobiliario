from .Jogador import Jogador
import random

class Aleatorio(Jogador):
    def __init__(self, nome):
        super().__init__(nome)     
        
    def podeNegociarPropriedade(self, propriedade):
        return random.randint(0, 1) == 1 and self.saldo >= propriedade.custoDeVenda