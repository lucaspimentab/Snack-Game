from pathlib import Path

# Caminho absoluto até a raiz
BASE_DIR = Path(__file__).resolve().parent.parent

ASSETS_DIR = BASE_DIR / "assets"
DB_PATH           = BASE_DIR / "database" / "usuarios.json"
SOUNDTRACK_PATH   = ASSETS_DIR / "soundtrack.mp3"
BEEP_SOUND_PATH   = ASSETS_DIR / "beep.mp3"
SPEED_SOUND_PATH  = ASSETS_DIR / "speed.mp3"
IMPACT_SOUND_PATH = ASSETS_DIR / "impact.mp3"

