import flet as ft
from interface.estilos import Cores as Cor

def Cabecalho() -> ft.Row:
    """
    Cria o cabeçalho da interface com o ícone e o título do jogo.

    Returns:
        ft.Row: Linha contendo a imagem do jogo e o nome do jogo, centralizados e estilizados.
    """
    return ft.Row(
        controls = [
            ft.Image(
                src    = "assets/snake.png",
                width  = 40,
                height = 40,
                fit    = ft.ImageFit.CONTAIN,
            ),
            ft.Text(
                "Snack Game",
                size   = 28,
                weight = "bold",
                color  = Cor.VERDE_ESCURO,
            )
        ],
        alignment          = "center",
        vertical_alignment = "center",
    )
