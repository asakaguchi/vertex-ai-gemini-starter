# CLAUDE.md

このファイルは、このリポジトリでコードを扱う際のClaude Code (claude.ai/code) へのガイダンスを提供します。

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

プロジェクトはThe Hitchhiker's Guide to Pythonの推奨構造に従います：

- **vertex_ai_gemini/**: メインパッケージディレクトリ
  - **chat.py**: Gemini との基本的な単発 Q&A
  - **streaming.py**: リアルタイムストリーミングによるインタラクティブなマルチターン会話
  - **vision.py**: Gemini を使用した画像解析のビジョン機能
  - **models.py**: 異なる Gemini モデルの利用可能性をテストするユーティリティ
- **examples/**: 実行可能なサンプルスクリプト
- **tests/**: テストファイルとテスト用コンテキスト
- **docs/**: ドキュメントとガイド
  - **quickstart.md**: 基本的な使い方のクイックスタートガイド
  - **adc-guide-with-diagrams.md**: ADC認証の詳細解説（図解付き）
  - **images/**: ドキュメント用の画像ファイル（PNG）
  - **diagrams/**: 図の編集可能なソースファイル（Excalidraw）

すべてのモジュールは共通パターンを共有します：

- python-dotenv を使用した環境変数検証
- より良い UX のための Rich コンソールフォーマット
- 一貫した Vertex AI クライアント初期化
- 日本語サポートによる包括的なエラーハンドリング

## 設定

`.env`に必要な環境変数：

- `GCP_PROJECT_ID`: Google Cloud プロジェクト ID
- `GEMINI_MODEL`: モデル名（例：gemini-1.5-flash, gemini-1.5-pro）

オプション：

- `GCP_LOCATION`: デフォルトは us-central1

## 主要な依存関係

- **google-cloud-aiplatform**: コア Vertex AI SDK
- **python-dotenv**: 環境管理
- **rich**: 拡張ターミナル出力
- **uv**: パッケージマネージャー（pip/poetry の代替）

## 開発ノート

- モダンな Python 依存関係管理に uv を使用
- 全体を通じて日本語 UI とドキュメント
- テキストとマルチモーダル（ビジョン）機能の両方をサポート
- すべての例に適切な認証チェックと役立つエラーメッセージが含まれる