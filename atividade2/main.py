from datetime import date

from atividade2.models import db_session
from models import Livro
import flet as ft
from flet import AppBar, Text, View
from flet.core.colors import Colors
import sqlalchemy
from sqlalchemy.exc import IntegrityError
from sqlalchemy import select, desc

def main(page: ft.Page):
    # Configurações
    page.title = "Exemplo de Rotas"
    page.theme_mode = ft.ThemeMode.DARK
    page.window.width = 375
    page.window.height = 667
    # def lista_em_detalhes(e):
    #     lv_Descricao.controls.clear()
    #     for livro in lista:
    #         lv_Descricao.controls.append(
    #             ft.ListTile(
    #                 leading=ft.Icon(ft.Icons.PERSON),
    #                 title=ft.Text(livro.nome),
    #                 subtitle=ft.Text(livro.autor),
    #                 trailing=ft.PopupMenuButton(
    #                     icon=ft.Icons.MORE_VERT,
    #                     items=[
    #                         ft.PopupMenuItem(text='detalhes',on_click=lambda _: page.go('/terceira')),
    #                     ]
    #                 )
    #             )
    #         )
    #     page.update()
    def exibir_banco_em_detalhes(e):
        lv_Descricao.controls.clear()
        livros = db_session.execute(select(Livro)).scalars()
        for livro in livros:
            lv_Descricao.controls.append(
                ft.ListTile(
                    leading=ft.Icon(ft.Icons.BOOK),
                    title=ft.Text(livro.nome),
                    subtitle=ft.Text(livro.autor),
                    trailing=ft.PopupMenuButton(
                                            icon=ft.Icons.MORE_VERT,
                                            items=[
                                                ft.PopupMenuItem(text='detalhes',on_click=lambda _, l=livro: exibir_detalhesuu(l)),

                                            ]
                                        )
                                    )
                                )
        page.update()


    lista = []
    # Funções
    def exibir_banco(e):
        livros = db_session.execute(select(Livro)).scalars()
        lv_Descricao.controls.clear()
        for livro in livros:
            lv_Descricao.controls.append(
                ft.Text(value=f'Nome do livro: {livro.nome}\nDescricao do livro: {livro.descricao}\nAutor do livro: {livro.autor}\n categoria: {livro.categoria}\n INSBN: {livro.ISBN}')
            )
    txt_titulo = ft.Text('')
    txt_autor = ft.Text('')
    txt_descricao = ft.Text('')
    txt_categoria = ft.Text('')
    txt_ISBN = ft.Text('')

    def exibir_detalhesuu(livro):


        txt_titulo.value = 'titulo: ' + livro.nome
        txt_autor.value = 'autor: ' + livro.autor
        txt_descricao.value = 'descricao ' + livro.descricao
        txt_categoria.value = 'categoria: ' + livro.categoria
        txt_ISBN.value = 'ISBN: ' + livro.ISBN
        page.go('/detalhes')

    # def exibir_lista(e):
    #     print('teste')
    #     lv_Descricao.controls.clear()
    #     for livro in lista:
    #         lv_Descricao.controls.append(
    #             ft.Text(value=f'nome do livro {livro.nome} \ndescrição: {livro.descricao}\nautor: {livro.autor}')
    #         )
    # def detalhes(e,id_do_livro):


    def salvar_livro(e):
        if input_nome.value == '' or input_descricao.value == '' or input_autor.value == '':
            page.overlay.append(msg_error)
            msg_error.open = True
            page.update()
        elif input_ISBN.value in lista:
            page.overlay.append(msg_error)
            msg_error.open = True
            page.update()
        else:
            livro = Livro(nome=input_nome.value, descricao=input_descricao.value, autor=input_autor.value, categoria=input_categoria.value, ISBN=input_ISBN.value)
            livro.save()
            input_nome.value = ''
            input_descricao.value = ''
            input_autor.value = ''
            input_categoria.value = ''
            input_ISBN.value = ''
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
                    input_categoria,
                    input_ISBN,
                    ft.Button(
                        text="Salvar",
                        on_click=lambda _: salvar_livro(e),
                    ),
                    ft.Button(
                        text="Exibir",
                        on_click=lambda _: page.go('/livros'),
                    )
                ],
            )
        )
        if page.route == "/livros" or page.route == "/detalhes":
            exibir_banco_em_detalhes(e)

            page.views.append(
                View(
                    "/Livros",
                    [
                        AppBar(title=Text("Segunda tela"), bgcolor=Colors.SECONDARY_CONTAINER),
                        lv_Descricao,


                        # ft.FloatingActionButton('+', on_click=detalhes(e))
                    ],
                )
            )
        page.update()
        if page.route == "/detalhes":
            page.views.append(
                View(
                    "/detalhes",
                    [
                        AppBar(title=Text('Detalhes do livro'), bgcolor=Colors.SECONDARY_CONTAINER),
                        txt_titulo,
                        txt_autor,
                        txt_descricao,
                        txt_categoria,
                        txt_ISBN,

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
    input_categoria = ft.TextField(label='insira a categoria do livro')
    input_ISBN = ft.TextField(label='insira o ISBN do livro')
    # Eventos
    page.on_route_change = gerencia_rotas
    page.on_view_pop = voltar

    page.go(page.route)

# Comando que executa o aplicativo
# Deve estar sempre colado na linha
ft.app(main)