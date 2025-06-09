import flet as ft
import json
import os

class TelaRanking:
    def __init__(self, on_voltar):
        self.on_voltar = on_voltar
        self.ranking_data = self.carregar_ranking()
        self.view = ft.Column(
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=10,
            controls=[
                ft.Text("Ranking de Jogadores", size=24, weight=ft.FontWeight.BOLD)
            ] + [
                ft.Text(f"{i+1}. {nome} - {pontos} pts") for i, (nome, pontos) in enumerate(self.ranking_data)
            ] + [
                ft.ElevatedButton("Voltar", on_click=lambda _: on_voltar())
            ]
        )

    def carregar_ranking(self):
        path = "database/ranking.json"
        if not os.path.exists(path):
            return []
        with open(path, "r", encoding="utf-8") as f:
            dados = json.load(f)
        ordenado = sorted(dados.items(), key=lambda x: x[1], reverse=True)
        return ordenado[:5]