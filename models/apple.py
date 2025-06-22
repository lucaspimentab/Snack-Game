import pygame
import random
from utils.logger import logger
from interface.estilos import Cores as Cor

class Apple:
    """
    Representa uma maçã no jogo da cobrinha.

    Responsável por gerar posições válidas para a maçã e desenhá-la na tela.

    Attributes:
        tamanho (int): Tamanho da maçã em pixels.
        largura (int): Largura da área de jogo.
        altura (int): Altura da área de jogo.
        x (int): Posição X atual da maçã.
        y (int): Posição Y atual da maçã.
    """

    def __init__(self, largura, altura):
        """
        Inicializa uma nova instância de Apple.

        Args:
            largura (int): Largura da área de jogo.
            altura (int): Altura da área de jogo.
        """
        self.tamanho = 10
        self.largura = largura
        self.altura = altura
        self.x = 0
        self.y = 0

    def gerar_nova_posicao(self, corpo_cobra):
        """
        Gera uma nova posição aleatória para a maçã, evitando colisão com o corpo da cobra.

        Args:
            corpo_cobra (list): Lista de tuplas com as posições ocupadas pelo corpo da cobra.
        """
        while True:
            x = random.randint(0, (self.largura - self.tamanho) // 10) * 10
            y = random.randint(0, (self.altura - self.tamanho) // 10) * 10
            if (x, y) not in corpo_cobra:
                self.x, self.y = x, y
                logger.info(f"Nova maca gerada em ({self.x}, {self.y})")
                break

    def get_pos(self):
        """
        Retorna a posição atual da maçã.

        Returns:
            tuple: Tupla (x, y) com a posição da maçã.
        """
        return (self.x, self.y)

    def desenhar(self, tela):
        """
        Desenha a maçã na tela.

        Args:
            tela (pygame.Surface): Superfície onde a maçã será desenhada.
        """
        pygame.draw.rect(
            tela, 
            Cor.rgb(Cor.VERMELHO), 
            (self.x, self.y, self.tamanho, self.tamanho)
        )
