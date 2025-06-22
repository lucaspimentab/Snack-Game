import flet as ft
from interface.estilos import Cores as Cor

class Notificador:
    """
    Componente de notificação visual do sistema.

    Utiliza SnackBar do Flet para exibir mensagens de erro, sucesso ou informação.
    """

    def __init__(self):
        """
        Inicializa o componente com um SnackBar reutilizável.
        """
        self._snackbar = ft.SnackBar(
            content = ft.Text(""),
            duration = 3500,
            show_close_icon = True,
        )

    def erro(self, page, mensagem: str) -> None:
        """
        Exibe uma notificação de erro com destaque em vermelho.

        Args:
            page (ft.Page): Página onde o snackbar será exibido.
            mensagem (str): Texto da mensagem.
        """
        self._mostrar(page, mensagem, Cor.VERMELHO)

    def info(self, page, mensagem: str) -> None:
        """
        Exibe uma notificação de informação com destaque em cor cinza.

        Args:
            page (ft.Page): Página onde o snackbar será exibido.
            mensagem (str): Texto da mensagem.
        """
        self._mostrar(page, mensagem, Cor.CINZA_TEXTO)

    def sucesso(self, page, mensagem: str) -> None:
        """
        Exibe uma notificação de sucesso com destaque em verde.

        Args:
            page (ft.Page): Página onde o snackbar será exibido.
            mensagem (str): Texto da mensagem.
        """
        self._mostrar(page, mensagem, Cor.VERDE_MEDIO)

    def _mostrar(self, page, mensagem: str, cor: str) -> None:
        """
        Exibe o SnackBar com a mensagem e a cor especificada.

        Args:
            page (ft.Page): Página onde o snackbar será exibido.
            mensagem (str): Texto da mensagem.
            cor (str): Cor de fundo da notificação.
        """
        self._snackbar.content.value = mensagem
        self._snackbar.bgcolor = cor
        page.snack_bar = self._snackbar
        self._snackbar.open = True
        page.update()

    def get_snackbar(self):
            """
            Retorna o objeto SnackBar para uso manual (em layouts, por exemplo).

            Returns:
                ft.SnackBar: Instância de snackbar encapsulada.
            """
            return self._snackbar
