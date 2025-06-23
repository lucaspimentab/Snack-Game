import flet as ft
from interface.estilos import Cores as Cor

def InputTextoPersonalizado(label: str, password = False):
    """
    Cria um campo de texto personalizado com estilos definidos.

    Args:
        label (str): O rótulo exibido acima do campo de texto.
        password (bool, optional): Se True, o campo será do tipo senha. 
            Permite exibir/ocultar o texto. Padrão é False.

    Returns:
        ft.TextField: Um componente TextField estilizado com as cores do tema.
    """
    return ft.TextField(
        label                = label,
        password             = password,
        can_reveal_password  = password,
        width                = 300,
        border_color         = Cor.BORDAS_INPUT,
        focused_border_color = Cor.VERDE_MEDIO,
        hint_style           = ft.TextStyle(Cor.VERDE_PLACEHOLDER)
    )
