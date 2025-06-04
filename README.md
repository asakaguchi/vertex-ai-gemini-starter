# Vertex AI Gemini API スターターキット

Vertex AI経由でGemini APIを使い始めるためのテンプレートリポジトリです。

## 🚀 クイックスタート

### 1. このテンプレートを使う

GitHubで「Use this template」ボタンをクリックして、自分のリポジトリを作成してください。

### 2. クローンして環境構築

```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
cd YOUR_REPO_NAME

# 環境変数を設定
cp .env.example .env
# .env ファイルを編集して GCP_PROJECT_ID を設定

# パッケージをインストール（uvを使用）
uv sync

# または、pipを使用する場合
pip install -r requirements.txt
```

### 3. 認証設定

```bash
gcloud auth application-default login
```

### 4. サンプルを実行

```bash
# シンプルなチャット
python examples/simple_chat.py
# または: uv run python examples/simple_chat.py

# 画像解析
python examples/image_analysis.py --image-uri gs://your-bucket/image.jpg

# ストリーミングチャット
python examples/streaming_chat.py

# モデル可用性チェック
python -m vertex_ai_gemini.models
```

## 📋 前提条件

- macOS (または Linux)
- Python 3.9以上
- uv パッケージマネージャー（推奨）または pip
- gcloud CLI
- Google Cloud プロジェクト（Vertex AI API が有効）

## 📁 プロジェクト構造

```
vertex-ai-gemini-starter/
├── README.md
├── LICENSE
├── setup.py              # パッケージ設定
├── requirements.txt      # 依存関係
├── vertex_ai_gemini/     # メインパッケージ
│   ├── __init__.py
│   ├── chat.py          # テキスト生成
│   ├── streaming.py     # ストリーミングチャット
│   ├── vision.py        # 画像解析
│   └── models.py        # モデル確認
├── examples/            # 実行可能なサンプル
│   ├── simple_chat.py
│   ├── streaming_chat.py
│   └── image_analysis.py
├── tests/               # テストファイル
│   ├── context.py
│   └── __init__.py
└── docs/
    └── quickstart.md
```

## 🛠️ トラブルシューティング

### APIが有効になっていないエラー

```bash
gcloud services enable aiplatform.googleapis.com
```

### 認証エラー

```bash
gcloud auth application-default login --force
```

## 📖 ドキュメント

- [クイックスタートガイド](docs/quickstart.md) - 詳細な導入手順とトラブルシューティング

## 📝 ライセンス

MIT License - 詳細は [LICENSE](LICENSE) ファイルを参照してください。
