from datetime import date

import flet as ft
from flet import AppBar, Text, View
from flet.core.colors import Colors

class Livro():
    def __init__(self, nome, descricao, autor):
        self.nome = nome
        self.descricao = descricao
        self.autor = autor

def main(page: ft.Page):
    # Configurações
    page.title = "Exemplo de Rotas"
    page.theme_mode = ft.ThemeMode.DARK  # ou ft.ThemeMode.DARK
    page.window.width = 375
    page.window.height = 667
    def lista_em_detalhes(e):
        lv_Descricao.controls.clear()
        for livro in lista:
            lv_Descricao.controls.append(
                ft.ListTile(
                    leading=ft.Icon(ft.Icons.PERSON),
                    title=ft.Text(livro.nome),
                    subtitle=ft.Text(livro.autor),
                    trailing=ft.PopupMenuButton(
                        icon=ft.Icons.MORE_VERT,
                        items=[
                            ft.PopupMenuItem(text='detalhes',on_click=lambda _: page.go('/terceira')),
                        ]
                    )
                )
            )
        page.update()


    lista = []
    # Funções
    def exibir_lista(e):
        print('teste')
        lv_Descricao.controls.clear()
        for livro in lista:
            lv_Descricao.controls.append(
                ft.Text(value=f'nome do livro {livro.nome} \ndescrição: {livro.descricao}\nautor: {livro.autor}')
            )
    def salvar_user(e):
        if input_nome.value == '' or input_descricao.value == '' or input_autor.value == '':
            page.overlay.append(msg_error)
            msg_error.open = True
            page.update()
        elif input_nome.value in lista:
            page.overlay.append(msg_error)
            msg_error.open = True
            page.update()
        else:
            livro = Livro(nome=input_nome.value, descricao=input_descricao.value, autor=input_autor.value)
            lista.append(livro)

            input_nome.value = ''
            input_descricao.value = ''
            input_autor.value = ''
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
                    input_nome,
                    input_descricao,
                    input_autor,
                    ft.Button(
                        text="Salvar",
                        on_click=lambda _: salvar_user(e),
                    ),
                    ft.Button(
                        text="Exibir",
                        on_click=lambda _: page.go('/segunda'),
                    )
                ],
            )
        )
        if page.route == "/segunda":
            # exibir_lista(e)
            lista_em_detalhes(e)
            page.views.append(
                View(
                    "/segunda",
                    [
                        AppBar(title=Text("Segunda tela"), bgcolor=Colors.SECONDARY_CONTAINER),
                        lv_Descricao,
                        ft.FloatingActionButton('+', on_click=lambda _:page.go('/'),)
                    ],
                )
            )
        page.update()
        if page.route == "/terceira":
            exibir_lista(e)
            page.views.append(
                View(
                    "/terceira",
                    [
                        AppBar(title=Text("Segunda tela"), bgcolor=Colors.SECONDARY_CONTAINER),
                        lv_Descricao,

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
        content=ft.Text(value='nome repetido'),
        bgcolor=Colors.RED,
        duration=2000,
    )
    lv_Descricao = ft.ListView(
        height=500,

    )
    input_nome = ft.TextField(label="Digite o nome do livro")
    input_descricao = ft.TextField(label='insira a descricao do livro')
    input_autor = ft.TextField(label='insira o autor do livro')
    # Eventos
    page.on_route_change = gerencia_rotas
    page.on_view_pop = voltar

    page.go(page.route)

# Comando que executa o aplicativo
# Deve estar sempre colado na linha
ft.app(main)