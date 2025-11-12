# Claude Code プロジェクト設定

## プロジェクト概要
Pythonフレームワーク周りと動作検証のための学習リポジトリです。

## 環境構築方針
- **パッケージマネージャー**: mise で uv をインストール
- **Python バージョン**: 3.12以上を要求
- **依存関係管理**: 各ディレクトリごとに独立したパッケージ管理
- **設定ファイル**: pyproject.toml と uv.lock を使用
- **コードフォーマッタ**: ruff（blackから移行済み）

## ディレクトリ構成
各ディレクトリは独立したプロジェクトとして管理されています：

- `behave_practice/` - BDD テストフレームワーク Behave の練習
- `start_qrcode/` - QRコード生成の練習
- `start_streamlit/` - Streamlit アプリケーションの練習
- `playground/new_feature/` - Python新機能の学習
- `playground/try_fastapi/` - FastAPI フレームワークの学習
- `playground/try_plyer/` - Plyer ライブラリの学習
- `playground/try_ray/` - Ray 分散処理フレームワークの学習
- `disposable/` - 使い捨てスクリプト置き場

## 開発フロー

### 環境セットアップ
```bash
# 各プロジェクトディレクトリで実行
cd <プロジェクトディレクトリ>
uv sync
```

### 依存関係の追加
```bash
uv add <パッケージ名>
```

### 開発依存関係の追加
```bash
uv add --dev <パッケージ名>
```

### コード実行
```bash
uv run python <スクリプト名>
```

### 型チェック（mypyが設定されている場合）
```bash
uv run mypy src/
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

### テスト実行（テストが存在する場合）
```bash
uv run pytest
```

## 注意事項
- 各ディレクトリは独立したプロジェクトとして管理
- 新しいプロジェクトを追加する際は、該当ディレクトリで `uv init` を実行
- 依存関係の競合を避けるため、プロジェクト間での依存関係の共有は行わない