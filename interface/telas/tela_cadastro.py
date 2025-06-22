import flet as ft
import asyncio
from services.cadastro import CadastroService
from interface.componentes.notificador import Notificador
from interface.componentes.input import InputTextoPersonalizado
from interface.componentes.botoes import BotaoVerde, BotaoTextoCinza
from interface.componentes.box import CaixaCentral
from interface.estilos import Cores as Cor
from interface.componentes.cabecalho import Cabecalho

class TelaCadastro:
    """
    Tela de cadastro de usuário na aplicação.

    Permite o registro de um novo usuário e exibe mensagens de erro ou sucesso.
    """

    def __init__(self, navegar_para_login):
        """
        Inicializa os componentes da tela e recebe o callback para navegação após cadastro.

        Args:
            navegar_para_login (callable): Função chamada para ir à tela de login após cadastro.
        """
        self.nome_input = InputTextoPersonalizado("Nome de usuário")
        self.senha_input = InputTextoPersonalizado("Senha", password=True)
        self.notificador = Notificador()
        self.cadastro_service = CadastroService()
        self.navegar_para_login = navegar_para_login

        # Botões
        botao_cadastrar = BotaoVerde("Cadastrar", lambda e: e.page.run_task(self.cadastrar, e))
        botao_voltar = BotaoTextoCinza("Voltar", lambda _: self.navegar_para_login())

        # Layout da box de cadastro
        conteudo = ft.Column(
            [
                ft.Text("Cadastre seu usuário", size=24, weight="bold", color=Cor.VERDE_ESCURO),
                ft.Container(height=10),
                self.nome_input,
                ft.Container(height=10),
                self.senha_input,
                ft.Container(height=20),
                ft.Row([botao_cadastrar, botao_voltar], alignment="center")
            ],
            spacing=10,
            alignment="center",
            horizontal_alignment="center",
        )
        layout = CaixaCentral(conteudo)

        self.view = ft.Container(
            expand=True,
            content=ft.Column(
                [
                    Cabecalho(),
                    ft.Container(height=20),
                    layout,
                    ft.Container(height=20),
                    self.notificador.get_snackbar()
                ],
                alignment="center",
                horizontal_alignment="center",
                expand=True
            ),
            alignment=ft.alignment.center,
        )

    async def cadastrar(self, e):
        """
        Realiza o cadastro do usuário com os dados informados.

        Exibe notificação de sucesso ou erro, limpa os campos e
        agenda retorno à tela de login após 1.5 segundos.
        """
        nome = self.nome_input.value.strip()
        senha = self.senha_input.value.strip()
        resultado = self.cadastro_service.cadastrar_usuario(nome, senha)

        if resultado["status"] == "erro":
            self.notificador.erro(e.page, resultado["mensagem"])
        else:
            self.notificador.sucesso(e.page, resultado["mensagem"])
            self.nome_input.value = ""
            self.senha_input.value = ""
            e.page.update()

            await asyncio.sleep(1.5)
            self.navegar_para_login()
