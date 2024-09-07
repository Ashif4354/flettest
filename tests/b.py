from flet import Page, Row, Column, app, AppView, Text, Container, ResponsiveRow

def main(page: Page) -> None:

    text = lambda color: Text("Hello World!", color=color)



    page.add(
        ResponsiveRow(
            controls = [

                Container(
                    content=text("green"),
                    bgcolor="yellow",
                    expand=True,
                    # height=page.window.height,
                    width=200,
                    col={
                        'sm': 12,
                        'xl': 6,
                        'xxl': 4
                    }
                ),

        
                Container(
                    content=text("red"),
                    bgcolor="green",
                    expand=True,
                    # height=page.window.height,
                    width=200,
                    col={
                        'sm': 12,
                        'xl': 6,
                        'xxl': 4
                    }
                ),

                Container(
                    content=text("yellow"),
                    bgcolor="blue",
                    expand=True,
                    # height=page.window.height,
                    width=200,
                    col={
                        'sm': 12,
                        'xl': 6,
                        'xxl': 4
                    }
                )
            ]        
        )
    )

    # page.add(
    #     ResponsiveRow([
    #         Column(controls=[Text("Column 1")]),
    #         Column(controls=[Text("Column 2")])
    #     ])
    # )

if __name__ == "__main__":
    # app(target = main, view=AppView.WEB_BROWSER, port=50724)
    app(target = main)
