from pathlib import Path

# Caminho absoluto da raiz do projeto, a partir de onde o script foi iniciado
BASE_DIR = Path(__file__).resolve()

# Sobe diretórios até encontrar a raiz do projeto
while BASE_DIR.name != "Snack-Game" and BASE_DIR != BASE_DIR.parent:
    BASE_DIR = BASE_DIR.parent

# Agora usa a raiz real
DB_PATH = BASE_DIR / "database" / "usuarios.json"
