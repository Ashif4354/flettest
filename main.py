import flet as ft
from time import sleep


def main(page: ft.Page):
    # page.adaptive = True
    page.add(ft.SafeArea(ft.Text("Hello, Flet!")))
    t = ft.Text(value=page.route, color="green")
    page.add(t)

    page.add(
        ft.Row(controls=[
            ft.Text("A"),
            ft.Text("B"),
            ft.Text("C")
        ])
    )

    smn_ = ft.TextField(hint_text="What's your name?", width=300)

    def on_click_say_my_name(e):
        if not smn_.value:
            smn_.focus()
        if smn_.value:
            page.clean()
            def reset(e):
                page.clean()
                page.add(main(page))
            reset_btn = ft.ElevatedButton("Reset", on_click=reset)
            page.add(ft.Text(f"Hello, {smn_.value}!"), reset_btn)

    page.add(
        ft.ResponsiveRow(controls=[
            smn_,
            ft.ElevatedButton(on_click=on_click_say_my_name, text="Say my name!")
        ])
    )

    def add_clicked(e):
        if new_task.value:
            page.add(ft.Checkbox(label=new_task.value))
            new_task.value = ""
            new_task.focus()
            new_task.update()

    new_task = ft.TextField(hint_text="What's needs to be done?", width=300)
    page.add(ft.Row([new_task, ft.ElevatedButton("Add", on_click=add_clicked)]))

    first_name = ft.TextField(label="First name")
    # first_name.error_text = "This field is required" 
    last_name = ft.TextField(label="Last name")
    c = ft.Column(controls=[
        first_name,
        last_name
    ])
    # last_name.visible = False
    # c.disabled = True
    page.add(c)

    def dd_button_clicked(e):
        output_text.value = f"Dropdown value is:  {color_dropdown.value}"
        page.update()

    output_text = ft.Text()
    submit_btn = ft.ElevatedButton(text="Submit", on_click=dd_button_clicked)
    color_dropdown = ft.Dropdown(
        width=100,
        options=[
            ft.dropdown.Option("Red"),
            ft.dropdown.Option("Green"),
            ft.dropdown.Option("Blue"),
        ],
    )
    page.add(color_dropdown, submit_btn, output_text)
    page.update()


ft.app(main)
