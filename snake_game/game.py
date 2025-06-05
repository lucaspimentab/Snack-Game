import pygame
from login import LoginScreen
from entities.snake import Snake
from entities.apple import Apple

class Game:
    def __init__(self):
        pygame.init()
        self.largura, self.altura = 660, 600
        self.tela = pygame.display.set_mode((self.largura, self.altura))
        pygame.display.set_caption("Jogo da Cobrinha")
        self.clock = pygame.time.Clock()
        self.fonte = pygame.font.SysFont(None, 36)
        self.jogador = ""
        self.reset()

    def reset(self):
        self.snake = Snake()
        self.apple = Apple(self.largura, self.altura)

    def mostrar_game_over(self):
        texto = self.fonte.render(f"Game Over, {self.jogador}!", True, (255, 255, 255))
        self.tela.blit(texto, (180, 250))
        pygame.display.flip()
        pygame.time.wait(2000)

    def run(self):
        login = LoginScreen(self.tela)
        self.jogador = login.run()

        while True:
            self.clock.tick(10)
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    pygame.quit()
                    return
                if evento.type == pygame.KEYDOWN:
                    self.snake.mudar_direcao(evento.key)

            self.snake.mover()

            if self.snake.colidiu_com(self.apple.get_pos()):
                self.snake.crescer()
                self.apple.gerar_nova_posicao()

            if self.snake.bateu_na_parede(self.largura, self.altura) or self.snake.colidiu_consigo():
                self.mostrar_game_over()
                self.reset()

            self.tela.fill((0, 0, 0))
            self.snake.desenhar(self.tela)
            self.apple.desenhar(self.tela)
            pygame.display.update()
