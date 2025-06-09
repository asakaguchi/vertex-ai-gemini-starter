# Vertex AI Gemini API を始めよう！クイックスタートガイド

最近話題の Gemini、使ってみたいけど何から始めればいいか分からない...そんな声をよく聞きます。このガイドでは、macOS で Vertex AI 経由の Gemini API を使い始めるための最小限の手順をまとめました。

GitHub テンプレートリポジトリも用意したので、コピーして 5 分で動かせます。難しく考える必要はありません。

## 🔒 セキュリティを重視した設計

**このプロジェクトの重要な特徴：API キーやサービスアカウントキーを一切使用しません。**

### なぜキーファイルを使わないのか？

従来の多くのチュートリアルでは、サービスアカウントキー（JSON ファイル）や API キーを使用していますが、これには以下のリスクがあります。

- ❌ **誤コミットリスク**：キーファイルを Git に誤ってコミットしてしまう危険性
- ❌ **キー管理の複雑さ**：キーの配布、ローテーション、削除の管理が煩雑
- ❌ **共有時の漏洩リスク**：チームでファイル共有する際の情報漏洩リスク

### このプロジェクトの安全なアプローチ

代わりに、Google が推奨する **Application Default Credentials（ADC）**を使用します。

- ✅ **ゼロキー設計**：API キーやサービスアカウントキーが不要
- ✅ **個人認証**：各開発者が自分の Google アカウントで安全に認証
- ✅ **自動認証**：`gcloud auth application-default login` で一度設定すれば完了
- ✅ **エンタープライズ対応**：企業のセキュリティポリシーにも準拠

この方式により、**セキュリティを犠牲にすることなく、簡単に Vertex AI Gemini API を使い始められます**。

> 💡 **ADC 認証をもっと詳しく理解したい方へ**  
> このクイックスタートで設定した ADC 認証の仕組みや、複数プロジェクトでの活用方法について、詳細な解説を用意しました。  
> → [ADC 認証でらくらく複数プロジェクト開発ガイド](adc-guide-with-diagrams.md)

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

## 4 ステップで始める Vertex AI Gemini API

### ステップ 1：サービスアカウントを作る

サービスアカウントは、プログラムが使う専用の Google アカウントみたいなものです。人間用のアカウントとは別に、アプリケーション専用のアカウントを作ります。

【Google Cloud Console での作成手順】

1. Google Cloud Console を開いて、プロジェクトを選択
2. 「IAM と管理」→「サービスアカウント」へ移動
3. 「サービスアカウントを作成」をクリック
4. 分かりやすい名前をつける（例：`gemini-test-sa`）
5. ロールは「Vertex AI ユーザー」を選択
6. 「完了」をクリック

画像や PDF などのファイルを扱いたい場合は「ストレージ オブジェクト閲覧者」も追加しておくと便利です。このステップは最初だけなので、頑張りましょう。

### ステップ 2：ローカル環境の認証設定

開発マシンで認証設定をします。これもコマンド 1 つで完了します。

```bash
gcloud auth application-default login
```

ブラウザが開いて、Google アカウントでログインを求められます。ログインしたら準備完了です。

【ちょっとした補足】
この設定により、コード内に認証情報を書く必要がなくなります。セキュリティ的にも安心ですね。認証情報は `~/.config/gcloud/` に保存されます。

### ステップ 3：Vertex AI API の有効化

Google Cloud プロジェクトで Vertex AI API を有効にします。これも 1 つのコマンドで完了します。

```bash
gcloud services enable aiplatform.googleapis.com
```

このコマンドで、プロジェクトで Vertex AI Gemini API が使用できるようになります。

### ステップ 4：テンプレートリポジトリで即座に試す

面倒な設定は抜きにして、すぐに動かしたいですよね。GitHub テンプレートリポジトリを用意しました。

#### テンプレートから新しいリポジトリを作成

