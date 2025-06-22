from utils.logger import logger
import json
from pathlib import Path
from utils.config import DB_PATH

class BaseService:
    """
    Classe base para serviços que manipulam dados de usuários armazenados em um arquivo JSON.

    Responsável por garantir que o arquivo exista e por fornecer métodos utilitários para
    carregar e salvar os dados.
    
    Attributes:
        db_path (Path): Caminho para o arquivo JSON onde os dados dos usuários são armazenados.
    """

    def __init__(self, db_path=DB_PATH):
        """
        Inicializa o serviço base com o caminho do banco de dados.

        Cria o diretório pai e o arquivo JSON vazio se ainda não existirem.

        Args:
            db_path (str or Path, optional): Caminho para o arquivo JSON.
                Default é o valor definido em DB_PATH.
        """
        self.db_path = Path(db_path)
        self.db_path.parent.mkdir(parents=True, exist_ok=True)
        if not self.db_path.exists():
            with open(self.db_path, "w", encoding="utf-8") as f:
                json.dump({}, f)
                logger.info(f"Arquivo de banco de dados criado em: {self.db_path}")
        else:
            logger.debug(f"Arquivo de banco de dados ja existente em: {self.db_path}")

    def _carregar_usuarios(self) -> dict:
        """
        Carrega os dados de usuários do arquivo JSON.

        Returns:
            dict: Dicionário com os dados dos usuários.
        """
        logger.debug("Carregando usuarios do db...")
        with open(self.db_path, "r", encoding="utf-8") as f:
            dados = json.load(f)
        logger.debug(f"{len(dados)} usuarios carregados.")
        return dados

    def _salvar_usuarios(self, usuarios: dict):
        """
        Salva os dados dos usuários no arquivo JSON.

        Args:
            usuarios (dict): Dicionário com os dados dos usuários a serem salvos.
        """
        with open(self.db_path, "w", encoding="utf-8") as f:
            json.dump(usuarios, f, indent=2)
        logger.info(f"{len(usuarios)} usuarios salvos no db.")
