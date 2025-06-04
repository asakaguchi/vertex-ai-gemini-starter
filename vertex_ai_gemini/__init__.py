"""
Vertex AI Gemini API スターターキット

このパッケージは、Vertex AI経由でGemini APIを使用するための
基本的な機能を提供します。

Modules:
    chat: シンプルなテキスト生成
    streaming: ストリーミングチャット機能
    vision: 画像解析機能
    models: モデル可用性チェック
"""

__version__ = "0.1.0"
__author__ = "vertex-ai-gemini-starter contributors"

from .chat import main as simple_chat
from .streaming import streaming_chat
from .vision import analyze_image
from .models import check_models

__all__ = [
    "simple_chat",
    "streaming_chat",
    "analyze_image",
    "check_models",
]