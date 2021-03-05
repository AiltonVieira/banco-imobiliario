from functools import reduce

class Relatorio:
    def __init__(self):
        self.encerradosPorTimeout = 0
        self.turnosPorPartida = []
        self.campeoesPorPartida = []
        
    def registrarRelatorio(self, dados):
        self.campeoesPorPartida.append(dados.vencedor)
        self.encerradosPorTimeout += dados.timeout
        self.turnosPorPartida.append(dados.turno)
        
        
    def gerarRelatorio(self, jogadores):
        return {
            "encerradosPorTimeout" : self.encerradosPorTimeout,
            "mediaDeTurnosPorPartida" : round(reduce((lambda x, y: x + y), self.turnosPorPartida) / len(self.turnosPorPartida), 1),
            "maiorCampeaoPorPartida" : max(self.campeoesPorPartida, key=self.campeoesPorPartida.count),
            "taxaDeVitoriaPorComportamento" : dict((jogador.nome, self.obterTaxaDeVitoria(jogador.nome)) for jogador in jogadores)
        }
        
    def obterTaxaDeVitoria(self, nome):
        return f"{round(( self.campeoesPorPartida.count(nome) * 100 ) / len(self.campeoesPorPartida), 1)}%"
        