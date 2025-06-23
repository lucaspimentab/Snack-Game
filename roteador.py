import flet as ft
from utils.logger import logger
from interface.telas.tela_cadastro import TelaCadastro
from interface.telas.tela_login import TelaLogin
from interface.telas.tela_menu import TelaMenuUsuario
from interface.telas.tela_ranking import TelaRanking
from services.login import AuthService
from game.game_runner import GameRunner as Game

class Roteador:
    """
    Gerencia a navegação entre as diferentes telas do aplicativo.
    """

    def __init__(self, page: ft.Page):
        """
        Inicializa o roteador com a página principal do app.

        Args:
            page (ft.Page): A instância da página Flet usada para navegação.
        """
        self.page = page

    def navegar(self, route: str, *args) -> None:
        """
        Navega para a rota especificada, carregando a tela correspondente.

        Args:
            route (str): Caminho da rota (por exemplo, "/", "/cadastro").
            *args: Argumentos adicionais opcionais para rotas futuras.
        """
        logger.info(f"Navegando para a rota: {route}")
        self.page.views.clear()

        #---------------------------------------------------
        # Rota principal (login)
        if route == "/":
            tela = TelaLogin(
                navegar_para_menu = lambda: self.page.go("/menu"),
                navegar_para_cadastro = lambda: self.page.go("/cadastro")
            )
            self.page.views.append(ft.View("/", controls = [tela.view]))

        #---------------------------------------------------
        # Rota de cadastro de usuário
        elif route == "/cadastro":
            tela = TelaCadastro(
                navegar_para_login = lambda: self.page.go("/")
            )
            self.page.views.append(ft.View("/cadastro", controls = [tela.view]))

        #---------------------------------------------------
        # Rota do menu do usuário
        elif route == "/menu":
            usuario = AuthService.get_usuario_logado()
            if not usuario:
                logger.warning("Acesso ao menu sem login. Redirecionando para login.")
                self.page.go("/")
                return

            tela = TelaMenuUsuario(
                usuario_nome = usuario.nome,
                iniciar_jogo = lambda: Game(usuario).iniciar_jogo(),
                navegar_para_ranking = lambda: self.page.go("/ranking"),
                logout = self._fazer_logout
            )
            self.page.views.append(ft.View("/menu", controls = [tela.view]))

        #---------------------------------------------------
        # Rota de ranking
        elif route == "/ranking":
            if not AuthService.esta_logado():
                logger.warning("Acesso ao ranking sem login. Redirecionando para login.")
                self.page.go("/")
                return

            tela = TelaRanking(voltar_para_menu = lambda: self.page.go("/menu"))
            self.page.views.append(ft.View("/ranking", controls = [tela.view]))

        self.page.update()

    def _fazer_logout(self) -> None:
        """
        Realiza logout do usuário e redireciona para a tela de login.
        """
        AuthService.logout()
        self.page.go("/")
