from flet import Page, TextField, Row, IconButton
from flet import MainAxisAlignment
from flet import app, AppView


def main(page: Page) -> None:
    page.vertical_alignment = MainAxisAlignment.CENTER
    value_ = TextField(value = "0")

    def add(e):
        value_.value = str(int(value_.value) + 1)
        page.update()

    def sub(e):
        value_.value = str(int(value_.value) - 1)
        page.update()


    
    page.add(
        Row(
            controls = [
                IconButton("remove", on_click=sub),
                value_,
                IconButton("Add", on_click=add),
            ],
            alignment=MainAxisAlignment.CENTER
        )        
    )


if __name__ == "__main__":
    app(target = main, view=AppView.WEB_BROWSER, port=50724)