import flet as ft
from controllers.cadastro_controller import CadastroController

class TelaCadastro:
    def __init__(self, on_cadastro_sucesso, on_voltar):
        self.nome = ft.TextField(label="Nome de usuário")
        self.senha = ft.TextField(label="Senha", password=True)
        self.msg = ft.Text("", color="red")

        self.view = ft.Column(
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                ft.Text("Cadastro", size=24),
                self.nome,
                self.senha,
                self.msg,
                ft.Row([
                    ft.ElevatedButton("Cadastrar", on_click=self.cadastrar),
                    ft.OutlinedButton("Voltar", on_click=lambda _: on_voltar())
                ])
            ]
        )

        self.on_cadastro_sucesso = on_cadastro_sucesso

    def cadastrar(self, e):
        nome = self.nome.value.strip()
        senha = self.senha.value.strip()

        if not nome or not senha:
            self.msg.value = "Preencha todos os campos."
            e.page.update()
            return

        res = CadastroController.cadastrar_usuario(nome, senha)

        if res["status"] == "sucesso":
            self.on_cadastro_sucesso()
        else:
            self.msg.value = res["mensagem"]
            e.page.update()