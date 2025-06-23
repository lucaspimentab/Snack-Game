import flet as ft
from interface.estilos import Cores as Cor

def CaixaCentral(conteudo: ft.Control) -> ft.Container:
    """
    Cria um container centralizado com fundo colorido, bordas arredondadas e sombra.

    Args:
        conteudo (ft.Control): Componente Flet a ser exibido dentro da caixa.

    Returns:
        ft.Container: Container estilizado com preenchimento, sombra e bordas arredondadas.
    """
    return ft.Container(
        content       = conteudo,
        padding       = 30,
        bgcolor       = Cor.VERDE_CLARO,
        border_radius = 10,
        width         = 350,
        shadow        = ft.BoxShadow(
            blur_radius = 10,
            color       = Cor.CINZA_SOMBRA,
            offset      = ft.Offset(2, 2)
        )
    )
