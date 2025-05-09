import flet as ft
from flet import AppBar, Text, View
from flet.core.colors import Colors

class User():
    def __init__(self, name, profissao):
        self.name = name
        self.profissao = profissao

def main(page: ft.Page):
    # Configurações
    page.title = "Exemplo de Rotas"
    page.theme_mode = ft.ThemeMode.DARK  # ou ft.ThemeMode.DARK
    page.window.width = 375
    page.window.height = 667

    # Funções

    lista = []
    def exibir_lista(e):
        lv_Descricao.controls.clear()
        for user in lista:
            lv_Descricao.controls.append(
                ft.Text(value=f'nome: {user.name};\nprofissão: {user.profissao}')
            )
    def salvar_itens(e):
        if inputName.value == '' or inputProfissao.value == '':
            page.overlay.append(msg_error)
            msg_error.open = True
            page.update()
        elif inputName.value in lista or inputProfissao.value in lista:
            page.overlay.append(msg_error)
            msg_error.open = True
            page.update()
        else:
            user = User(name=inputName.value, profissao=inputProfissao.value)
            lista.append(user)
            inputName.value = ''
            inputProfissao.value = ''
            page.overlay.append(msg_sucesso)
            msg_sucesso.open = True
            page.update()

    def gerencia_rotas(e):
        page.views.clear()
        page.views.append(
            View(
                "/",
                [
                    AppBar(title=Text("Home"), bgcolor=Colors.PRIMARY_CONTAINER),
                    inputName,
                    inputProfissao,
                    ft.Button(
                        text='salvar',
                        on_click=lambda _: salvar_itens(e)
                    ),
                    ft.Button(
                        text='Exibir',
                        on_click=lambda _: page.go('/segunda'),
                    )
                ],
            )
        )
        if page.route == "/segunda":
            exibir_lista(e)
            page.views.append(
                View(
                    "/segunda",
                    [
                        AppBar(title=Text("Segunda tela"), bgcolor=Colors.SECONDARY_CONTAINER),
                        lv_Descricao,
                        ft.FloatingActionButton('+', on_click=lambda _: page.go('/'),)

                    ],
                )
            )
        page.update()

    def voltar(e):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)


    # Componentes

    msg_sucesso = ft.SnackBar(
        content=ft.Text(value='nome salvado com sucesso'),
        bgcolor=Colors.GREEN,
        duration=1000,
    )

    msg_error = ft.SnackBar(
        content=ft.Text(value='nome está vazio'),
        bgcolor=Colors.RED,
        duration=2000,
    )
    msg_error_repetido = ft.SnackBar(
        content=ft.Text(value='nome repetido'),
        bgcolor=Colors.RED,
        duration=2000,
    )
    lv_Descricao = ft.ListView(
        height=500,

    )
    inputName = ft.TextField(label='digite seu nome')
    inputProfissao = ft.TextField(label='digite seu profissão')

    # Eventos
    page.on_route_change = gerencia_rotas
    page.on_view_pop = voltar

    page.go(page.route)

# Comando que executa o aplicativo
# Deve estar sempre colado na linha
ft.app(main)