import flet as ft
from datetime import datetime


def main(page: ft.Page):
    page.title = "Мое первое приложение"
    greeting_text = ft.Text("Привет, мир!")

    page.theme_mode = ft.ThemeMode.LIGHT

    greeting_history = []

    name_input = ft.TextField(label='Введите ваше имя:')

    def update_history_view():
        history_controls = [ft.Text("История приветствий:", size="bodyMedium")]
        for idx, record in enumerate(greeting_history):
            history_controls.append(
                ft.Row([
                    ft.Text(record),
                    ft.IconButton(icon=ft.Icons.CLOSE, on_click=lambda e, i=idx: remove_name_from_history(i))
                ])
            )
        history_column.controls = history_controls
        page.update()

    def remove_name_from_history(index):
        if 0 <= index < len(greeting_history):
            del greeting_history[index]
            update_history_view()

    def clear_history(_):
        greeting_history.clear()
        update_history_view()

    def get_greeting(name):
        now = datetime.now()
        hour = now.hour

        if 6 <= hour < 12:
            return f"Доброе утро, {name}!"
        elif 12 <= hour < 18:
            return f"Добрый день, {name}!"
        elif 18 <= hour < 24:
            return f"Добрый вечер, {name}!"
        else:
            return f"Доброй ночи, {name}!"

    def on_button_click(_):
        name = name_input.value.strip()

        if name:
            greeting_text.value = get_greeting(name)
            now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            greeting_history.append(f"{now}: {name}")
            update_history_view()
        else:
            greeting_text.value = "Пожалуйста, введите имя!"

        page.update()

    def toggle_theme(_):
        if page.theme_mode == ft.ThemeMode.LIGHT:
            page.theme_mode = ft.ThemeMode.DARK
        else:
            page.theme_mode = ft.ThemeMode.LIGHT
        page.update()

    greet_button = ft.ElevatedButton('Поздороваться снова', on_click=on_button_click)
    theme_button = ft.IconButton(icon=ft.Icons.BRIGHTNESS_7, tooltip="Переключить тему", on_click=toggle_theme)
    clear_button = ft.IconButton(icon=ft.Icons.DELETE, tooltip="Очистить историю", on_click=clear_history)

    history_column = ft.Column([])
    update_history_view()

    top_row = ft.Row([theme_button, ft.Text("Очистить историю"), clear_button],
                     alignment=ft.MainAxisAlignment.CENTER)

    page.add(ft.Column(controls=[
        top_row,
        greeting_text,
        name_input,
        greet_button,
        history_column
    ], alignment=ft.MainAxisAlignment.CENTER))


ft.app(target=main, view=ft.WEB_BROWSER)
