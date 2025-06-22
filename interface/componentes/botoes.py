import flet as ft
from interface.estilos import Cores as Cor

def BotaoVerde(texto, on_click):
    """
    Cria um botão elevado com fundo verde escuro e texto branco.

    Args:
        texto (str): Texto exibido no botão.
        on_click (function): Função chamada quando o botão for clicado.

    Returns:
        ft.ElevatedButton: Um botão estilizado com bordas arredondadas.
    """
    return ft.ElevatedButton(
        texto,
        on_click = on_click,
        style    = ft.ButtonStyle(
            bgcolor = Cor.VERDE_ESCURO,
            color   = Cor.BRANCO,
            shape   = ft.RoundedRectangleBorder(radius = 12),
        )
    )

def BotaoTextoCinza(texto, on_click):
    """
    Cria um botão de texto simples com cor de fonte cinza.

    Args:
        texto (str): Texto exibido no botão.
        on_click (function): Função chamada quando o botão for clicado.

    Returns:
        ft.TextButton: Um botão de texto estilizado com cor cinza.
    """
    return ft.TextButton(
        texto,
        on_click = on_click,
        style    = ft.ButtonStyle(color = Cor.CINZA_TEXTO)
    )
