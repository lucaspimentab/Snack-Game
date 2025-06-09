import json
import os

class AuthController:
    """
    Controlador de autenticação simplificado para o jogo Snake.
    Gerencia login, logout e sessão ativa em memória.
    """

    _db_path = "database/usuarios.json"
    sessao_ativa = {}

    @staticmethod
    def login(nome: str, senha: str) -> dict:
        usuarios = AuthController._carregar_usuarios()
        if nome not in usuarios:
            return {"status": "erro", "mensagem": "Usuário não encontrado."}
        if usuarios[nome] != senha:
            return {"status": "erro", "mensagem": "Senha incorreta."}
        AuthController.sessao_ativa[nome] = {"nome": nome}
        return {"status": "sucesso", "mensagem": "Login realizado.", "usuario_id": nome}

    @staticmethod
    def logout(nome: str):
        AuthController.sessao_ativa.pop(nome, None)

    @staticmethod
    def _carregar_usuarios():
        if not os.path.exists(AuthController._db_path):
            return {}
        with open(AuthController._db_path, "r", encoding="utf-8") as f:
            return json.load(f)
