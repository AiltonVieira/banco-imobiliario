from src.model import Tabuleiro, Jogador, Relatorio, Dados
import random
import curses

def iniciar(terminal):
    iniciarTerminal(terminal)
    relatorio = Relatorio()
    for i in range(0, 300):
        tabuleiro = Tabuleiro()
        dados = Dados()
        random.shuffle(tabuleiro.jogadores)
        for i in range(0, 1000):
            jogadores = list(filter(lambda j: not j.estaFalido(), tabuleiro.jogadores))
            tabuleiro.reinvindicarPropriedades()
            if len(jogadores) == 1:
                dados.vencedor = jogadores[0].nome
                dados.turno = i
                break
            for jogador in jogadores:
                jogador.andar(tabuleiro.jogarDado())
                if jogador.posicao >= len(tabuleiro.propriedades):
                    tabuleiro.completarVolta(jogador)
                else:
                    if tabuleiro.devePagarAluguel(jogador):
                        jogador.pagarAluguel(tabuleiro.propriedades[jogador.posicao])
                    else:
                        if jogador.podeNegociarPropriedade(tabuleiro.propriedades[jogador.posicao]):
                            jogador.comprarPropriedade(tabuleiro.propriedades[jogador.posicao])
        tabuleiro.encerrarJogo(dados, relatorio)
    montarTerminal(terminal, relatorio.gerarRelatorio(tabuleiro.jogadores))
    
def ajustarTexto(relatorio):
    resultado = \
        f'''
            --------------------  Resultado Final  -----------------------
            Vitórias por Timeout: {relatorio['encerradosPorTimeout']}
            Média de Turnos por Partida: {relatorio['mediaDeTurnosPorPartida']}
            Maior Campeão: {relatorio['maiorCampeaoPorPartida']}
            Taxa de Vitória por Jogador: '''
    for taxa in relatorio['taxaDeVitoriaPorComportamento']:
        resultado += f"{taxa} - {relatorio['taxaDeVitoriaPorComportamento'][taxa]} | "
    return resultado

def iniciarTerminal(terminal):
    terminal.clear()
    curses.curs_set(0)
    h, w = terminal.getmaxyx()
    terminal.addstr(h//2, w//2, "Simulando partidas...")
    terminal.refresh()

def montarTerminal(terminal, relatorio):
    try:
        while True:
            terminal.clear()
            terminal.refresh()
            h, w = terminal.getmaxyx()
            terminal.addstr(h//2 - 5, 0, ajustarTexto(relatorio))
            textoEncerrar = "Aperte qualquer tecla para encerrar..."
            terminal.addstr(h - 2, (w - len(textoEncerrar))//2, textoEncerrar)
            terminal.refresh()
            key = terminal.getch()
            if(key):
                return False
    except curses.error as e:
        raise RuntimeError("Seu terminal é muito pequeno para exibir o resultado, por favor maximize ele.")
      
curses.wrapper(iniciar)