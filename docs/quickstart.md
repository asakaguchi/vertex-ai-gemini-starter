# Vertex AI Gemini API を始めよう！クイックスタートガイド

最近話題の Gemini、使ってみたいけど何から始めればいいか分からない...そんな声をよく聞きます。このガイドでは、macOS で Vertex AI 経由の Gemini API を使い始めるための最小限の手順をまとめました。

GitHub テンプレートリポジトリも用意したので、コピーして 5 分で動かせます。難しく考える必要はありません。

## 🔒 セキュリティを重視した設計

**このプロジェクトの重要な特徴：API キーやサービスアカウントキーを一切使用しません。**

### なぜキーファイルを使わないのか？

従来の多くのチュートリアルでは、サービスアカウントキー（JSON ファイル）や API キーを使用していますが、これには以下のリスクがあります。

- ❌ **誤コミットリスク**: キーファイルを Git に誤ってコミットしてしまう危険性
- ❌ **キー管理の複雑さ**: キーの配布、ローテーション、削除の管理が煩雑
- ❌ **共有時の漏洩リスク**: チームでファイル共有する際の情報漏洩リスク

### このプロジェクトの安全なアプローチ

代わりに、Google が推奨する **Application Default Credentials (ADC)** を使用します。

- ✅ **ゼロキー設計**: API キーやサービスアカウントキーが不要
- ✅ **個人認証**: 各開発者が自分の Google アカウントで安全に認証
- ✅ **自動認証**: `gcloud auth application-default login` で一度設定すれば完了
- ✅ **エンタープライズ対応**: 企業のセキュリティポリシーにも準拠

この方式により、**セキュリティを犠牲にすることなく、簡単に Vertex AI Gemini API を使い始められます**。

## まずは Vertex AI Gemini API って何？

簡単に言うと、Google の AI モデル「Gemini」を自分のプログラムから使えるようにするサービスです。チャットボットを作ったり、画像を解析したり、いろんなことができます。

Vertex AI を経由することで、より安全に、そして企業向けの機能を使いながら Gemini を活用できるようになります。セキュリティも安心です。

## 事前準備：macOS での環境セットアップ

### uv のインストール（まだの人だけ）

Python のパッケージ管理には、高速で使いやすい `uv` を使います。Homebrew でさくっとインストールしましょう。

```bash
brew install uv
```

### gcloud CLI のインストール

Google Cloud とやりとりするためのツールです。こちらも Homebrew で簡単にインストールできます。

```bash
brew install google-cloud-sdk
```

インストールが完了したら、初期化します。

```bash
gcloud init
```

プロジェクトを選択する画面が出てきますので、使いたいプロジェクトを選んでください。

## 3 ステップで始める Vertex AI Gemini API

### ステップ 1：サービスアカウントを作る

サービスアカウントは、プログラムが使う専用の Google アカウントみたいなものです。人間用のアカウントとは別に、アプリケーション専用のアカウントを作ります。

【Google Cloud Console での作成手順】

1. Google Cloud Console を開いて、プロジェクトを選択
2. 「IAM と管理」→「サービスアカウント」へ移動
3. 「サービスアカウントを作成」をクリック
4. 分かりやすい名前をつける（例：`gemini-test-sa`）
5. ロールは「Vertex AI ユーザー」を選択
6. 「完了」をクリック

画像を扱いたい場合は「ストレージ オブジェクト閲覧者」も追加しておくと便利です。このステップは最初だけなので、頑張りましょう。

### ステップ 2：ローカル環境の認証設定

開発マシンで認証設定をします。これもコマンド 1 つで完了します。

```bash
gcloud auth application-default login
```

ブラウザが開いて、Google アカウントでログインを求められます。ログインしたら準備完了です。

【ちょっとした補足】
この設定により、コード内に認証情報を書く必要がなくなります。セキュリティ的にも安心ですね。認証情報は `~/.config/gcloud/` に保存されます。

### ステップ 3：テンプレートリポジトリで即座に試す

面倒な設定は抜きにして、すぐに動かしたいですよね。GitHub テンプレートリポジトリを用意しました。

```bash
# テンプレートから新しいリポジトリを作成
# 1. GitHubリポジトリページの画面右上にある緑色の「Use this template」ボタンをクリック
# 2. 「Create a new repository」をクリック
# 3. リポジトリ名を入力して「Create repository」をクリック

# クローンしたら
cd vertex-ai-gemini-starter
```

