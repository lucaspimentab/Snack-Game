import pygame
from pygame.locals import *
from utils.logger import logger
from interface.estilos import Cores as Cor

class Snake:
    """
    Representa a cobra no jogo.

    Responsável por movimentar, crescer, detectar colisões e se desenhar na tela.
    """

    def __init__(self):
        """
        Inicializa a cobra com uma posição inicial e direção para a direita.

        Atributos:
            _corpo (list): Lista de tuplas representando os segmentos da cobra.
            _direcao (int): Direção atual de movimento (constante do pygame, ex: K_RIGHT).
            _crescer_na_proxima (bool): Indica se a cobra deve crescer no próximo movimento.
        """
        self._corpo = [(300, 300)]
        self._direcao = K_RIGHT
        self._crescer_na_proxima = False
        logger.info("Cobra criada na posicao (300, 300) com direcao inicial para a direita.")

    @property
    def corpo(self):
        """
        Retorna os segmentos atuais da cobra.

        Returns:
            list: Lista de tuplas (x, y) com as posições dos segmentos.
        """
        return self._corpo

    def mover(self):
        """
        Move a cobra de acordo com a direção atual.

        Se estiver marcada para crescer, ela aumenta de tamanho ao mover.
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
        Altera a direção da cobra, ignorando comandos que fariam ela voltar para trás.

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
        Desenha todos os segmentos da cobra na tela.

        Args:
            tela (pygame.Surface): Superfície onde os segmentos serão desenhados.
        """
        for parte in self._corpo:
            pygame.draw.rect(
                tela, Cor.rgb(Cor.VERDE_MEDIO), (*parte, 10, 10)
            )

    def get_pos(self):
        """
        Retorna a posição da cabeça da cobra.

        Returns:
            tuple: Coordenadas (x, y) da cabeça.
        """
        return self._corpo[0]

    def bateu_na_parede(self, largura, altura):
        """
        Verifica se a cobra colidiu com os limites da tela.

        Args:
            largura (int): Largura da área de jogo.
            altura (int): Altura da área de jogo.

        Returns:
            bool: True se a cabeça estiver fora dos limites, False caso contrário.
        """
        x, y = self.corpo[0]
        colidiu = not (0 <= x < largura and 0 <= y < altura)
        if colidiu:
            logger.warning(f"Cobra bateu na parede na posicao ({x}, {y})")
        return colidiu

    def colidiu_consigo(self):
        """
        Verifica se a cobra colidiu com o próprio corpo.

        Returns:
            bool: True se a cabeça estiver sobre outro segmento, False caso contrário.
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
            bool: True se colidiu com a posição fornecida, False caso contrário.
        """
        return self._corpo[0] == pos
