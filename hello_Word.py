import flet as ft

def main(page: ft.Page):
    page.title = "Mi primera vez en flet"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    txt_number = ft.TextField(value="0", text_align=ft.TextAlign.CENTER, width=100)

    def minus(e):
        txt_number.value = str(int(txt_number.value)-1)
        page.update()

    def plus(e):
        txt_number.value = str(int(txt_number.value)+1)
        page.update()

    def refreshs(e):
        txt_number.value = "0"
        page.update()

    page.add(
        ft.Row([
            ft.IconButton(ft.icons.REMOVE, on_click=minus),
            txt_number,
            ft.IconButton(ft.icons.ADD, on_click=plus),
            ft.ElevatedButton("REFRESH",icon="REFRESH", on_click=refreshs)
            ],
        alignment=ft.MainAxisAlignment.CENTER
        ),
    )

ft.app(main)

# Estructura para lanzar desde un navegador web
# ft.app(target=main, view=ft.WEB_BROWSER)

