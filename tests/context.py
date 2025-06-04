"""
テスト用のコンテキスト設定

このファイルは、テストファイルからパッケージを
正しくインポートするためのヘルパーです。
"""

import os
import sys

# プロジェクトルートをパスに追加
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import vertex_ai_gemini