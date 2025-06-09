# Vertex AI Gemini API スターターキット

Vertex AI 経由で Gemini API を使い始めるためのテンプレートリポジトリです。

## 🔒 セキュリティを重視した設計

**重要な特徴：API キーやサービスアカウントキーを一切使用しません。**

このプロジェクトは、Google が推奨する **Application Default Credentials (ADC)** を使用した安全な設計です。

- ✅ **ゼロキー設計**: API キーやサービスアカウントキーが不要
- ✅ **個人認証**: 各開発者が自分の Google アカウントで安全に認証
- ✅ **誤コミット防止**: キーファイルの Git 誤コミットリスクを完全に排除
- ✅ **エンタープライズ対応**: 企業のセキュリティポリシーにも準拠

詳細は [クイックスタートガイド](docs/quickstart.md) を参照してください。

## 🚀 クイックスタート

### 1. このテンプレートを使う

1. このリポジトリページの画面右上にある緑色の「**Use this template**」ボタンをクリック
2. 「**Create a new repository**」を選択
3. 自分のリポジトリ名を入力して作成

### 2. クローンして環境構築

```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
cd YOUR_REPO_NAME
```

環境変数を設定：

```bash
cp .env.example .env
```

`.env` ファイルを編集して `GCP_PROJECT_ID` を設定してから、パッケージをインストール：

```bash
uv sync
```

### 3. 認証設定

```bash
gcloud auth application-default login
```

### 4. サンプルを実行

まずは基本的なチャットから始めましょう：

```bash
# シンプルなチャット
uv run python examples/simple_chat.py
```

慣れてきたら他のサンプルも試してみてください：

```bash
# ストリーミングチャット
uv run python examples/streaming_chat.py
```

## 📋 前提条件

- macOS (または Linux)
- Python 3.9 以上
- uv パッケージマネージャー（必須）
- gcloud CLI
- Google Cloud プロジェクト（Vertex AI API が有効）

## 📁 プロジェクト構造

```text
vertex-ai-gemini-starter/
├── README.md
├── LICENSE
├── CLAUDE.md            # 開発ガイドライン
├── pyproject.toml       # 依存関係とツール設定
├── .pre-commit-config.yaml  # コード品質チェック
├── .env.example         # 環境変数のサンプル
├── examples/            # すぐに実行できるサンプル
│   ├── simple_chat.py   # 基本的なチャット
│   ├── streaming_chat.py # ストリーミングチャット
│   └── image_analysis.py # 画像解析
├── tests/               # テストファイル
│   ├── context.py
│   ├── test_basic.py
│   └── __init__.py
└── docs/
    └── quickstart.md    # 詳細ガイド
```

## 🚀 さらに高度な機能

基本的な使い方をマスターしたら、画像解析も試してみてください：

```bash
# 画像解析（事前に Cloud Storage に画像をアップロード）
uv run python examples/image_analysis.py --image-uri gs://your-bucket/image.jpg
```

## 🛠️ 開発者向けコマンド

### コード品質チェック

```bash
# コードフォーマット
uv run --frozen ruff format .

# リンティング
uv run --frozen ruff check .

# 型チェック
uv run --frozen pyright

# テスト実行
uv run --frozen pytest

# Pre-commit 設定
uv run pre-commit install
```

### トラブルシューティング

#### API が有効になっていないエラー

```bash
gcloud services enable aiplatform.googleapis.com
```

#### 認証エラー

```bash
gcloud auth application-default login --force
```

## 📖 ドキュメント

- [クイックスタートガイド](docs/quickstart.md) - 詳細な導入手順とトラブルシューティング
- [CLAUDE.md](CLAUDE.md) - 開発ガイドラインと品質基準

## 📝 ライセンス

MIT License - 詳細は [LICENSE](LICENSE) ファイルを参照してください。
