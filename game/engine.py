import pygame
import sys
import json
from models.snake import Snake
from models.apple import Apple
from utils.config import DB_PATH
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
        """
        pygame.init()

        self.largura, self.altura = 660, 600
        self.tela = pygame.display.set_mode((self.largura, self.altura))
        pygame.display.set_caption("Snake Game - Executável")
        self.clock = pygame.time.Clock()
        self.fonte = pygame.font.SysFont(None, 36)
        self.jogador = sys.argv[1] if len(sys.argv) > 1 else "Jogador"
        self.score = 0

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
        Exibe a mensagem de fim de jogo, salva o score e pausa por 2 segundos.
        """
        logger.info(f"Game over! {self.jogador} fez {self.score} ponto(s)")
        self.salvar_score()
        texto = self.fonte.render(
            f"Game Over, {self.jogador}!", 
            True, 
            Cor.rgb(Cor.CINZA_TEXTO)
        )
        self.tela.blit(texto, (180, 250))
        pygame.display.flip()
        pygame.time.wait(2000)

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
        self.tela.blit(texto, (450, 10))

    def run(self):
        """
        Inicia o loop principal do jogo, tratando eventos, atualizando estados e desenhando a tela.
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
                    self.snake.mudar_direcao(evento.key)
                    logger.debug(f"Direcao alterada: {evento.key}")

            self.snake.mover()

            if self.snake.colidiu_com(self.apple.get_pos()):
                self.snake.crescer()
                self.apple.gerar_nova_posicao(self.snake.corpo)
                self.score += 1
                logger.info(f"{self.jogador} pegou uma maca! Score: {self.score}")

            if self.snake.bateu_na_parede(self.largura, self.altura) or self.snake.colidiu_consigo():
                logger.info("Colisao detectada. Reiniciando jogo...")
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
