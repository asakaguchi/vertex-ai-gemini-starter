"""
Vertex AI で利用可能な Gemini モデルを確認する

このスクリプトは、あなたのプロジェクトとリージョンで
利用可能な Gemini モデルの一覧を表示します。
"""

import os
import sys

import vertexai
from dotenv import load_dotenv
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from vertexai.generative_models import GenerativeModel

load_dotenv()
console = Console()


def check_models():
    """利用可能な Gemini モデルをチェックする"""
    # 設定を環境変数から取得
    project_id = os.getenv("GCP_PROJECT_ID")
    location = os.getenv("GCP_LOCATION", "us-central1")

    # 必須設定のチェック
    if not project_id:
        console.print("[red]エラー: GCP_PROJECT_ID が設定されていません。[/red]")
        console.print(".env ファイルに以下を追加してください。")
        console.print("[dim]GCP_PROJECT_ID=your-project-id[/dim]\n")
        sys.exit(1)

    console.print(f"[cyan]プロジェクト: {project_id}[/cyan]")
    console.print(f"[cyan]リージョン: {location}[/cyan]\n")

    # Vertex AI を初期化
    vertexai.init(project=project_id, location=location)

    # テストするモデルのリスト（最新版を優先、エイリアス含む）
    models_to_test = [
        # Gemini 2.5 系（最新プレビュー）
        "gemini-2.5-pro-preview-06-05",
        "gemini-2.5-pro-preview-05-06", 
        "gemini-2.5-flash-preview-05-20",
        "gemini-2.5-flash-preview-04-17",
        
        # Gemini 2.0 系（安定版とエイリアス）
        "gemini-2.0-flash",  # alias for gemini-2.0-flash-001
        "gemini-2.0-flash-lite",  # alias for gemini-2.0-flash-lite-001
        "gemini-2.0-flash-preview-image-generation",
        
        # Gemini 1.5 系（安定版とエイリアス）
        "gemini-1.5-pro",  # alias for gemini-1.5-pro-002
        "gemini-1.5-flash",  # alias for gemini-1.5-flash-002
        "gemini-1.5-flash-8b",  # alias for gemini-1.5-flash-8b-001
        
        # Gemma 3 系
        "gemma-3-27b-it",
        "gemma-3-12b-it",
        "gemma-3-4b-it",
        "gemma-3-1b-it",
        "gemma-3n-e4b-it",
    ]

    # 結果テーブルを作成
    table = Table(title="Gemini モデル可用性チェック")
    table.add_column("モデル名", style="cyan")
    table.add_column("ステータス", style="bold")
    table.add_column("備考", style="dim")

    available_models = []
    
    for model_name in models_to_test:
        try:
            # モデルをインスタンス化してテスト
            model = GenerativeModel(model_name)
            # 簡単なテストクエリを送信
            response = model.generate_content("Hello")
            
            if response and response.text:
                table.add_row(model_name, "[green]利用可能[/green]", "正常に応答")
                available_models.append(model_name)
            else:
                table.add_row(model_name, "[yellow]応答なし[/yellow]", "レスポンスが空")
                
        except Exception as e:
            error_msg = str(e)
            if "404" in error_msg or "not found" in error_msg.lower():
                table.add_row(model_name, "[red]利用不可[/red]", "モデルが見つかりません")
            elif "permission" in error_msg.lower() or "forbidden" in error_msg.lower():
                table.add_row(model_name, "[yellow]権限不足[/yellow]", "アクセス権限がありません")
            else:
                table.add_row(model_name, "[red]エラー[/red]", "その他のエラー")

    # 結果を表示
    console.print(table)
    
    if available_models:
        console.print(f"\n[green]✅ 利用可能なモデル: {len(available_models)}個[/green]")
        
        # おすすめモデルを表示
        recommended_model = None
        if "gemini-2.5-pro-preview-05-06" in available_models:
            recommended_model = "gemini-2.5-pro-preview-05-06"
            recommendation_text = "gemini-2.5-pro-preview-05-06 (最新・最高性能)"
        elif "gemini-2.5-flash-preview-05-20" in available_models:
            recommended_model = "gemini-2.5-flash-preview-05-20"
            recommendation_text = "gemini-2.5-flash-preview-05-20 (最新・高速)"
        elif "gemini-2.0-flash" in available_models:
            recommended_model = "gemini-2.0-flash"
            recommendation_text = "gemini-2.0-flash (安定版・高速)"
        elif "gemini-1.5-flash" in available_models:
            recommended_model = "gemini-1.5-flash"
            recommendation_text = "gemini-1.5-flash (安定版・コスト効率良)"
        elif "gemini-1.5-pro" in available_models:
            recommended_model = "gemini-1.5-pro"
            recommendation_text = "gemini-1.5-pro (安定版・高性能)"
            
        if recommended_model:
            console.print("\n[yellow]💡 おすすめモデル:[/yellow]")
            console.print(f"  • {recommendation_text}")
                
            console.print(f"\n[blue]💾 .env ファイルに設定例:[/blue]")
            console.print(f"[dim]GEMINI_MODEL={recommended_model}[/dim]")
        else:
            console.print(f"\n[blue]💾 .env ファイルに設定例:[/blue]")
            console.print(f"[dim]GEMINI_MODEL={available_models[0]}[/dim]")
        
    else:
        console.print("\n[red]❌ 利用可能なモデルが見つかりませんでした[/red]")
        console.print("\n[yellow]確認事項:[/yellow]")
        console.print("• Vertex AI API が有効になっているか")
        console.print("• 正しいプロジェクト ID が設定されているか")
        console.print("• 認証が正しく設定されているか")


def main():
    """メイン処理"""
    console.print(Panel.fit(
        "Vertex AI Gemini モデル可用性チェック",
        style="bold blue"
    ))
    
    try:
        check_models()
    except KeyboardInterrupt:
        console.print("\n\n[yellow]中断されました[/yellow]")
    except Exception as e:
        console.print(f"\n[red]予期しないエラーが発生しました: {e}[/red]")


if __name__ == "__main__":
    main()