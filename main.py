import flet as ft
from roteador import Roteador

def main(page: ft.Page):
    
    # Configurações da janela
    page.title = "Snake Game - Interface"
    page.window_width = 500
    page.window_height = 500
    page.theme_mode = ft.ThemeMode.LIGHT

    # Inicializa o roteador e define a função de navegação
    roteador = Roteador(page)
    page.on_route_change = lambda e: roteador.navegar(page.route)

    # Navega para a rota inicial
    page.go("/")

# Inicializa o app com a função main
if __name__ == "__main__":
    ft.app(target=main)
