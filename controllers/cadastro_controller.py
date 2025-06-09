import json
import os

class CadastroController:
    """
    Controlador de cadastro de usuários para o jogo Snake.
    Armazena os dados em JSON local.
    """

    _db_path = "database/usuarios.json"

    @staticmethod
    def cadastrar_usuario(nome: str, senha: str) -> dict:
        usuarios = CadastroController._carregar_usuarios()
        if nome in usuarios:
            return {"status": "erro", "mensagem": "Nome de usuário já cadastrado."}

        usuarios[nome] = senha
        CadastroController._salvar_usuarios(usuarios)
        return {"status": "sucesso", "mensagem": "Usuário cadastrado com sucesso."}

    @staticmethod
    def _carregar_usuarios():
        if not os.path.exists(CadastroController._db_path):
            return {}
        with open(CadastroController._db_path, "r", encoding="utf-8") as f:
            return json.load(f)

    @staticmethod
    def _salvar_usuarios(usuarios):
        os.makedirs(os.path.dirname(CadastroController._db_path), exist_ok=True)
        with open(CadastroController._db_path, "w", encoding="utf-8") as f:
            json.dump(usuarios, f, indent=2)
