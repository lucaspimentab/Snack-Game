import flet as ft
from services.ranking import RankingService
from services.login import AuthService
from interface.componentes.box import CaixaCentral
from interface.componentes.botoes import BotaoTextoCinza
from interface.componentes.cabecalho import Cabecalho
from interface.estilos import Cores as Cor

class TelaRanking:
    """
    Tela de exibição do ranking com os 3 maiores scores e o score do usuário atual.
    """

    def __init__(self, voltar_para_menu):
        """
        Inicializa a tela de ranking.

        Args:
            voltar_para_menu (Callable): Função para retornar ao menu principal.
        """
        self.voltar_para_menu = voltar_para_menu
        self.ranking_service = RankingService()
        self.usuario = AuthService.get_usuario_logado()

        top_3 = self.ranking_service.top_3()
        usuario_score = self.ranking_service.get_score_usuario_logado()

        # Título da seção
        titulo = ft.Text(
            "TOP 3 jogadores", 
            size   = 24, 
            weight = "bold", 
            color  = Cor.VERDE_ESCURO
        )

        # Lista com os 3 melhores jogadores
        lista_top = ft.Column(
            [
                ft.Text(f"{i + 1}. {nome}: {score} pts", size = 18)
                for i, (nome, score) in enumerate(top_3)
            ],
            spacing = 5
        )

        # Score do usuário atual
        score_pessoal = ft.Text(
            f"Seu score: {usuario_score} pts",
            size  = 18,
            weight = "bold",
            color  = Cor.CINZA_TEXTO
        )

        # Botão para voltar ao menu
        botao_voltar = BotaoTextoCinza("Voltar", lambda _: self.voltar_para_menu())

        # Layout do conteúdo central
        conteudo = ft.Column(
            [
                titulo,
                ft.Container(height = 10),
                lista_top,
                ft.Container(height = 20),
                score_pessoal,
                ft.Container(height = 20),
                botao_voltar
            ],
            spacing = 10,
            alignment = "center",
            horizontal_alignment = "center"
        )
        layout = CaixaCentral(conteudo)

        # Composição completa da view
        self.view = ft.Container(
            expand = True,
            content = ft.Column(
                [
                    Cabecalho(),
                    ft.Container(height = 20),
                    layout,
                ],
                alignment = "center",
                horizontal_alignment = "center",
                expand = True
            ),
            alignment = ft.alignment.center
        )
