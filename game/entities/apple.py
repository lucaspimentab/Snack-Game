import pygame
import random

class Apple:
    def __init__(self, largura, altura):
        self.tamanho = 10
        self.largura = largura
        self.altura = altura
        self.x = 0
        self.y = 0

    def gerar_nova_posicao(self, corpo_cobra):
        while True:
            x = random.randint(0, (self.largura - self.tamanho) // 10) * 10
            y = random.randint(0, (self.altura - self.tamanho) // 10) * 10
            if (x, y) not in corpo_cobra:
                self.x, self.y = x, y
                break

    def get_pos(self):
        return (self.x, self.y)

    def desenhar(self, tela):
        pygame.draw.rect(tela, (255, 0, 0), (self.x, self.y, self.tamanho, self.tamanho))