プロジェクト構成はこんな感じです。

```text
vertex-ai-gemini-starter/
├── .gitignore
├── README.md
├── LICENSE
├── setup.py            # パッケージ設定
├── requirements.txt    # 依存関係
├── pyproject.toml      # uv の設定ファイル
├── .env.example        # 環境変数のサンプル
├── vertex_ai_gemini/   # メインパッケージ
│   ├── __init__.py
│   ├── chat.py         # シンプルなチャット
│   ├── streaming.py    # ストリーミングチャット
│   ├── vision.py       # 画像解析
│   └── models.py       # モデル確認
├── examples/           # 実行可能なサンプル
│   ├── simple_chat.py
│   ├── streaming_chat.py
│   └── image_analysis.py
├── tests/              # テストファイル
│   ├── __init__.py
│   └── context.py
└── docs/
    └── quickstart.md
```

セットアップは超簡単です。

```bash
# 環境変数を設定
cp .env.example .env
# .env ファイルを編集してプロジェクトIDを記入

# パッケージをインストール
uv sync

# サンプルを実行
python examples/simple_chat.py
# または: uv run python examples/simple_chat.py
```

たったこれだけで、Gemini と会話ができるようになります。

## サンプルコードの中身

### シンプルなチャット（examples/simple_chat.py）

```python
import os
from dotenv import load_dotenv
import vertexai
from vertexai.generative_models import GenerativeModel

# 環境変数を読み込み
load_dotenv()

# プロジェクトIDとリージョンを環境変数から取得
PROJECT_ID = os.getenv("GCP_PROJECT_ID")
LOCATION = os.getenv("GCP_LOCATION", "us-central1")

# 初期化
vertexai.init(project=PROJECT_ID, location=LOCATION)

# モデルを準備
model = GenerativeModel("gemini-1.5-flash-001")

# 質問してみる
response = model.generate_content("こんにちは！今日の気分はどう？")
print(response.text)
```

環境変数を使うことで、プロジェクト ID をコードにハードコーディングしなくて済みます。チームで共有する時も安心です。

### pyproject.tomlの構成

```toml
[project]
name = "vertex-ai-gemini-starter"
version = "0.1.0"
description = "Vertex AI Gemini API スターターキット"
requires-python = ">=3.9"
dependencies = [
    "google-cloud-aiplatform>=1.38",
    "python-dotenv>=1.0.0",
    "rich>=13.0.0",
]

[tool.uv]
dev-dependencies = [
    "ipython",  # デバッグ用
]
```

最小限の依存関係だけを含めています。必要に応じて追加してください。

## よくあるトラブルと解決方法

### 「API が有効になっていません」エラー

これ、本当によく忘れます。Google Cloud Console で「API とサービス」→「ライブラリ」から「Vertex AI API」を検索して有効にしてください。

### プロジェクト ID が分からない

`.env`ファイルに記入するプロジェクト ID は、以下のコマンドで確認できます。

```bash
gcloud config get-value project
```

### 認証エラーが出る

macOS の場合、たまに認証情報のキャッシュがおかしくなることがあります。

```bash
# 認証情報をリフレッシュ
gcloud auth application-default login --force
```

それでもダメな場合は、一度認証情報を削除してやり直してみましょう。

```bash
rm ~/.config/gcloud/application_default_credentials.json
gcloud auth application-default login
```

## もっと楽しくするアイデア

テンプレートリポジトリには、他にも楽しいサンプルを入れています。

【画像解析を試す】

```bash
python examples/image_analysis.py --image-uri gs://your-bucket/photo.jpg
```

【ストリーミングチャットを試す】

```bash
python examples/streaming_chat.py
```

【モデル可用性チェック】

```bash
python -m vertex_ai_gemini.models
```

## まとめ

Vertex AI Gemini API は、uv と GitHub テンプレートを使えば本当に簡単に始められます。まずはテンプレートをコピーして、`uv run` で動かしてみてください。

きっと「え、こんなに簡単なの？」と驚くはずです。

【テンプレートリポジトリ】

[GitHub リポジトリ](https://github.com/asakaguchi/vertex-ai-gemini-starter)

テンプレートとして使用する場合は、上記ページの画面右上にある緑色の「Use this template」ボタンをクリックして、「Create a new repository」を選択してください。
