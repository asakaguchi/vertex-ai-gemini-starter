"""
利用可能な Gemini モデルを確認する
"""
import os
from dotenv import load_dotenv
import vertexai
from vertexai.generative_models import GenerativeModel
from rich.console import Console
from rich.table import Table
from rich.panel import Panel

load_dotenv()
console = Console()

def check_models():
    """利用可能なGeminiモデルをテストする.
    
    定義済みのモデルリストに対して実際に問い合わせを送信し、
    各モデルの可用性を確認してテーブル形式で結果を表示する.
    
    Returns:
        None: 結果は標準出力に表示される.
    """
    # 設定を環境変数から取得
    project_id = os.getenv("GCP_PROJECT_ID")
    location = os.getenv("GCP_LOCATION", "us-central1")
    
    if not project_id:
        console.print("[red]エラー: GCP_PROJECT_ID が設定されていません。[/red]")
        return
    
    # Vertex AI を初期化
    console.print(f"[cyan]プロジェクト: {project_id}[/cyan]")
    console.print(f"[cyan]リージョン: {location}[/cyan]\n")
    
    vertexai.init(project=project_id, location=location)
    
    # テストするモデル一覧 (2025年6月時点)
    test_models = [
        "gemini-2.5-pro-preview-05-06",
        "gemini-2.5-flash-preview-04-17",
        "gemini-2.5-flash-preview-05-20",
        "gemini-2.0-flash-001",
        "gemini-2.0-flash-preview-image-generation",
        "gemini-2.0-flash-lite-001",
        "gemini-1.5-pro-002",
        "gemini-1.5-flash-002",
        "gemini-1.5-flash-8b-001",
    ]
    
    # 結果を格納
    results = []
    
    console.print("[yellow]モデルの利用可能性をチェック中...[/yellow]\n")
    
    test_prompt = "Hello, please respond with 'OK' if you're working."
    
    for model_name in test_models:
        console.print(f"テスト中: {model_name}... ", end="")
        try:
            model = GenerativeModel(model_name)
            response = model.generate_content(test_prompt)
            if response.text:
                console.print("[green]✓ 利用可能[/green]")
                results.append((model_name, "✓ 利用可能", "green"))
            else:
                console.print("[yellow]? 応答なし[/yellow]")
                results.append((model_name, "? 応答なし", "yellow"))
        except Exception as e:
            # エラーメッセージの最初の行のみ
            error_msg = str(e).split('\n')[0]
            if "404" in error_msg:
                console.print("[red]✗ 利用不可[/red]")
                results.append((model_name, "✗ 利用不可", "red"))
            else:
                console.print(f"[yellow]! エラー[/yellow]")
                results.append((model_name, f"! {error_msg[:30]}...", "yellow"))
    
    # 結果をテーブルで表示
    console.print("\n")
    table = Table(title="モデル利用可能性チェック結果")
    table.add_column("モデル名", style="cyan")
    table.add_column("状態", style="white")
    
    for model_name, status, color in results:
        table.add_row(model_name, f"[{color}]{status}[/{color}]")
    
    console.print(table)
    
    # 利用可能なモデルだけをリストアップ
    available_models = [m[0] for m in results if "✓" in m[1]]
    if available_models:
        console.print("\n[green]利用可能なモデル:[/green]")
        for model in available_models:
            console.print(f"  • {model}")
        
        console.print(f"\n[dim]これらのモデル名を .env ファイルの GEMINI_MODEL に設定できます。[/dim]")
    else:
        console.print("\n[red]利用可能なモデルが見つかりませんでした。[/red]")
        console.print("[yellow]プロジェクトの設定や権限を確認してください。[/yellow]")


def main():
    """メイン処理"""
    check_models()

if __name__ == "__main__":
    main()
