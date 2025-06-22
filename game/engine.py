import pygame
import sys
import json
from models.snake import Snake
from models.apple import Apple
from utils.config import DB_PATH, SOUNDTRACK_PATH, SOUNDEFFECT_PATH
from models.usuario import Usuario
from utils.logger import logger
from interface.estilos import Cores as Cor

class Game:
    """
    Classe principal do jogo (Snake Game).

    Responsável por inicializar o Pygame, gerenciar entidades do jogo,
    controle de fluxo, exibição, score e persistência dos dados do jogador.
    """

    def __init__(self):
        """
        Inicializa o jogo e todos os recursos necessários.

        Attributes:
            largura (int): Largura da tela do jogo.
            altura (int): Altura da tela do jogo.
            tela (pygame.Surface): Superfície principal do jogo.
            clock (pygame.time.Clock): Objeto para controlar a taxa de atualização do jogo.
            fonte (pygame.font.Font): Fonte usada para textos na tela.
            jogador (str): Nome do jogador atual.
            score (int): Pontuação atual do jogador.
            snake (Snake): Instância da cobra.
            apple (Apple): Instância da maçã.
            pausado (bool): Estado do jogo.
        """
        pygame.init()
        
        # Configurações da trilha sonora
        pygame.mixer.init()
        pygame.mixer.music.load(str(SOUNDTRACK_PATH))
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.music.play(-1)
        self.som_ao_comer = pygame.mixer.Sound(str(SOUNDEFFECT_PATH))

        self.largura, self.altura = 520, 450
        self.tela = pygame.display.set_mode((self.largura, self.altura))
        pygame.display.set_caption("Snake Game - Executável")
        self.clock = pygame.time.Clock()
        self.fonte = pygame.font.SysFont(None, 36)
        self.jogador = sys.argv[1] if len(sys.argv) > 1 else "Jogador"
        self.score = 0
        self.pausado = False

        logger.info(f"Jogo iniciado para o jogador: {repr(self.jogador)}")
        self.reset()

    def reset(self):
        """
        Reinicia o estado do jogo: cobra, maçã e pontuação.
        """
        self.snake = Snake()
        self.apple = Apple(self.largura, self.altura)
        self.apple.gerar_nova_posicao(self.snake.corpo)
        self.score = 0
        logger.debug("Jogo resetado: entidades reiniciadas")

    def mostrar_game_over(self):
        """
        Exibe a mensagem de fim de jogo, salva o score e aguarda o jogador pressionar ENTER.
        """
        logger.info(f"Game over! Aguardando restart...")
        self.salvar_score()

        self.tela.fill(Cor.rgb(Cor.VERDE_CLARO))

        texto1 = self.fonte.render(f"Game Over, {self.jogador}!", True, Cor.rgb(Cor.VERDE_ESCURO))
        rect1 = texto1.get_rect(center=(self.largura // 2, self.altura // 2 - 30))
        self.tela.blit(texto1, rect1)

        texto2 = self.fonte.render("Pressione ENTER para jogar novamente", True, Cor.rgb(Cor.CINZA_TEXTO))
        rect2 = texto2.get_rect(center=(self.largura // 2, self.altura // 2 + 30))
        self.tela.blit(texto2, rect2)

        pygame.display.flip()

        # Espera o jogador apertar ENTER ou ESC
        esperando = True
        while esperando:
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_RETURN:
                        esperando = False
                    if evento.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()

    def salvar_score(self):
        """
        Salva o score do jogador no arquivo JSON, caso o novo score seja maior.
        """
        if not DB_PATH.exists():
            logger.warning(f"Arquivo de usuarios não encontrado em {DB_PATH}")
            return

        with open(DB_PATH, "r", encoding="utf-8") as f:
            usuarios_dict = json.load(f)

        if self.jogador not in usuarios_dict:
            logger.warning(f"Usuario '{self.jogador}' nao encontrado para salvar score.")
            return

        usuario = Usuario.from_dict(self.jogador, usuarios_dict[self.jogador])
        logger.debug(f"Score anterior de {self.jogador}: {usuario.score}")

        usuario.score = self.score
        usuarios_dict[self.jogador] = usuario.to_dict()

        with open(DB_PATH, "w", encoding="utf-8") as f:
            json.dump(usuarios_dict, f, indent=2)

        logger.info(f"Score de {self.jogador} atualizado para {self.score}")

    def desenhar_score(self):
        """
        Desenha o score atual na tela.
        """
        texto = self.fonte.render(
            f"Score: {self.score}", 
            True, 
            Cor.rgb(Cor.VERDE_ESCURO)
        )
        self.tela.blit(texto, (10, 10))

    def desenhar_sair(self):
        """
        Desenha a instrução para sair do jogo (ESC).
        """
        texto = self.fonte.render(
            "ESC para sair", 
            True, 
            Cor.rgb(Cor.CINZA_TEXTO)
        )
        pos_texto = texto.get_rect(topright = (self.largura - 10, 10))
        self.tela.blit(texto, pos_texto)

    def run(self):
        """
        Inicia o loop principal do jogo, tratando eventos, 
        atualizando estados e desenhando a tela.
        """
        logger.info("Loop principal iniciado")
        while True:
            self.clock.tick(10)
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    logger.info("Jogo encerrado pelo botao de fechar")
                    pygame.quit()
                    return

                if evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_ESCAPE:
                        logger.info("Jogo encerrado com ESC")
                        pygame.quit()
                        return

                    if evento.key == pygame.K_SPACE:
                        self.pausado = not self.pausado
                        estado = "Pausado" if self.pausado else "Retomado"
                        logger.info(f"Jogo {estado.lower()}")

                        # Pausa/Despausa a música
                        if self.pausado:
                            pygame.mixer.music.pause()
                        else:
                            pygame.mixer.music.unpause()

                    self.snake.mudar_direcao(evento.key)
                    logger.debug(f"Direcao alterada: {evento.key}")

            if self.pausado:
                self.tela.fill(Cor.rgb(Cor.VERDE_CLARO))
                self.snake.desenhar(self.tela)
                self.apple.desenhar(self.tela)
                self.desenhar_score()
                self.desenhar_sair()

                texto = self.fonte.render("PAUSADO", True, Cor.rgb(Cor.CINZA_TEXTO))
                pos_texto = texto.get_rect(
                    center = (self.largura // 2, self.altura // 2)
                )
                self.tela.blit(texto, pos_texto)
                pygame.display.update()
                continue

            self.snake.mover()

            if self.snake.colidiu_com(self.apple.get_pos()):
                self.som_ao_comer.play()
                self.snake.crescer()
                self.apple.gerar_nova_posicao(self.snake.corpo)
                self.score += 1
                logger.info(f"{self.jogador} pegou uma maca! Score: {self.score}")

            if self.snake.bateu_na_parede(self.largura, self.altura) or self.snake.colidiu_consigo():
                logger.info("Colisao detectada!")
                self.mostrar_game_over()
                self.reset()

            self.tela.fill(Cor.rgb(Cor.VERDE_CLARO))
            self.snake.desenhar(self.tela)
            self.apple.desenhar(self.tela)
            self.desenhar_score()
            self.desenhar_sair()
            pygame.display.update()

if __name__ == "__main__":
    try:
        Game().run()
    except Exception as e:
        logger.exception("Erro ao iniciar o jogo:")
        input("Pressione Enter para sair...")
