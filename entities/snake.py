import pygame
from pygame.locals import *
from entities.entity import Entity

class Snake(Entity):
    def __init__(self):
        self.corpo = [(300, 300)]
        self.direcao = K_RIGHT

    def mover(self):
        x, y = self.corpo[0]
        if self.direcao == K_RIGHT:
            x += 10
        elif self.direcao == K_LEFT:
            x -= 10
        elif self.direcao == K_UP:
            y -= 10
        elif self.direcao == K_DOWN:
            y += 10

        self.corpo = [(x, y)] + self.corpo[:-1]

    def mudar_direcao(self, tecla):
        if tecla in [K_UP, K_DOWN, K_LEFT, K_RIGHT]:
            self.direcao = tecla

    def crescer(self):
        self.corpo.append(self.corpo[-1])

    def desenhar(self, tela):
        for parte in self.corpo:
            pygame.draw.rect(tela, (255, 255, 255), (*parte, 10, 10))

    def get_pos(self):
        return self.corpo[0]

    def bateu_na_parede(self, largura, altura):
        x, y = self.corpo[0]
        return not (0 <= x < largura and 0 <= y < altura)

    def colidiu_consigo(self):
        return self.corpo[0] in self.corpo[1:]

    def colidiu_com(self, pos):
        return self.corpo[0] == pos
