# Microsoft Foundry Agent呼び出し（Activity Protocol使用）
from openai import OpenAI
from azure.identity import DefaultAzureCredential, get_bearer_token_provider

# TODO: 実際のMicrosoft Foundry情報でこれらの値を更新してください
# 取得先: https://ai.azure.com → Your Project → Deployments
FOUNDRY_ENDPOINT = "https://foundry-junwoo.services.ai.azure.com/api/projects/proj-default"
AGENT_NAME = "ModelRouterAgent"
API_VERSION = "2025-11-15-preview"

# Azure認証を使用してOpenAIクライアントを作成
client = OpenAI(
    api_key=get_bearer_token_provider(
        DefaultAzureCredential(), 
        "https://ai.azure.com/.default"
    ),
    base_url=f"{FOUNDRY_ENDPOINT}/applications/{AGENT_NAME}/protocols/openai",
    default_query={"api-version": API_VERSION}
)

try:
    # responses APIを使用してエージェントを呼び出し
    response = client.responses.create(
        input="東京2泊3日の旅行コースを推薦してください"
    )
    
    print(f"Response: {response.output_text}")
    
except Exception as e:
    print(f"Error: {e}")
    print("\n�� トラブルシューティング:")
    print("1. https://ai.azure.com でエンドポイントURLを確認してください")
    print("2. プロジェクト名とエージェント名が存在することを確認してください")
    print("3. ログインしていることを確認してください: az login")
    print("4. エージェントがデプロイされて実行中であることを確認してください")

