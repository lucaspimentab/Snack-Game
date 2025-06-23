import flet as ft
import asyncio
from services.login import AuthService
from interface.componentes.notificador import Notificador
from interface.componentes.input import InputTextoPersonalizado
from interface.componentes.botoes import BotaoVerde, BotaoTextoCinza
from interface.componentes.box import CaixaCentral
from interface.estilos import Cores as Cor
from interface.componentes.cabecalho import Cabecalho
from typing import Callable

class TelaLogin:
    """
    Tela de login para autenticação do usuário.

    Permite a entrada com nome e senha, e navega para o menu em caso de sucesso.
    """

    def __init__(
        self, 
        navegar_para_menu     : Callable[[], None], 
        navegar_para_cadastro : Callable[[], None]
    ):
        """
        Inicializa os componentes da tela de login.

        Args:
            navegar_para_menu (Callable): Função chamada após login bem-sucedido.
            navegar_para_cadastro (Callable): Função para navegar à tela de cadastro.
        """
        self.nome_input = InputTextoPersonalizado("Nome de usuário")
        self.senha_input = InputTextoPersonalizado("Senha", password = True)
        self.notificador = Notificador()
        self.navegar_para_menu = navegar_para_menu
        self.navegar_para_cadastro = navegar_para_cadastro

        # Botões da tela
        botao_entrar = BotaoVerde("Entrar", self.entrar)
        botao_cadastrar = BotaoTextoCinza("Cadastrar", lambda _: self.navegar_para_cadastro())

        # Layout da área de login
        conteudo = ft.Column(
            [
                ft.Text("Login", size = 24, weight = "bold", color = Cor.VERDE_ESCURO),
                ft.Container(height = 10),
                self.nome_input,
                ft.Container(height = 10),
                self.senha_input,
                ft.Container(height = 20),
                ft.Row([botao_entrar, botao_cadastrar], alignment = "center")
            ],
            spacing = 10,
            alignment = "center",
            horizontal_alignment = "center",
        )
        layout = CaixaCentral(conteudo)

        # Composição da view com cabeçalho, formulário e snackbar
        self.view = ft.Container(
            expand = True,
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
            alignment = ft.alignment.center,
        )

    async def entrar(self, e: ft.ControlEvent) -> None:
        """
        Realiza a tentativa de login com os dados informados.

        Exibe mensagem de erro se falhar ou navega para o menu em caso de sucesso.

        Args:
            e (ft.ControlEvent): Evento gerado pelo clique no botão "Entrar".
        """
        nome = self.nome_input.value.strip()
        senha = self.senha_input.value.strip()

        # Tenta autenticar o usuário
        usuario = AuthService.login(nome, senha)

        if usuario is None:
            self.notificador.erro(e.page, "Nome ou senha inválidos.")
        else:
            self.notificador.sucesso(
                e.page, f"Login de {usuario.nome} realizado com sucesso."
            )
            await asyncio.sleep(1)
            self.navegar_para_menu()
