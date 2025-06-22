import pygame
from pygame.locals import *
from utils.logger import logger
from interface.estilos import Cores as Cor

class Snake:
    """
    Representa a cobra no jogo da cobrinha.

    Controla a movimentação, crescimento, colisões e renderização da cobra na tela.
    """

    def __init__(self):
        """
        Inicializa a cobra com uma posição inicial e direção à direita.

        Attributes:
            _corpo (list): Lista de tuplas representando as posições dos segmentos da cobra.
            _direcao (int): Direção atual de movimento (valores de pygame.locals, como K_RIGHT).
            _crescer_na_proxima (bool): Marca se a cobra deve crescer no próximo movimento.
        """
        self._corpo = [(300, 300)]
        self._direcao = K_RIGHT
        self._crescer_na_proxima = False
        logger.info("Cobra criada na posicao (300, 300) com direcao inicial para a direita.")

    @property
    def corpo(self):
        """
        Retorna a lista de segmentos que compõem o corpo da cobra.

        Returns:
            list: Lista de tuplas (x, y) representando cada segmento da cobra.
        """
        return self._corpo

    def mover(self):
        """
        Move a cobra na direção atual.

        Se a cobra estiver marcada para crescer, ela aumenta de tamanho; caso contrário, apenas se move.
        """
        x, y = self._corpo[0]
        if self._direcao == K_RIGHT:
            x += 10
        elif self._direcao == K_LEFT:
            x -= 10
        elif self._direcao == K_UP:
            y -= 10
        elif self._direcao == K_DOWN:
            y += 10

        nova_cabeca = (x, y)

        if self._crescer_na_proxima:
            self._corpo = [nova_cabeca] + self._corpo
            self._crescer_na_proxima = False
            logger.debug(f"Cobra cresceu para {len(self._corpo)} segmentos")
        else:
            self._corpo = [nova_cabeca] + self._corpo[:-1]

    def mudar_direcao(self, tecla):
        """
        Altera a direção da cobra, evitando movimentos de 180 graus.

        Args:
            tecla (int): Código da tecla pressionada (ex: K_UP, K_LEFT).
        """
        if tecla == K_LEFT and self._direcao == K_RIGHT:
            return
        if tecla == K_RIGHT and self._direcao == K_LEFT:
            return
        if tecla == K_UP and self._direcao == K_DOWN:
            return
        if tecla == K_DOWN and self._direcao == K_UP:
            return

        if tecla in [K_UP, K_DOWN, K_LEFT, K_RIGHT]:
            logger.debug(f"Direcao alterada para {self._direcao}")
            self._direcao = tecla

    def crescer(self):
        """
        Marca a cobra para crescer no próximo movimento.
        """
        self._crescer_na_proxima = True

    def desenhar(self, tela):
        """
        Desenha a cobra na tela.

        Args:
            tela (pygame.Surface): Superfície onde a cobra será desenhada.
        """
        for parte in self._corpo:
            pygame.draw.rect(
                tela, Cor.rgb(Cor.VERDE_MEDIO), (*parte, 10, 10)
            )

    def get_pos(self):
        """
        Retorna a posição da cabeça da cobra.

        Returns:
            tuple: Coordenadas (x, y) da cabeça da cobra.
        """
        return self._corpo[0]

    def bateu_na_parede(self, largura, altura):
        """
        Verifica se a cobra colidiu com as bordas da tela.

        Args:
            largura (int): Largura da área de jogo.
            altura (int): Altura da área de jogo.

        Returns:
            bool: True se a cobra bateu na parede, False caso contrário.
        """
        x, y = self.corpo[0]
        colidiu = not (0 <= x < largura and 0 <= y < altura)
        if colidiu:
            logger.warning(f"Cobra bateu na parede na posicao ({x}, {y})")
        return colidiu

    def colidiu_consigo(self):
        """
        Verifica se a cobra colidiu com seu próprio corpo.

        Returns:
            bool: True se colidiu com ela mesma, False caso contrário.
        """
        colidiu = self.corpo[0] in self.corpo[1:]
        if colidiu:
            logger.warning("Cobra colidiu consigo mesma.")
        return colidiu

    def colidiu_com(self, pos):
        """
        Verifica se a cabeça da cobra colidiu com uma posição específica.

        Args:
            pos (tuple): Posição (x, y) a ser verificada.

        Returns:
            bool: True se a cabeça da cobra estiver na posição, False caso contrário.
        """
        return self._corpo[0] == pos
