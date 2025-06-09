import pygame
import sys
import json
import os
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
        self.jogador = sys.argv[1] if len(sys.argv) > 1 else "Jogador"
        self.score = 0
        self.reset()

    def reset(self):
        self.snake = Snake()
        self.apple = Apple(self.largura, self.altura)
        self.apple.gerar_nova_posicao(self.snake.corpo)
        self.score = 0

    def mostrar_game_over(self):
        self.salvar_score()
        texto = self.fonte.render(f"Game Over, {self.jogador}!", True, (255, 255, 255))
        self.tela.blit(texto, (180, 250))
        pygame.display.flip()
        pygame.time.wait(2000)

    def salvar_score(self):
        os.makedirs("database", exist_ok=True)
        path = "database/ranking.json"
        if os.path.exists(path):
            with open(path, "r", encoding="utf-8") as f:
                dados = json.load(f)
        else:
            dados = {}

        if self.jogador in dados:
            dados[self.jogador] = max(dados[self.jogador], self.score)
        else:
            dados[self.jogador] = self.score

        with open(path, "w", encoding="utf-8") as f:
            json.dump(dados, f, indent=2)

    def desenhar_score(self):
        texto = self.fonte.render(f"Score: {self.score}", True, (255, 255, 0))
        self.tela.blit(texto, (10, 10))

    def desenhar_sair(self):
        texto = self.fonte.render("ESC para sair", True, (150, 150, 150))
        self.tela.blit(texto, (450, 10))

    def run(self):
        while True:
            self.clock.tick(10)
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    pygame.quit()
                    return
                if evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_ESCAPE:
                        pygame.quit()
                        return
                    self.snake.mudar_direcao(evento.key)

            self.snake.mover()

            if self.snake.colidiu_com(self.apple.get_pos()):
                self.snake.crescer()
                self.apple.gerar_nova_posicao(self.snake.corpo)
                self.score += 1

            if self.snake.bateu_na_parede(self.largura, self.altura) or self.snake.colidiu_consigo():
                self.mostrar_game_over()
                self.reset()

            self.tela.fill((0, 0, 0))
            self.snake.desenhar(self.tela)
            self.apple.desenhar(self.tela)
            self.desenhar_score()
            self.desenhar_sair()
            pygame.display.update()

if __name__ == "__main__":
    try:
        Game().run()
    except Exception as e:
        print("Erro ao iniciar o jogo:", e)
        input("Pressione Enter para sair...")
