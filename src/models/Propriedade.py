class Propriedade:
    def __init__(self, custoDeVenda,valorDeAluguel):
        self.custoDeVenda = custoDeVenda
        self.valorDeAluguel = valorDeAluguel
        self.proprietario = None
        
        
    def possuiProprietario(self):
        return self.proprietario != None
    
    def pertenceAoJogador(self, jogador):
        return self.proprietario == jogador
    
    def atribuirProprietario(self, jogador):
        self.proprietario = jogador
    