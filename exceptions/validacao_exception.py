class ValidacaoException(Exception):
    """
    Exceção personalizada para erros de validação.

    Attributes:
        mensagem (str): Mensagem descritiva do erro de validação.
    """
    def __init__(self, mensagem: str):
        """
        Inicializa a exceção com uma mensagem de erro.

        Args:
            mensagem (str): Mensagem explicando o motivo da exceção.
        """
        super().__init__(mensagem)
        self.mensagem = mensagem
    