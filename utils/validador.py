import re
from utils.logger import logger
from exceptions.validacao_exception import ValidacaoException

class ValidarUsuario:
    """
    Classe utilitária para validação de dados de um usuário.

    Utiliza métodos estáticos para validar nome, senha e score.
    """

    @staticmethod
    def tudo(nome: str, senha: str, score: int = 0) -> None:
        """
        Realiza a validação completa de nome, senha e score de um usuário.

        Args:
            nome (str): Nome do usuário.
            senha (str): Senha do usuário.
            score (int, optional): Score do usuário. Default é 0.

        Raises:
            ValidacaoException: Se qualquer dado estiver inválido.
        """
        logger.debug("Validando dados do usuario...")
        ValidarUsuario._nome(nome)
        ValidarUsuario._senha(senha)
        ValidarUsuario._score(score)
        logger.info(f"Validacao concluida para usuario: {nome}")

    @staticmethod
    def _nome(nome: str) -> None:
        """
        Valida o nome do usuário.

        Args:
            nome (str): Nome a ser validado.

        Raises:
            ValidacaoException: Se o nome for nulo, vazio, muito curto,
            muito longo ou contiver caracteres inválidos.
        """
        nome_limpo = nome.strip()

        if not nome or len(nome_limpo) < 3:
            logger.warning(f"Nome invalido: '{nome}' (muito curto ou vazio)")
            raise ValidacaoException(
                "O nome de usuário deve ter pelo menos 3 caracteres."
            )

        if len(nome_limpo) > 15:
            logger.warning(f"Nome invalido: '{nome}' (muito longo)")
            raise ValidacaoException(
                "O nome de usuário deve ter no máximo 15 caracteres."
            )

        if not re.fullmatch(r"[a-zA-Z0-9]+", nome_limpo):
            logger.warning(f"Nome invalido: '{nome}' (caracteres invalidos)")
            raise ValidacaoException(
                "O nome de usuário deve conter apenas letras e números (sem espaços ou símbolos)."
            )

    @staticmethod
    def _senha(senha: str) -> None:
        """
        Valida a senha do usuário.

        Args:
            senha (str): Senha a ser validada.

        Raises:
            ValidacaoException: Se a senha for nula, vazia, muito curta ou muito longa.
        """
        if not senha or len(senha) < 4:
            logger.warning("Senha invalida (muito curta ou vazia)")
            raise ValidacaoException("A senha deve ter pelo menos 4 caracteres.")

        if len(senha) > 20:
            logger.warning("Senha invalida (muito longa)")
            raise ValidacaoException("A senha deve ter no máximo 20 caracteres.")

    @staticmethod
    def _score(score: int) -> None:
        """
        Valida o score do usuário.

        Args:
            score (int): Score a ser validado.

        Raises:
            ValidacaoException: Se o score for negativo.
        """
        # Score não pode ser negativo em nenhuma situação
        if score < 0:
            logger.warning(f"Score invalido: {score} (negativo)")
            raise ValidacaoException("Score não pode ser negativo.")
