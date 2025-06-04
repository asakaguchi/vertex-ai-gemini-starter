"""
Vertex AI Gemini API の基本的な使い方
"""
import os
from dotenv import load_dotenv
import vertexai
from vertexai.generative_models import GenerativeModel
from rich.console import Console
from rich.panel import Panel

# 環境変数を読み込み
load_dotenv()

# きれいな出力のためのコンソール
console = Console()

def main():
    """メイン処理"""
    # 設定を環境変数から取得
    project_id = os.getenv("GCP_PROJECT_ID")
    location = os.getenv("GCP_LOCATION", "us-central1")
    model_name = os.getenv("GEMINI_MODEL", "gemini-1.5-flash-001")
    
    if not project_id:
        console.print("[red]エラー: GCP_PROJECT_ID が設定されていません。[/red]")
        console.print(".env ファイルを確認してください。")
        return
    
    # Vertex AI を初期化
    console.print(f"[cyan]プロジェクト: {project_id}[/cyan]")
    console.print(f"[cyan]リージョン: {location}[/cyan]")
    console.print(f"[cyan]モデル: {model_name}[/cyan]\n")
    
    vertexai.init(project=project_id, location=location)
    model = GenerativeModel(model_name)
    
    # Gemini に質問
    prompt = "こんにちは！Pythonプログラミングの楽しさを3つ教えてください。"
    console.print(Panel(prompt, title="質問", border_style="blue"))
    
    try:
        response = model.generate_content(prompt)
        console.print("\n[green]Gemini の回答:[/green]")
        console.print(Panel(response.text, border_style="green"))
    except Exception as e:
        console.print(f"\n[red]エラーが発生しました: {e}[/red]")

if __name__ == "__main__":
    main()
