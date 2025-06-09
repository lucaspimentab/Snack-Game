import flet as ft
from controllers.auth_controller import AuthController

class TelaLogin:
    def __init__(self, on_login_sucesso, on_voltar):
        self.input_nome = ft.TextField(label="Nome de usuário", autofocus=True)
        self.input_senha = ft.TextField(label="Senha", password=True)
        self.msg = ft.Text("", color="red")

        self.view = ft.Column(
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=20,
            controls=[
                ft.Text("Login", size=24),
                self.input_nome,
                self.input_senha,
                self.msg,
                ft.Row([
                    ft.ElevatedButton("Entrar", on_click=self.login),
                    ft.OutlinedButton("Voltar", on_click=lambda _: on_voltar())
                ])
            ]
        )

        self.on_login_sucesso = on_login_sucesso

    def login(self, e):
        nome = self.input_nome.value.strip()
        senha = self.input_senha.value.strip()

        if not nome or not senha:
            self.msg.value = "Preencha todos os campos."
            e.page.update()
            return

        res = AuthController.login(nome, senha)
        if res["status"] == "sucesso":
            self.on_login_sucesso(res["usuario_id"])
        else:
            self.msg.value = res["mensagem"]
            e.page.update()