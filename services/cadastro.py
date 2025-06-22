from utils.logger import logger
from exceptions.validacao_exception import ValidacaoException
from models.usuario import Usuario
from services.base_abstrata import BaseService

class CadastroService(BaseService):
    """
    Serviço responsável pelo cadastro e armazenamento de usuários em arquivo JSON.

    Herda métodos e atributos de BaseService.
    """
    
    def cadastrar_usuario(self, nome: str, senha: str) -> dict:
        """
        Cadastra um novo usuário, caso o nome não exista previamente.

        Args:
            nome (str): Nome do usuário a ser cadastrado.
            senha (str): Senha do usuário.

        Returns:
            dict: Dicionário com o status do cadastro e uma mensagem correspondente.

        Raises:
            ValidacaoException: Caso os dados do usuário sejam inválidos.
        """
        try:
            logger.info(f"Tentando cadastrar usuario: {nome}")
            usuarios = self._carregar_usuarios()

            # Caso o usuário já esteja cadastrado
            if nome in usuarios:
                logger.warning(f"Cadastro falhou - usuario ja existente: {nome}")
                return {
                    "status": "erro",
                    "mensagem": "Usuário já cadastrado."
                }

            # Cria instância do usuário
            usuario = Usuario(nome, senha)

            # Cadastra e salva o usuário no db
            usuarios[nome] = {"senha": usuario._senha, "score": usuario.score}
            self._salvar_usuarios(usuarios)

            logger.info(f"Usuario cadastrado com sucesso: {nome}")
            return {
                "status": "sucesso",
                "mensagem": "Usuário cadastrado com sucesso."
            }

        except ValidacaoException as e:
            logger.warning(f"Erro de validacao ao cadastrar '{nome}': {e.mensagem}")
            return {
                "status": "erro",
                "mensagem": e.mensagem
            }

        except Exception as e:
            logger.error(f"Erro inesperado no cadastro de '{nome}': {str(e)}")
            return {
                "status": "erro",
                "mensagem": f"Erro inesperado: {str(e)}"
            }
