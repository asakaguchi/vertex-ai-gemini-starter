"""
Vertex AI Gemini API でストリーミングチャット
"""

import os
import sys

import vertexai
from dotenv import load_dotenv
from rich.console import Console
from rich.live import Live
from rich.panel import Panel
from rich.prompt import Prompt
from rich.text import Text
from vertexai.generative_models import GenerativeModel

load_dotenv()
console = Console()


def streaming_chat():
    """ストリーミング対応のチャット"""
    # 設定を環境変数から取得
    project_id = os.getenv("GCP_PROJECT_ID")
    location = os.getenv("GCP_LOCATION", "us-central1")
    model_name = os.getenv("GEMINI_MODEL")

    # 必須設定のチェック
    if not project_id:
        console.print("[red]エラー: GCP_PROJECT_ID が設定されていません。[/red]")
        console.print(".env ファイルに以下を追加してください。")
        console.print("[dim]GCP_PROJECT_ID=your-project-id[/dim]\n")
        sys.exit(1)

    if not model_name:
        console.print("[red]エラー: GEMINI_MODEL が設定されていません。[/red]")
        console.print(".env ファイルに以下を追加してください。")
        console.print("[dim]GEMINI_MODEL=gemini-1.5-flash-002[/dim]\n")
        console.print("利用可能なモデルを確認するには：")
        console.print("[cyan]uv run python src/check_models.py[/cyan]\n")
        sys.exit(1)

    # Vertex AI を初期化
    vertexai.init(project=project_id, location=location)
    model = GenerativeModel(model_name)

    # チャットセッションを開始
    chat = model.start_chat()

    console.print(
        f"[bold cyan]Gemini ({model_name}) とのチャットを開始します[/bold cyan]"
    )
    console.print("終了するには 'exit' または 'quit' と入力してください\n")

    while True:
        # ユーザー入力を取得
        user_input = Prompt.ask("[bold blue]あなた[/bold blue]")

        if user_input.lower() in ["exit", "quit", "終了"]:
            console.print(
                "\n[yellow]チャットを終了します。またお話ししましょう！[/yellow]"
            )
            break

        # ストリーミングで応答を表示
        console.print("\n[bold green]Gemini[/bold green]: ", end="")

        try:
            full_response = ""
            with Live("", refresh_per_second=10, transient=True) as live:
                for chunk in chat.send_message(user_input, stream=True):
                    full_response += chunk.text
                    live.update(Text(full_response))

            # 最終的な応答を表示
            console.print(Panel(full_response, border_style="green"))
            console.print()

        except Exception as e:
            console.print(f"\n[red]エラーが発生しました: {e}[/red]")


def main():
    """メイン処理"""
    try:
        streaming_chat()
    except KeyboardInterrupt:
        console.print("\n\n[yellow]中断されました[/yellow]")


if __name__ == "__main__":
    main()
