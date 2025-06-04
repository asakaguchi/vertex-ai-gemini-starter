# CLAUDE.md

このファイルは、このリポジトリでコードを扱う際のClaude Code (claude.ai/code) へのガイダンスを提供します。

## プロジェクト概要

これはVertex AI Gemini APIスターターキットで、Vertex AIを通じてGoogleのGemini AIモデルを統合するための実用的な例を提供します。テキスト生成、ストリーミングチャット、画像解析、モデルテストユーティリティが含まれています。

## 必須コマンド

```bash
# 環境設定
cp .env.example .env
uv sync

# 認証（すべての例を実行する前に必要）
gcloud auth application-default login

# 必要なGoogle Cloud APIを有効化
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

プロジェクトはThe Hitchhiker's Guide to Pythonの推奨構造に従います：

- **vertex_ai_gemini/**: メインパッケージディレクトリ
  - **chat.py**: Geminiとの基本的な単発Q&A
  - **streaming.py**: リアルタイムストリーミングによるインタラクティブなマルチターン会話
  - **vision.py**: Geminiを使用した画像解析のビジョン機能
  - **models.py**: 異なるGeminiモデルの利用可能性をテストするユーティリティ
- **examples/**: 実行可能なサンプルスクリプト
- **tests/**: テストファイルとテスト用コンテキスト

すべてのモジュールは共通パターンを共有します：

- python-dotenvを使用した環境変数検証
- より良いUXのためのRichコンソールフォーマット
- 一貫したVertex AIクライアント初期化
- 日本語サポートによる包括的なエラーハンドリング

## 設定

`.env`に必要な環境変数：

- `GCP_PROJECT_ID`: Google CloudプロジェクトID
- `GEMINI_MODEL`: モデル名（例：gemini-1.5-flash, gemini-1.5-pro）

オプション：

- `GCP_LOCATION`: デフォルトはus-central1

## 主要な依存関係

- **google-cloud-aiplatform**: コアVertex AI SDK
- **python-dotenv**: 環境管理
- **rich**: 拡張ターミナル出力
- **uv**: パッケージマネージャー（pip/poetryの代替）

## 開発ノート

- モダンなPython依存関係管理にuvを使用
- 全体を通じて日本語UIとドキュメント
- テキストとマルチモーダル（ビジョン）機能の両方をサポート
- すべての例に適切な認証チェックと役立つエラーメッセージが含まれる