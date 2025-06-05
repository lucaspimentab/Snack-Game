import pygame
import random
from entities.entity import Entity

class Apple(Entity):
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura
        self.pos = self.gerar_nova_posicao()

    def gerar_nova_posicao(self):
        x = random.randint(0, self.largura - 10)
        y = random.randint(0, self.altura - 10)
        self.pos = (x // 10 * 10, y // 10 * 10)
        return self.pos

    def desenhar(self, tela):
        pygame.draw.rect(tela, (255, 0, 0), (*self.pos, 10, 10))

    def get_pos(self):
        return self.pos
