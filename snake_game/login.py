import pygame

class LoginScreen:
    def __init__(self, tela):
        self.tela = tela
        self.fonte = pygame.font.SysFont(None, 36)
        self.nome = ""
        self.ativo = True

    def run(self):
        while self.ativo:
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_RETURN and self.nome.strip():
                        self.ativo = False
                    elif evento.key == pygame.K_BACKSPACE:
                        self.nome = self.nome[:-1]
                    elif len(self.nome) < 15:
                        self.nome += evento.unicode

            self.tela.fill((0, 0, 0))
            texto = self.fonte.render("Digite seu nome e pressione Enter:", True, (255, 255, 255))
            nome_txt = self.fonte.render(self.nome, True, (255, 0, 0))
            self.tela.blit(texto, (100, 200))
            self.tela.blit(nome_txt, (100, 250))
            pygame.display.flip()
        return self.nome
