import flet as ft
from flet import AppBar, Text, View
from flet.core.colors import Colors
from models import User, db_session
import sqlalchemy
from sqlalchemy.exc import IntegrityError
from sqlalchemy import select, desc


def main(page: ft.Page):
    # Configurações
    page.title = "Usuario com banco"
    page.theme_mode = ft.ThemeMode.DARK  # ou ft.ThemeMode.DARK
    page.window.width = 375
    page.window.height = 667

    # Funções

    def exibir_banco_em_detalhes(e):
        lv_Descricao.controls.clear()
        users = db_session.execute(select(User)).scalars()

        for user in users:
            lv_Descricao.controls.append(
                ft.ListTile(
                    leading=ft.Icon(ft.Icons.PERSON),
                    title=ft.Text(user.nome),
                    subtitle=ft.Text(user.profissao),
                    trailing=ft.PopupMenuButton(
                        icon=ft.Icons.MORE_VERT,
                        items=[
                            ft.PopupMenuItem(text='detalhes', on_click=lambda _, u=user: exibir_detalhesuu(u)),

                        ]
                    )
                )
            )
        page.update()

    def exibir_detalhesuu(user):
        txt_nome.value = user.nome
        txt_salario.value = user.profissao
        txt_profissao.value = user.salario
        page.go('/terceira')

    lista = []

    def exibir_lista(e):
        lv_Descricao.controls.clear()
        for user in lista:
            lv_Descricao.controls.append(
                ft.Text(value=f'nome: {user.name};\nprofissão: {user.profissao}\n salario: {user.salario}')
            )

    def salvar_itens(e):
        if inputName.value == '' or inputProfissao.value == '' or inputSalario.value == '':
            page.overlay.append(msg_error)
            msg_error.open = True
            page.update()
        elif inputName.value in lista:
            page.overlay.append(msg_error)
            msg_error.open = True
            page.update()
        else:
            try:
                valorInteiro = float(inputSalario.value)
            except ValueError:
                page.overlay.append(msg_error_repetido)
                msg_error_repetido.open = True
                page.update()
                return

            user = User(nome=inputName.value, profissao=inputProfissao.value, salario=valorInteiro)
            user.save()
            inputName.value = ''
            inputProfissao.value = ''
            inputSalario.value = ''
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
                    inputSalario,
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
        if page.route == "/segunda" or page.route == "/terceira":
            exibir_banco_em_detalhes(e)
            page.views.append(
                View(
                    "/segunda",
                    [
                        AppBar(title=Text("Segunda tela"), bgcolor=Colors.SECONDARY_CONTAINER),
                        lv_Descricao,
                        ft.FloatingActionButton('+', on_click=lambda _: page.go('/'), )

                    ],
                )
            )

        if page.route == '/terceira':
            page.views.append(
                View(
                    '/terceira',
                    [
                        AppBar(title=Text('terceira tela'), bgcolor=Colors.SECONDARY_CONTAINER),
                        txt_nome,
                        txt_profissao,
                        txt_salario,
                    ]
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
        content=ft.Text(value='insira um valor numerico no salario'),
        bgcolor=Colors.RED,
        duration=2000,
    )
    lv_Descricao = ft.ListView(
        height=500,

    )
    txt_nome = ft.Text('')
    txt_profissao = ft.Text('')
    txt_salario = ft.Text('')
    inputName = ft.TextField(label='digite seu nome')
    inputProfissao = ft.TextField(label='digite seu profissão')
    inputSalario = ft.TextField(label='digite seu salario')
    # Eventos
    page.on_route_change = gerencia_rotas
    page.on_view_pop = voltar
    page.go(page.route)


ft.app(main)
