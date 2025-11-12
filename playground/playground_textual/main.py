"""
Textual サンプルアプリケーション

ボタンをクリックしてカウンターを増やしたり、アプリを終了したりできます。
"""

from textual.app import App, ComposeResult
from textual.containers import Container, Vertical
from textual.widgets import Button, Footer, Header, Static


class CounterApp(App):
    """シンプルなカウンターアプリケーション"""

    CSS = """
    Container {
        align: center middle;
    }

    Vertical {
        width: 60;
        height: auto;
        border: solid green;
        background: $surface;
        padding: 2;
    }

    #counter {
        content-align: center middle;
        text-style: bold;
        color: cyan;
        height: 5;
    }

    Button {
        width: 100%;
        margin: 1;
    }
    """

    def __init__(self):
        super().__init__()
        self.count = 0

    def compose(self) -> ComposeResult:
        """UI コンポーネントを構成"""
        yield Header()
        with Container():
            with Vertical():
                yield Static(f"カウント: {self.count}", id="counter")
                yield Button("カウントアップ ⬆", id="increment", variant="success")
                yield Button("リセット 🔄", id="reset", variant="warning")
                yield Button("終了 ❌", id="quit", variant="error")
        yield Footer()

    def on_button_pressed(self, event: Button.Pressed) -> None:
        """ボタンが押されたときの処理"""
        button_id = event.button.id

        if button_id == "increment":
            self.count += 1
            self.update_counter()
        elif button_id == "reset":
            self.count = 0
            self.update_counter()
        elif button_id == "quit":
            self.exit()

    def update_counter(self) -> None:
        """カウンター表示を更新"""
        counter = self.query_one("#counter", Static)
        counter.update(f"カウント: {self.count}")


def main():
    """アプリケーションを実行"""
    app = CounterApp()
    app.run()


if __name__ == "__main__":
    main()
