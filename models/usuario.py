from utils.validador import ValidarUsuario as Validar
from utils.logger import logger

class Usuario:
    """
    Representa um usuário do jogo, contendo nome, senha e score.

    Attributes:
        _nome (str): Nome do usuário.
        _senha (str): Senha protegida do usuário.
        _score (int): Pontuação máxima do usuário.
    """

    def __init__(self, nome: str, senha: str, score: int = 0):
        """
        Inicializa um novo usuário.

        Args:
            nome (str): Nome do usuário.
            senha (str): Senha do usuário.
            score (int, optional): Pontuação inicial. Default é 0.
        """
        Validar.tudo(nome, senha, score)
        self._nome = nome
        self._senha = senha
        self._score = score
        logger.info(f"Usuario criado: {self._nome} com score inicial {self._score}")

    @property
    def nome(self):
        """
        Retorna o nome do usuário.

        Returns:
            str: Nome do usuário.
        """
        return self._nome

    def verificar_senha(self, senha_digitada: str) -> bool:
        """
        Verifica se a senha digitada corresponde à senha do usuário.

        Args:
            senha_digitada (str): Senha fornecida para verificação.

        Returns:
            bool: True se a senha estiver correta, False caso contrário.
        """
        estado = self._senha == senha_digitada
        logger.info(f"Verificacao de senha do usuario {self._nome}: {'sucesso' if estado else 'falha'}")
        return estado

    @property
    def score(self):
        """
        Retorna a pontuação atual do usuário.

        Returns:
            int: Score do usuário.
        """
        return self._score

    @score.setter
    def score(self, novo_score: int):
        """
        Atualiza o score do usuário, se o novo score for maior que o atual.

        Args:
            novo_score (int): Novo score a ser considerado.
        """
        if novo_score > self._score:
            logger.info(f"Score atualizado para o usuario {self._nome}: {self._score} -> {novo_score}")
            self._score = novo_score

    def to_dict(self) -> dict:
        """
        Converte os dados do usuário para um dicionário.

        Returns:
            dict: Dicionário contendo a senha e o score do usuário.
        """
        return {
            "senha": self._senha,
            "score": self._score
        }

    @classmethod
    def from_dict(cls, nome: str, dados: dict):
        """
        Cria uma instância de Usuario a partir de um dicionário.

        Args:
            nome (str): Nome do usuário.
            dados (dict): Dicionário contendo 'senha' e opcionalmente 'score'.

        Returns:
            Usuario: Instância da classe Usuario.
        """
        return cls(nome, dados["senha"], dados.get("score", 0))
