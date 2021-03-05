class Jogador:
    def __init__(self, nome):
        self.nome = nome
        self.saldo = 300
        self.posicao = -1
            
    def comprarPropriedade(self, propriedade):
        self.saldo -= propriedade.custoDeVenda
        propriedade.atribuirProprietario(self)
        
    def andar(self, posicao):
        self.posicao = self.posicao + posicao
        
    def pagarAluguel(self, propriedade):
        self.saldo -= propriedade.valorDeAluguel
        propriedade.proprietario.saldo += propriedade.valorDeAluguel
    
    def estaFalido(self):
        return self.saldo <= 0