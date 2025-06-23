import flet as ft
import asyncio
from interface.componentes.notificador import Notificador
from interface.componentes.box import CaixaCentral
from interface.componentes.botoes import BotaoVerde, BotaoTextoCinza
from interface.componentes.cabecalho import Cabecalho
from interface.estilos import Cores as Cor
from typing import Callable

class TelaMenuUsuario:
    """
    Tela de menu principal do usuário logado.

    Apresenta opções como iniciar o jogo, ver o ranking e fazer logout.
    Também exibe o nome do usuário atualmente autenticado.
    """

    def __init__(
        self,
        usuario_nome         : str,
        iniciar_jogo         : Callable[[], None],
        navegar_para_ranking : Callable[[], None],
        logout               : Callable[[], None]
    ):
        """
        Inicializa a tela do menu do usuário com os botões e layout.

        Args:
            usuario_nome (str): Nome do usuário logado, exibido na tela.
            iniciar_jogo (Callable): Função para iniciar o jogo.
            navegar_para_ranking (Callable): Função que navega para a tela de ranking.
            logout (Callable): Função que realiza logout e volta para o login.
        """
        self.notificador = Notificador()
        self.iniciar_jogo = iniciar_jogo
        self.navegar_para_ranking = navegar_para_ranking
        self.logout = logout

        # Botões principais do menu
        botao_jogar = BotaoVerde("Jogar", self.avisar_e_jogar)
        botao_ranking = BotaoTextoCinza("Ranking", lambda _: self.navegar_para_ranking())
        botao_logout = BotaoTextoCinza("Logout", lambda _: self.logout())

        # Layout interno da caixa central
        conteudo = ft.Column(
            [
                ft.Text(
                    f"Bem-vindo(a), {usuario_nome}!",
                    size   = 20,
                    weight = "w500",
                    color  = Cor.CINZA_TEXTO
                ),
                ft.Container(height = 10),
                botao_jogar,
                ft.Container(height = 10),
                botao_ranking,
                ft.Container(height = 10),
                botao_logout
            ],
            spacing = 10,
            alignment = "center",
            horizontal_alignment = "center"
        )
        layout = CaixaCentral(conteudo)

        # Composição geral da view do menu
        self.view = ft.Container(
            content = ft.Column(
                [
                    Cabecalho(),
                    ft.Container(height = 20),
                    layout,
                    ft.Container(height = 20),
                    self.notificador.get_snackbar()
                ],
                alignment = "center",
                horizontal_alignment = "center",
                expand = True
            ),
            expand = True,
            alignment = ft.alignment.center
        )

    async def avisar_e_jogar(self, e: ft.ControlEvent) -> None:
        """
        Exibe uma mensagem informando que o jogo será aberto em nova janela e inicia o jogo após 1.5s.

        Args:
            e (ft.ControlEvent): Evento de clique no botão "Jogar".
        """
        self.notificador.info(e.page, "O jogo será aberto em uma nova janela.")
        await asyncio.sleep(1.5)
        self.iniciar_jogo()
