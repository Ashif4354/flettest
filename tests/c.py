from flet import Page, WebView, AppView, app

def main(page: Page) -> None:
    page.add(
        WebView(
            url="https://www.google.com",
            expand=True
        )
    )


if __name__ == "__main__":
    # app(target = main, view=AppView.WEB_BROWSER, port=50724)
    app(target = main)