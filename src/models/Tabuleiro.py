from ..model import Jogador, Propriedade, Aleatorio, Cauteloso, Exigente, Impulsivo
import random
from functools import reduce

class Tabuleiro:
    def __init__(self):
        self.propriedades = self.gerarPropriedades()
        self.jogadores = [
            Impulsivo("Impulsivo"),
            Exigente("Exigente"),
            Cauteloso("Cauteloso"),
            Aleatorio("Aleatorio")
        ]

    def gerarPropriedades(self):
        propriedades = []
        for i in range(0, 20):
            propriedades.append(Propriedade(random.randint(10, 100), random.randint(10, 100)))
        return propriedades
    
    
    def devePagarAluguel(self, jogador):
        propriedade = self.propriedades[jogador.posicao]
        return propriedade.possuiProprietario() and not propriedade.pertenceAoJogador(jogador)
        
    def jogarDado(self):
        return random.randint(1, 6)
    
    def completarVolta(self, jogador):
        jogador.saldo += 100
        jogador.posicao = -1
        
    def encerrarJogo(self, dados, relatorio):
        if not dados.vencedor:
            dados.timeout = 1
            dados.vencedor = max(self.jogadores, key=lambda jogador: jogador.saldo).nome
        relatorio.registrarRelatorio(dados)
        
    def reinvindicarPropriedades(self):
        devedores = list(filter(lambda devedor: devedor.estaFalido(), self.jogadores))
        for devedor in devedores:
            map(lambda propriedade: None, self.listarPropriedadesDeDevedores(devedor))
            
    def listarPropriedadesDeDevedores(self, devedor):
        return filter(lambda prop: prop.pertenceAoJogador(devedor), self.propriedades)
    
    def listarDevedores(self):
        return list(filter(lambda jogador: not jogador.estaFalido(), self.jogadores))