# Vertex AI Gemini API を始めよう！クイックスタートガイド

最近話題のGemini、使ってみたいけど何から始めればいいか分からない...そんな声をよく聞きます。このガイドでは、macOSでVertex AI経由のGemini APIを使い始めるための最小限の手順をまとめました。

GitHubテンプレートリポジトリも用意したので、コピーして5分で動かせます。難しく考える必要はありません。

## 🔒 セキュリティを重視した設計

**このプロジェクトの重要な特徴：APIキーやサービスアカウントキーを一切使用しません。**

### なぜキーファイルを使わないのか？

従来の多くのチュートリアルでは、サービスアカウントキー（JSONファイル）やAPIキーを使用していますが、これには以下のリスクがあります：

- ❌ **誤コミットリスク**: キーファイルをGitに誤ってコミットしてしまう危険性
- ❌ **キー管理の複雑さ**: キーの配布、ローテーション、削除の管理が煩雑
- ❌ **共有時の漏洩リスク**: チームでファイル共有する際の情報漏洩リスク

### このプロジェクトの安全なアプローチ

代わりに、Googleが推奨する **Application Default Credentials (ADC)** を使用します：

- ✅ **ゼロキー設計**: APIキーやサービスアカウントキーが不要
- ✅ **個人認証**: 各開発者が自分のGoogleアカウントで安全に認証
- ✅ **自動認証**: `gcloud auth application-default login`で一度設定すれば完了
- ✅ **エンタープライズ対応**: 企業のセキュリティポリシーにも準拠

この方式により、**セキュリティを犠牲にすることなく、簡単にVertex AI Gemini APIを使い始められます**。

## まずはVertex AI Gemini APIって何？

簡単に言うと、GoogleのAIモデル「Gemini」を自分のプログラムから使えるようにするサービスです。チャットボットを作ったり、画像を解析したり、いろんなことができます。

Vertex AIを経由することで、より安全に、そして企業向けの機能を使いながらGeminiを活用できるようになります。セキュリティも安心です。

## 事前準備：macOSでの環境セットアップ

### uvのインストール（まだの人だけ）

Pythonのパッケージ管理には、高速で使いやすい`uv`を使います。Homebrewでさくっとインストールしましょう。

```bash
brew install uv
```

### gcloud CLIのインストール

Google Cloudとやりとりするためのツールです。こちらもHomebrewで簡単にインストールできます。

```bash
brew install google-cloud-sdk
```

インストールが完了したら、初期化します。

```bash
gcloud init
```

プロジェクトを選択する画面が出てきますので、使いたいプロジェクトを選んでください。

## 3ステップで始めるVertex AI Gemini API

### ステップ1：サービスアカウントを作る

サービスアカウントは、プログラムが使う専用のGoogleアカウントみたいなものです。人間用のアカウントとは別に、アプリケーション専用のアカウントを作ります。

【Google Cloud Consoleでの作成手順】

1. Google Cloud Consoleを開いて、プロジェクトを選択
2. 「IAMと管理」→「サービスアカウント」へ移動
3. 「サービスアカウントを作成」をクリック
4. 分かりやすい名前をつける（例：`gemini-test-sa`）
5. ロールは「Vertex AI ユーザー」を選択
6. 「完了」をクリック

画像を扱いたい場合は「ストレージ オブジェクト閲覧者」も追加しておくと便利です。このステップは最初だけなので、頑張りましょう。

### ステップ2：ローカル環境の認証設定

開発マシンで認証設定をします。これもコマンド1つで完了します。

```bash
gcloud auth application-default login
```

ブラウザが開いて、Googleアカウントでログインを求められます。ログインしたら準備完了です。

【ちょっとした補足】
この設定により、コード内に認証情報を書く必要がなくなります。セキュリティ的にも安心ですね。認証情報は`~/.config/gcloud/`に保存されます。

### ステップ3：テンプレートリポジトリで即座に試す

面倒な設定は抜きにして、すぐに動かしたいですよね。GitHubテンプレートリポジトリを用意しました。

```bash
# テンプレートから新しいリポジトリを作成
# GitHubで「Use this template」ボタンをクリック

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
├── pyproject.toml      # uvの設定ファイル
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
# .envファイルを編集してプロジェクトIDを記入

# パッケージをインストール
uv sync

# サンプルを実行
python examples/simple_chat.py
# または: uv run python examples/simple_chat.py
```

たったこれだけで、Geminiと会話ができるようになります。

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

環境変数を使うことで、プロジェクトIDをコードにハードコーディングしなくて済みます。チームで共有する時も安心です。

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

### 「APIが有効になっていません」エラー

これ、本当によく忘れます。Google Cloud Consoleで「APIとサービス」→「ライブラリ」から「Vertex AI API」を検索して有効にしてください。

### プロジェクトIDが分からない

`.env`ファイルに記入するプロジェクトIDは、以下のコマンドで確認できます。

```bash
gcloud config get-value project
```

### 認証エラーが出る

macOSの場合、たまに認証情報のキャッシュがおかしくなることがあります。

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

リアルタイムで回答が表示されるので、体感速度が全然違います。

## 開発のコツ

### VS Codeでの開発

VS Codeを使っている場合、以下の設定をしておくと便利です。

```json
// .vscode/settings.json
{
  "python.defaultInterpreterPath": ".venv/bin/python",
  "python.terminal.activateEnvironment": true
}
```

uvが作成した仮想環境を自動的に認識してくれます。

### デバッグのコツ

レスポンスの中身を詳しく見たい時は、iPythonを使うと便利です。

```bash
uv run ipython
```

```python
# iPython内で
from vertex_ai_gemini import simple_chat
# モジュールとして使用する場合の例
```

## 次のステップ

ここまでできたら、基本的な使い方はマスターです。テンプレートリポジトリをベースに、自分のアプリケーションを作ってみましょう。

【挑戦してみたいこと】

- Function Calling（外部ツールとの連携）
- RAG（検索拡張生成）の実装
- Slackボットへの組み込み

【本番環境への展開】

- Cloud Runへのデプロイ
- GitHub Actionsでの自動テスト
- エラーモニタリングの設定

## まとめ

Vertex AI Gemini APIは、uvとGitHubテンプレートを使えば本当に簡単に始められます。まずはテンプレートをコピーして、`uv run`で動かしてみてください。

きっと「え、こんなに簡単なの？」と驚くはずです。

何か分からないことがあれば、GitHub Issuesやコミュニティで聞いてください。みんなで一緒にAIを活用していきましょう！

【テンプレートリポジトリ】

[GitHub リポジトリ](https://github.com/asakaguchi/vertex-ai-gemini-starter)

テンプレートとして使用する場合は、上記ページで「Use this template」ボタンをクリックしてください。
