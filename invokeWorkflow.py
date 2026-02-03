# Microsoft Foundry Workflow呼び出し（Foundry SDK使用）
# 実行前に: pip install --pre azure-ai-projects>=2.0.0b1
from azure.identity import DefaultAzureCredential
from azure.ai.projects import AIProjectClient
from azure.ai.projects.models import ResponseStreamEventType

# プロジェクト設定
PROJECT_ENDPOINT = "https://foundry-junwoo.services.ai.azure.com/api/projects/proj-default"
WORKFLOW_NAME = "Sequential-Workflow"
WORKFLOW_VERSION = "1"  # 異なるバージョンの場合は更新してください

# AI Projectクライアントを作成
project_client = AIProjectClient(
    endpoint=PROJECT_ENDPOINT,
    credential=DefaultAzureCredential(),
)

with project_client:
    workflow = {
        "name": WORKFLOW_NAME,
        "version": WORKFLOW_VERSION,
    }
    
    # プロジェクトからOpenAIクライアントを取得
    openai_client = project_client.get_openai_client()

    # 会話を作成
    conversation = openai_client.conversations.create()
    print(f"会話を作成しました (id: {conversation.id})")

    # ストリーミングでワークフローを呼び出し
    print(f"\nワークフロー呼び出し中: {WORKFLOW_NAME}...\n")
    stream = openai_client.responses.create(
        conversation=conversation.id,
        extra_body={"agent": {"name": workflow["name"], "type": "agent_reference"}},
        input="東京2泊3日の旅行スケジュールを作成してください",
        stream=True,
        metadata={"x-ms-debug-mode-enabled": "1"},
    )

    # ストリーミングイベントを処理
    for event in stream:
        if event.type == ResponseStreamEventType.RESPONSE_OUTPUT_TEXT_DONE:
            print("\t", event.text)
        elif event.type == ResponseStreamEventType.RESPONSE_OUTPUT_ITEM_ADDED and event.item.type == "workflow_action":
            print(f"********************************\nアクター - '{event.item.action_id}' :")
        elif event.type == ResponseStreamEventType.RESPONSE_OUTPUT_ITEM_DONE and event.item.type == "workflow_action":
            print(f"ワークフローアイテム '{event.item.action_id}' は '{event.item.status}' です - (前のアイテム: '{event.item.previous_action_id}')")
        elif event.type == ResponseStreamEventType.RESPONSE_OUTPUT_TEXT_DELTA:
            print(event.delta, end="", flush=True)

    # クリーンアップ
    print("\n\n✅ ワークフローが完了しました！")
    openai_client.conversations.delete(conversation_id=conversation.id)
    print("会話を削除しました")
