import subprocess
import sys
import os
from pathlib import Path
from models.usuario import Usuario
from utils.logger import logger

class GameRunner:
    """
    Responsável por iniciar o jogo para um usuário específico.
    """

    def __init__(self, usuario: Usuario):
        """
        Inicializa o runner com um usuário.

        Args:
            usuario (Usuario): Instância do usuário autenticado.
        """
        self.usuario = usuario
        self.caminho_python = sys.executable
        self.caminho_engine = os.path.join("game", "engine.py")

    def iniciar_jogo(self):
        """
        Inicia o jogo para o usuário atual.

        Executa o script engine.py como subprocesso, passando o nome do usuário como argumento.
        """
        logger.info(f"Iniciando jogo para o usuario: {self.usuario.nome}")
        try:
            root = Path(__file__).resolve().parent.parent
            subprocess.run(
                [
                    sys.executable,
                    "-m", "game.engine",
                    self.usuario.nome
                ],
                cwd = str(root),
            )
        except Exception as e:
            logger.error(f"Erro ao iniciar o jogo: {e}")
    