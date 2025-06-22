from services.base_abstrata import BaseService
from services.login import AuthService
from utils.logger import logger

class RankingService(BaseService):
    """
    Serviço responsável por extrair e ordenar os usuários com maiores scores.

    Herda de BaseService para reutilizar carregamento dos dados do JSON.
    """

    def top_3(self):
        """
        Retorna os três usuários com os maiores scores.

        Returns:
            list: Lista de tuplas (nome, score) com no mínimo 3 posições.
        """
        logger.debug("Iniciando extracao do top 3 do ranking.")
        usuarios = self._carregar_usuarios()
        logger.debug(f"{len(usuarios)} usuarios carregados do db.")

        lista = [(nome, dados.get("score", 0)) for nome, dados in usuarios.items()]
        top_ordenado = sorted(lista, key=lambda x: x[1], reverse=True)

        # Preenche com "Posição vaga" caso haja menos de 3 jogadores
        while len(top_ordenado) < 3:
            top_ordenado.append(("Posição vaga", 0))

        top_3 = top_ordenado[:3]
        logger.info(f"Top 3 gerado: {top_3}")
        return top_3
    
    def get_score_usuario_logado(self):
        """
        Retorna o score mais recente do usuário atualmente logado.
        """
        usuario = AuthService.get_usuario_logado()
        if not usuario:
            return 0

        usuarios = self._carregar_usuarios()
        dados = usuarios.get(usuario.nome, {})
        return dados.get("score", 0)
