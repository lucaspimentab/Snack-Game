import flet as ft

class TelaLoginOuCadastro:
    def __init__(self, on_login, on_cadastro):
        self.view = ft.Column(
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=20,
            controls=[
                ft.Text("Bem-vindo ao Snake!", size=32, weight=ft.FontWeight.BOLD),
                ft.Text("Escolha uma opção abaixo para continuar:", size=16),
                ft.ElevatedButton("Entrar", width=200, on_click=lambda _: on_login()),
                ft.OutlinedButton("Cadastrar", width=200, on_click=lambda _: on_cadastro())
            ]
        )
