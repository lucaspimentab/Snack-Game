import subprocess
import sys
import os

def iniciar_jogo(nome_jogador: str):
    caminho_python = sys.executable
    caminho_engine = os.path.join("game", "engine.py")
    
    subprocess.run([caminho_python, caminho_engine, nome_jogador])
