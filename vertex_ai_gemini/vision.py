"""
Vertex AI Gemini API で画像を解析する
"""
import os
import sys
import argparse
from dotenv import load_dotenv
import vertexai
from vertexai.generative_models import GenerativeModel, Part
from rich.console import Console
from rich.panel import Panel

load_dotenv()
console = Console()

def analyze_image(image_uri: str, prompt: str = None):
    """画像を解析する.
    
    Args:
        image_uri (str): Cloud Storageの画像URI (例: gs://bucket/image.jpg)
        prompt (str, optional): カスタムプロンプト. 
                               省略時はデフォルトプロンプトを使用.
    
    Returns:
        None: 結果は標準出力に表示される.
    """
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
        console.print("画像解析には以下のモデルがおすすめです。")
        console.print("- gemini-1.5-pro-002（高精度）")
        console.print("- gemini-1.5-flash-002（高速）")
        console.print("- gemini-2.0-flash-001（最新版）\n")
        console.print("利用可能なモデルを確認するには：")
        console.print("[cyan]python -m vertex_ai_gemini.models[/cyan]\n")
        sys.exit(1)
    
    # Vertex AI を初期化
    console.print(f"[dim]使用モデル: {model_name}[/dim]")
    vertexai.init(project=project_id, location=location)
    model = GenerativeModel(model_name)
    
    # デフォルトのプロンプト
    if prompt is None:
        prompt = "この画像に何が写っていますか？詳しく説明してください。"
    
    console.print(f"[cyan]画像URI: {image_uri}[/cyan]")
    console.print(Panel(prompt, title="質問", border_style="blue"))
    
    try:
        # 画像とプロンプトを準備
        image_part = Part.from_uri(image_uri, mime_type="image/jpeg")
        
        # 画像解析を実行
        response = model.generate_content([image_part, prompt])
        
        console.print("\n[green]Gemini の分析結果:[/green]")
        console.print(Panel(response.text, border_style="green"))
        
    except Exception as e:
        console.print(f"\n[red]エラーが発生しました: {e}[/red]")
        console.print("[yellow]ヒント:[/yellow]")
        console.print("- 画像は Cloud Storage にアップロードされている必要があります")
        console.print("- サービスアカウントに「ストレージ オブジェクト閲覧者」権限が必要です")


def main():
    """メイン処理"""
    parser = argparse.ArgumentParser(description="画像を Gemini で解析します")
    parser.add_argument(
        "--image-uri",
        required=True,
        help="Cloud Storage の画像URI (例: gs://bucket/image.jpg)"
    )
    parser.add_argument(
        "--prompt",
        help="カスタムプロンプト（省略時はデフォルトを使用）"
    )
    
    args = parser.parse_args()
    analyze_image(args.image_uri, args.prompt)

if __name__ == "__main__":
    main()