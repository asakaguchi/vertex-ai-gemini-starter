# Vertex AI Gemini API スターターキット

Vertex AI 経由で Gemini API を使い始めるためのテンプレートリポジトリです。

## 🔒 セキュリティを重視した設計

**重要な特徴：API キーやサービスアカウントキーを一切使用しません。**

このプロジェクトは、Google が推奨する **Application Default Credentials (ADC)** を使用した安全な設計です：

- ✅ **ゼロキー設計**: API キーやサービスアカウントキーが不要
- ✅ **個人認証**: 各開発者が自分の Google アカウントで安全に認証
- ✅ **誤コミット防止**: キーファイルの Git 誤コミットリスクを完全に排除
- ✅ **エンタープライズ対応**: 企業のセキュリティポリシーにも準拠

詳細は [クイックスタートガイド](docs/quickstart.md) をご覧ください。

## 🚀 クイックスタート

### 1. このテンプレートを使う

GitHub で「Use this template」ボタンをクリックして、自分のリポジトリを作成してください。

### 2. クローンして環境構築

```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
cd YOUR_REPO_NAME

# 環境変数を設定
cp .env.example .env
# .env ファイルを編集して GCP_PROJECT_ID を設定

# パッケージをインストール（uv を使用）
uv sync

# または、pip を使用する場合
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
- Python 3.9 以上
- uv パッケージマネージャー（推奨）または pip
- gcloud CLI
- Google Cloud プロジェクト（Vertex AI API が有効）

## 📁 プロジェクト構造

```text
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

### API が有効になっていないエラー

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
