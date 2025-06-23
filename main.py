import flet as ft
from roteador import Roteador

def main(page: ft.Page) -> None:
    """
    Função principal da aplicação Flet.

    Define configurações iniciais da página, configura o roteador e inicia na rota principal.
    """
    page.title = "Snack Game - Interface"
    page.theme_mode = ft.ThemeMode.LIGHT

    roteador = Roteador(page)
    page.on_route_change = lambda e: roteador.navegar(page.route)
    page.go("/")

if __name__ == "__main__":
    # Inicia o app usando Flet com a função main como ponto de entrada
    ft.app(target = main)
