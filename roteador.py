import flet as ft
from views.tela_login_ou_cadastro import TelaLoginOuCadastro
from views.tela_login import TelaLogin
from views.tela_cadastro import TelaCadastro
from views.tela_menu_usuario import TelaMenuUsuario
from views.tela_ranking import TelaRanking
from game.game_runner import iniciar_jogo
from controllers.auth_controller import AuthController

def navegar(page: ft.Page, route: str):
    page.views.clear()

    if route == "/":
        tela = TelaLoginOuCadastro(
            on_login=lambda: page.go("/login"),
            on_cadastro=lambda: page.go("/cadastro")
        )
        page.views.append(ft.View("/", controls=[tela.view]))

    elif route == "/login":
        tela = TelaLogin(
            on_login_sucesso=lambda user_id: page.go(f"/menu?user={user_id}"),
            on_voltar=lambda: page.go("/")
        )
        page.views.append(ft.View("/login", controls=[tela.view]))

    elif route == "/cadastro":
        tela = TelaCadastro(
            on_cadastro_sucesso=lambda: page.go("/login"),
            on_voltar=lambda: page.go("/")
        )
        page.views.append(ft.View("/cadastro", controls=[tela.view]))

    elif route.startswith("/menu"):
        from urllib.parse import urlparse, parse_qs
        query = parse_qs(urlparse(route).query)
        user_id = query.get("user", [""])[0]
        cliente = AuthController.sessao_ativa.get(user_id)
        if not cliente:
            page.go("/login")
            return
        tela = TelaMenuUsuario(
            cliente=cliente,
            on_jogar=lambda: iniciar_jogo(cliente["nome"]),
            on_ver_ranking=lambda: page.go("/ranking"),
            on_logout=lambda: page.go("/")
        )
        page.views.append(ft.View("/menu", controls=[tela.view]))

    elif route == "/ranking":
        tela = TelaRanking(
            on_voltar=lambda: page.go("/")
        )
        page.views.append(ft.View("/ranking", controls=[tela.view]))

    page.update()