1. [GitHub リポジトリページ](https://github.com/asakaguchi/vertex-ai-gemini-starter)にアクセス
2. 画面右上にある緑色の「**Use this template**」ボタンをクリック
3. 「**Create a new repository**」を選択
4. リポジトリ名を入力（例：`my-gemini-project`）
5. 「**Create repository**」をクリック

#### ローカルにクローンして開始

```bash
# 自分のリポジトリをクローン
git clone https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
cd YOUR_REPO_NAME
```

プロジェクト構成はこんな感じです。

```text
vertex-ai-gemini-starter/
├── .gitignore
├── README.md
├── LICENSE
├── CLAUDE.md           # 開発ガイドライン
├── pyproject.toml      # 依存関係とツール設定
├── .pre-commit-config.yaml  # コード品質チェック
├── .env.example        # 環境変数のサンプル
├── examples/           # すぐに実行できるサンプル
│   ├── simple_chat.py  # 基本的なチャット
│   ├── streaming_chat.py # ストリーミングチャット
│   └── image_analysis.py # 画像解析
├── tests/              # テストファイル
│   ├── context.py
│   ├── test_basic.py
│   └── __init__.py
└── docs/
    └── quickstart.md   # 詳細ガイド
```

セットアップは超簡単です。

#### 環境変数を設定

```bash
cp .env.example .env
```

`.env` ファイルを編集してプロジェクト ID を記入してください。

#### パッケージをインストール

```bash
uv sync
```

#### サンプルを実行

```bash
uv run python examples/simple_chat.py
```

たったこれだけで、Gemini と会話ができるようになります。

## 💡 プロジェクトの構成

このプロジェクトはとてもシンプルです。`examples/` フォルダに3つのサンプルファイルがあるだけ：

```text
examples/
├── simple_chat.py    # 基本的なチャット
├── streaming_chat.py # ストリーミングチャット
└── image_analysis.py # 画像解析
```

**使い方**:

1. **最初**: `simple_chat.py` を実行してみる
2. **慣れたら**: `streaming_chat.py` を試す  
3. **発展**: `image_analysis.py` で画像解析

各ファイルはそのまま実行できるので、コードをコピーして自分のプロジェクトに活用することもできます。

## サンプルコードの中身

### シンプルなチャット（examples/simple_chat.py）

```python
import os
from dotenv import load_dotenv
import vertexai
from vertexai.generative_models import GenerativeModel

# 環境変数を読み込み
load_dotenv()

# プロジェクト ID とリージョンを環境変数から取得
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

これ、本当によく忘れます。以下のコマンドで Vertex AI API を有効にできます。

```bash
gcloud services enable aiplatform.googleapis.com
```

もしくは、Google Cloud Console で「API とサービス」→「ライブラリ」から「Vertex AI API」を検索して有効にすることもできます。

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

## 他のサンプルも試してみよう

基本的なチャットができたら、他のサンプルも試してみましょう：

### ストリーミングチャット

リアルタイムで応答が表示される対話的なチャットです：

```bash
uv run python examples/streaming_chat.py
```

終了するには `exit` と入力してください。

### 次のステップ

Vertex AI Gemini API の基本をマスターしたら：

- **画像解析**: `image_analysis.py` で画像を解析してみる
- **コードの活用**: サンプルコードを自分のプロジェクトにコピーして改造
- **本格的な開発**: この基盤を使ったアプリケーション構築

## まとめ

Vertex AI Gemini API は、uv と GitHub テンプレートを使えば本当に簡単に始められます。まずはテンプレートをコピーして、`uv run` で動かしてみてください。

きっと「え、こんなに簡単なの？」と驚くはずです。

### より深く学びたい方へ

基本的な使い方をマスターしたら、次のステップとして以下をお試しください。

- **複数プロジェクトでの開発**：[ADC 認証の詳細ガイド](adc-guide-with-diagrams.md)で、複数の Google Cloud プロジェクトを効率的に切り替える方法を学べます
- **チーム開発**：同じ ADC 方式を使って、チーム全体で安全な開発環境を構築できます
- **本格的なアプリケーション**：この基盤を使って、実際のプロダクトを構築してみましょう

### テンプレートリポジトリ

このプロジェクトを自分用にコピーするには：

1. [GitHub リポジトリ](https://github.com/asakaguchi/vertex-ai-gemini-starter)にアクセス
2. 「**Use this template**」→「**Create a new repository**」を選択
3. 自分のリポジトリ名を入力して作成
4. ローカルにクローンして開発開始

これで、すべての設定が完了した状態で開発を始められます。
