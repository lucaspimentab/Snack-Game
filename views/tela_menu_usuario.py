import flet as ft

class TelaMenuUsuario:
    def __init__(self, cliente, on_jogar, on_ver_ranking, on_logout):
        self.view = ft.Column(
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=20,
            controls=[
                ft.Text(f"Olá, {cliente['nome']}!", size=24),
                ft.ElevatedButton("Jogar", on_click=lambda _: on_jogar()),
                ft.ElevatedButton("Ver Ranking", on_click=lambda _: on_ver_ranking()),
                ft.ElevatedButton("Logout", on_click=lambda _: on_logout())
            ]
        )
