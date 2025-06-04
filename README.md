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

# パッケージをインストール
uv sync
```

### 3. 認証設定

```bash
gcloud auth application-default login
```

### 4. サンプルを実行

```bash
# シンプルなチャット
uv run python src/simple_chat.py

# 画像解析
uv run python src/image_analysis.py --image-uri gs://your-bucket/image.jpg

# ストリーミングチャット
uv run python src/streaming_chat.py
```

## 📋 前提条件

- macOS (または Linux)
- Python 3.9以上
- uv パッケージマネージャー
- gcloud CLI
- Google Cloud プロジェクト（Vertex AI API が有効）

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

社内利用のため、ライセンスは設定していません。
