from utils.logger import logger
from exceptions.validacao_exception import ValidacaoException
from services.base_abstrata import BaseService
from models.usuario import Usuario

class AuthService(BaseService):
    """
    Serviço responsável pela autenticação e gerenciamento de sessão do usuário.
    Apenas um usuário pode estar logado por vez.
    """
    _usuario_logado: Usuario = None

    @classmethod
    def login(cls, nome: str, senha: str) -> Usuario | None:
        """
        Autentica o usuário. Retorna o objeto Usuario se sucesso, None caso contrário.
        """
        try:
            logger.info(f"Tentando login para o usuario: {nome}...")

            lista_usuarios = cls()._carregar_usuarios()

            if nome not in lista_usuarios:
                logger.warning(f"Login falhou: usuario '{nome}' nao encontrado.")
                return None

            dados = lista_usuarios[nome]
            usuario = Usuario(nome, dados["senha"], dados.get("score", 0))

            if not usuario.verificar_senha(senha):
                logger.warning(f"Login falhou: senha incorreta para '{nome}'.")
                return None

            cls._usuario_logado = usuario
            logger.info(f"Login de '{nome}' realizado com sucesso.")
            return usuario

        except ValidacaoException as e:
            logger.warning(f"Erro de validacao no login de '{nome}': {e.mensagem}")
            return None

        except Exception as e:
            logger.error(f"Erro inesperado no login de '{nome}': {str(e)}")
            return None

    @classmethod
    def logout(cls):
        """Remove a sessão atual (se houver)."""
        if cls._usuario_logado:
            logger.info(f"Usuario '{cls._usuario_logado.nome}' fez logout.")
        else:
            logger.warning("Tentativa de logout sem usuario logado.")
        cls._usuario_logado = None

    @classmethod
    def esta_logado(cls) -> bool:
        """Retorna True se há usuário logado."""
        return cls._usuario_logado is not None

    @classmethod
    def get_usuario_logado(cls) -> Usuario | None:
        """Retorna o usuário logado ou None."""
        return cls._usuario_logado
