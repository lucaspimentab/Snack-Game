import flet as ft
from roteador import navegar

def main(page: ft.Page):
    page.title = "Snake com Login"
    page.window_width = 700
    page.window_height = 600
    page.theme_mode = ft.ThemeMode.DARK
    page.on_route_change = lambda e: navegar(page, page.route)
    page.go("/")

if __name__ == "__main__":
    ft.app(target=main)
