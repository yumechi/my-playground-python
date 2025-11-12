# Textual プロジェクト設定

## プロジェクト概要
Textual フレームワーク（Python製のターミナルUIフレームワーク）の学習用プロジェクトです。

## 環境構築方針
- **パッケージマネージャー**: mise で uv をインストール
- **Python バージョン**: 3.12以上を要求
- **依存関係管理**: pyproject.toml と uv.lock を使用
- **コードフォーマッタ**: ruff

## Textual について
Textual は Python 用のモダンなターミナル UI フレームワークです。以下の特徴があります：
- リアクティブな UI コンポーネント
- CSS ライクなスタイリング
- マウス・キーボード操作のサポート
- 非同期処理のサポート

## 環境セットアップ

### 初期セットアップ
```bash
# プロジェクト初期化
uv init

# Textual のインストール
uv add textual

# 開発依存関係の追加（必要に応じて）
uv add --dev mypy ruff pytest textual-dev
```

### 依存関係の同期
```bash
uv sync
```

## 開発フロー

### アプリケーション実行
```bash
# 通常実行
uv run python <スクリプト名>

# Textual 開発モード（リアルタイムリロード）
uv run textual run --dev <スクリプト名>

# Textual コンソール（デバッグ用）
uv run textual console
```

### コードフォーマット・リント
```bash
# フォーマット実行
uv run ruff format .

# リント実行
uv run ruff check .

# リント自動修正
uv run ruff check --fix .
```

### 型チェック
```bash
uv run mypy src/
```

### テスト実行
```bash
uv run pytest
```

## Textual の基本構造

### 基本的なアプリケーション例
```python
from textual.app import App, ComposeResult
from textual.widgets import Header, Footer, Button

class MyApp(App):
    """シンプルな Textual アプリケーション"""

    def compose(self) -> ComposeResult:
        yield Header()
        yield Button("Click me!", id="btn")
        yield Footer()

    def on_button_pressed(self, event: Button.Pressed) -> None:
        self.exit()

if __name__ == "__main__":
    app = MyApp()
    app.run()
```

## 便利なコマンド

### Textual のデザインシステムを確認
```bash
uv run textual colors
uv run textual borders
uv run textual easing
uv run textual keys
```

## 注意事項
- Textual アプリは非同期処理を多用するため、async/await の理解が必要
- CSS ファイルを別途作成してスタイリングすることも可能
- デバッグには `textual console` を別ターミナルで起動すると便利
