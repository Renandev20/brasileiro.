import random

class Jogador:
    def __init__(self, numero, posicao, nome, clube, valor, categoria):
        self.numero = numero
        self.posicao = posicao
        self.nome = nome
        self.clube = clube
        self.valor = valor
        self.categoria = categoria

    def exibir_informacoes(self):
        print(f"{self.numero}. {self.posicao}: {self.nome} ({self.clube}) - € {self.valor} milhões ({self.categoria})")

class Time:
    def __init__(self, nome, orcamento):
        self.nome = nome
        self.orcamento = orcamento
        self.jogadores = []
        self.chance_campeao = 0
        self.pontos = 0

    def exibir_informacoes(self):
        return f"{self.nome.ljust(20)}\t€ {self.orcamento} milhões\tChance de Campeão: {self.chance_campeao}%\tPontos: {self.pontos}"

class Campeonato:
    def __init__(self, times):
        self.times = times
        self.partidas = self.gerar_partidas()

    def exibir_times(self):
        print("Times no Brasileirão:")
        for i, time in enumerate(self.times, 1):
            print(f"{i}. {time.nome}")

    def escolher_time(self, escolha):
        return self.times[escolha - 1] if 1 <= escolha <= len(self.times) else None

    def contratar_jogador(self, time, jogador):
        if jogador.valor <= time.orcamento:
            if time.orcamento - jogador.valor >= 0:
                time.jogadores.append(jogador)
                time.orcamento -= jogador.valor
                if jogador.categoria == "Craque":
                    time.chance_campeao += 10
                elif jogador.categoria == "Bom":
                    time.chance_campeao += 5
                else:
                    time.chance_campeao += 3

    def gerar_partidas(self):
        partidas = []
        for i in range(len(self.times)):
            for j in range(i + 1, len(self.times)):
                partidas.append((self.times[i], self.times[j]))
                partidas.append((self.times[j], self.times[i]))
        return partidas

    def simular_partidas(self, num_rodadas):
        for rodada in range(1, num_rodadas + 1):
            for partida in self.partidas:
                time1, time2 = partida
                resultado = random.choice(["Vitória", "Empate", "Derrota"])
                if resultado == "Vitória":
                    time1.pontos += 3
                elif resultado == "Empate":
                    time1.pontos += 1
                    time2.pontos += 1
                else:
                    time2.pontos += 3

    def classificar_times(self):
        times_ordenados = sorted(self.times, key=lambda x: x.pontos, reverse=True)
        classificacao = []

        for i, time in enumerate(times_ordenados, 1):
            classificacao.append(f"{i}. {time.nome}: {time.pontos} pontos")

            if i <= 4:
                classificacao.append(f"{time.nome} se classificou para a Libertadores!")
            elif 5 <= i <= 8:
                classificacao.append(f"{time.nome} se classificou para a Sul-Americana.")
            elif i == len(self.times):
                classificacao.append(f"{time.nome} foi rebaixado para a Série B.")

        return "\n".join(classificacao)

    def exibir_tabela(self):
        print("\nTabela Final do Campeonato:")
        print("Posição\tTime\t\t\t\tPontos")
        times_ordenados = sorted(self.times, key=lambda x: x.pontos, reverse=True)
        for i, time in enumerate(times_ordenados, 1):
            print(f"{i}\t\t{time.exibir_informacoes()}")

        # Adiciona a classificação ao final das partidas
        print(self.classificar_times())

def criar_jogadores():
    jogadores = [
        Jogador(1, "Goleiro", "Alisson", "Liverpool", 1.5, "Craque"),
        Jogador(2, "Lateral-direito", "João Cancelo", "Manchester City", 1.2, "Craque"),
        Jogador(3, "Zagueiro", "Virgil van Dijk", "Liverpool", 2.0, "Craque"),
        Jogador(4, "Meia", "Kevin De Bruyne", "Manchester City", 2.5, "Craque"),
        Jogador(5, "Goleiro", "Hugo Lloris", "Tottenham", 1.3, "Bom"),
        Jogador(6, "Lateral-esquerdo", "Alex Grimaldo", "Benfica", 1.0, "Bom"),
        Jogador(7, "Volante", "Declan Rice", "West Ham", 0.8, "Bom"),
        Jogador(8, "Atacante", "Kylian Mbappé", "Paris Saint-Germain", 3.0, "Craque"),
        Jogador(9, "Goleiro", "Kepa Arrizabalaga", "Chelsea", 1.7, "Bom"),
        Jogador(10, "Lateral-direito", "Diogo Dalot", "Manchester United", 0.9, "Bom"),
        Jogador(11, "Zagueiro", "Raphaël Varane", "Manchester United", 2.2, "Craque"),
        Jogador(12, "Atacante", "Ousmane Dembélé", "Barcelona", 1.6, "Bom"),
    ]
    return jogadores

def criar_times_brasileirao():
    times_brasileirao = [
        Time("Palmeiras", 24.11),
        Time("Atlético Mineiro", 9),
        Time("Botafogo", 8.2),
        Time("Athletico Paranaense", 7),
        Time("Fluminense", 6.4),
        Time("Cuiabá", 5.3),
        Time("Red Bull Bragantino", 4.8),
        Time("Corinthians", 150.9),  # Aumentando a chance de o Corinthians ser campeão
        Time("São Paulo", 3.8),
        Time("Ceará", 3.6),
        Time("Fortaleza", 2.9),
        Time("América Mineiro", 2.8),
        Time("Santos", 2.5),
        Time("Internacional", 2.1),
        Time("Juventude", 1.6),
        Time("Avaí", 1.5),
        Time("Goiás", 1.3),
        Time("Grêmio", 0.6),
        Time("Cruzeiro", 0.2),
        Time("Flamengo", -1.8),
        Time("Vasco da Gama", -6.79),
    ]
    return times_brasileirao

def main():
    jogadores = criar_jogadores()
    times_brasileirao = criar_times_brasileirao()
    campeonato_brasileirao = Campeonato(times_brasileirao)

    campeonato_brasileirao.exibir_times()
    escolha_time_usuario = int(input("Escolha um time do Brasileirão (digite o número): "))
    time_selecionado = campeonato_brasileirao.escolher_time(escolha_time_usuario)

    if time_selecionado:
        print(f"\nVocê escolheu o time {time_selecionado.nome}.")
        print(f"Orçamento do time: € {time_selecionado.orcamento} milhões")

        while True:
            if time_selecionado.orcamento <= 0:
                print(f"Orçamento do time {time_selecionado.nome} estourado. Não é possível contratar mais jogadores.")
                break

            print("\nJogadores disponíveis:")
            jogadores_disponiveis = [jogador for jogador in jogadores if jogador not in time_selecionado.jogadores]
            for jogador in jogadores_disponiveis:
                jogador.exibir_informacoes()

            escolha_jogador_usuario = int(input("\nEscolha um jogador para contratar (digite o número, 0 para sair): "))

            if escolha_jogador_usuario == 0:
                break

            if 1 <= escolha_jogador_usuario <= len(jogadores_disponiveis):
                jogador_selecionado = jogadores_disponiveis[escolha_jogador_usuario - 1]
                campeonato_brasileirao.contratar_jogador(time_selecionado, jogador_selecionado)
            else:
                print("Escolha de jogador inválida. Por favor, escolha um jogador válido.")

        # Simular 32 partidas
        campeonato_brasileirao.simular_partidas(32)

        # Exibir tabela após as partidas
        campeonato_brasileirao.exibir_tabela()

    else:
        print("Escolha de time inválida. Por favor, escolha um time válido.")

if __name__ == "__main__":
    main()
