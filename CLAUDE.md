# CLAUDE.md

このファイルは、このリポジトリでコードを扱う際の Claude Code (claude.ai/code) へのガイダンスを提供します。

## プロジェクト概要

これは Vertex AI Gemini API スターターキットで、Vertex AI を通じて Google の Gemini AI モデルを統合するための実用的な例を提供します。テキスト生成、ストリーミングチャット、画像解析、モデルテストユーティリティが含まれています。

## セキュリティ設計の重要ポイント

**このプロジェクトは API キーやサービスアカウントキーを一切使用しません。**

開発時の重要な注意点：
- Application Default Credentials (ADC) を使用した認証方式を採用
- `gcloud auth application-default login` による個人認証が前提
- キーファイルの管理や配布が不要で、Git 誤コミットリスクを排除
- 本番環境では適切な IAM ロールとサービスアカウント設定が必要

## 必須コマンド

```bash
# 環境設定
cp .env.example .env
uv sync

# 認証（すべての例を実行する前に必要）
gcloud auth application-default login

# 必要な Google Cloud API を有効化
gcloud services enable aiplatform.googleapis.com

# 例の実行
python examples/simple_chat.py
python examples/streaming_chat.py
python examples/image_analysis.py --image-uri gs://bucket/image.jpg
python -m vertex_ai_gemini.models

# 開発用
uv add <package>        # 依存関係の追加
uv run pytest          # テスト実行（存在する場合）
```

## アーキテクチャ

プロジェクトは The Hitchhiker's Guide to Python の推奨構造に従います：

- **vertex_ai_gemini/**：メインパッケージディレクトリ
  - **chat.py**：Gemini との基本的な単発 Q&A
  - **streaming.py**：リアルタイムストリーミングによるインタラクティブなマルチターン会話
  - **vision.py**：Gemini を使用した画像解析のビジョン機能
  - **models.py**：異なる Gemini モデルの利用可能性をテストするユーティリティ
- **examples/**：実行可能なサンプルスクリプト
- **tests/**：テストファイルとテスト用コンテキスト
- **docs/**：ドキュメントとガイド
  - **quickstart.md**：基本的な使い方のクイックスタートガイド
  - **adc-guide-with-diagrams.md**：ADC 認証の詳細解説（図解付き）
  - **images/**：ドキュメント用の画像ファイル（PNG）
  - **diagrams/**：図の編集可能なソースファイル（Excalidraw）

すべてのモジュールは共通パターンを共有します：

- python-dotenv を使用した環境変数検証
- より良い UX のための Rich コンソールフォーマット
- 一貫した Vertex AI クライアント初期化
- 日本語サポートによる包括的なエラーハンドリング

## 設定

`.env` に必要な環境変数：

- `GCP_PROJECT_ID`：Google Cloud プロジェクト ID
- `GEMINI_MODEL`：モデル名（例：gemini-1.5-flash, gemini-1.5-pro）

オプション：

- `GCP_LOCATION`：デフォルトは us-central1

## 主要な依存関係

- **google-cloud-aiplatform**：コア Vertex AI SDK
- **python-dotenv**：環境管理
- **rich**：拡張ターミナル出力
- **uv**：パッケージマネージャー（pip/poetry の代替）

## 開発ノート

- モダンな Python 依存関係管理に uv を使用
- 全体を通じて日本語 UI とドキュメント
- テキストとマルチモーダル（ビジョン）機能の両方をサポート
- すべての例に適切な認証チェックと役立つエラーメッセージが含まれる

## 開発ガイドライン

### コア開発ルール

1. **パッケージ管理**
   - uv のみ使用、pip は絶対禁止
   - インストール：`uv add package`
   - ツール実行：`uv run tool`
   - アップグレード：`uv add --dev package --upgrade-package package`
   - 禁止：`uv pip install`、`@latest` 構文

2. **コード品質**
   - すべてのコードに型ヒント必須
   - パブリック API には docstring 必須
   - 関数は焦点を絞り、小さく保つ
   - 既存のパターンに厳密に従う
   - 行の長さ：最大 88 文字

3. **テスト要件**
   - フレームワーク：`uv run --frozen pytest`
   - 非同期テスト：anyio を使用（asyncio ではない）
   - カバレッジ：エッジケースとエラーをテスト
   - 新機能にはテスト必須
   - バグ修正には回帰テスト必須

### Python ツール

#### コードフォーマット

1. **Ruff**
   - フォーマット：`uv run --frozen ruff format .`
   - チェック：`uv run --frozen ruff check .`
   - 修正：`uv run --frozen ruff check . --fix`
   - 重要な問題：
     - 行の長さ（88 文字）
     - インポート順序（I001）
     - 未使用インポート
   - 行の折り返し：
     - 文字列：括弧を使用
     - 関数呼び出し：適切なインデントで複数行
     - インポート：複数行に分割

2. **型チェック**
   - ツール：`uv run --frozen pyright`
   - 要件：
     - Optional の明示的な None チェック
     - 文字列の型絞り込み
     - チェックが通れば、バージョン警告は無視可能

3. **Pre-commit**
   - 設定：`.pre-commit-config.yaml`
   - 実行：git commit 時
   - ツール：Prettier（YAML/JSON）、Ruff（Python）

#### エラー解決

1. **CI 失敗**
   - 修正順序：
     1. フォーマット
     2. 型エラー
     3. リンティング

2. **よくある問題**
   - 行の長さ：括弧で文字列を分割、複数行の関数呼び出し、インポートの分割
   - 型：None チェック追加、文字列型の絞り込み、既存パターンに合わせる
   - Pytest：anyio pytest マークが見つからない場合、コマンドの前に `PYTEST_DISABLE_PLUGIN_AUTOLOAD=""` を追加

### Git とコミット

- バグ修正や機能追加のコミット時：
  ```bash
  git commit --trailer "Reported-by:<name>"
  ```
- GitHub Issue 関連のコミット時：
  ```bash
  git commit --trailer "Github-Issue:#<number>"
  ```
- `co-authored-by` や使用ツールの言及は絶対禁止

### プルリクエスト

- 変更内容の詳細な説明を作成
- 解決しようとする問題の高レベルな説明と解決方法に焦点
- コードの詳細は明確さを追加する場合のみ記載
- レビュアーに `jerome3o-anthropic` と `jspahrsummers` を追加
- ツールの言及や `co-authored-by` は絶対禁止