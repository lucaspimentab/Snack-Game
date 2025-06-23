import flet as ft
from roteador import Roteador

def main(page: ft.Page):
    page.title = "Snake Game - Interface"
    page.theme_mode = ft.ThemeMode.LIGHT
    roteador = Roteador(page)
    page.on_route_change = lambda e: roteador.navegar(page.route)
    page.go("/")

if __name__ == "__main__":
    ft.app(target = main)
