# 05. ワークフロー

このモジュールでは、複数のエージェントを組み合わせて複雑なタスクを実行するワークフローを構築する方法を学習します。

## 📋 目次

- [ワークフロー概要](#ワークフロー概要)
- [Sequential Workflow](#sequential-workflow)
- [Group Chat Workflow](#group-chat-workflow)
- [Human-in-loop Workflow](#human-in-loop-workflow)
- [次のステップ](#次のステップ)

## 🎯 学習目標

- Microsoft Foundryワークフローのコア概念を理解
- Sequential Workflowを通じた順次的なタスクフローの構築
- Group Chat Workflowを通じたマルチエージェント協調の実装
- Human-in-loopパターンを通じた人間の介入ポイントの設定
- ワークフローのデプロイとプログラマティック呼び出し

## ⏱️ 予想所要時間

約20分

---

## ワークフロー概要

### ワークフローとは？

ワークフローは複数のAIエージェントを調整して複雑なタスクを段階的に実行する自動化システムです。

### ワークフロータイプ

```
Single Agent → Sequential Workflow → Group Chat → Human-in-loop
(シンプル)                                                    (複雑)
```

| タイプ | 説明 | ユースケース |
|------|------|-----------|
| **Sequential** | 順次実行 | データパイプライン、ドキュメント処理 |
| **Parallel** | 並列実行 | 同時分析、複数検索 |
| **Group Chat** | エージェント間対話 | 協調問題解決、意思決定 |
| **Human-in-loop** | 人間の介入 | 承認プロセス、検証 |
| **Conditional** | 条件分岐 | 動的ルーティング、エラー処理 |

### ワークフローの構成要素

```python
Workflow {
    Agents: [Agent1, Agent2, Agent3]
    Flow: Sequential | Parallel | Conditional
    Inputs: User request, Context
    Outputs: Final result, Intermediate results
    Handoffs: Agent transitions
    Termination: Completion condition
}
```

---

## Sequential Workflow

順次実行されるエージェントチェーンを構築します。旅行計画作成ワークフローを例として使用します。

### 必要なエージェントの作成

まずワークフローで使用するエージェントを作成します。

#### 1. TravelPlannerAgent

```
Agent name: TravelPlannerAgent
Description: 旅行目的地と日程を企画するエージェント
Model: gpt-5.1

Instructions:
あなたは旅行計画の専門家です。

役割：
1. ユーザーの旅行要件を分析します
2. 目的地の主要観光スポット、グルメ、宿泊施設を推薦します
3. 日程別の旅行スケジュールを具体的に作成します
4. 予想費用と準備物を提示します

出力形式：
- 目的地概要
- 日程別スケジュール（朝/昼/夜の活動）
- おすすめ宿泊施設
- 予想費用
- 準備物リスト

次のエージェントに渡す情報: 全体の旅行計画
```

#### 2. LocalAgent

```
Agent name: LocalAgent
Description: 現地情報を追加するエージェント
Model: gpt-5.1

Tools: Web search (有効化)

Instructions:
あなたは現地情報の専門家です。

役割：
1. 前のエージェントの旅行計画を受け取ります
2. Web searchを使用して最新の現地情報を検索します
3. リアルタイム情報を追加します：
   - 現在の天気と気候
   - 現地のフェスティバルとイベント
   - 交通情報（路線、料金、所要時間）
   - 営業時間と予約情報
   - 現地文化と注意事項

出力形式：
- 元のスケジュール + 現地情報補強
- 交通手段の詳細情報
- 予約が必要な場所のリスト
- 現地のヒント

次のエージェントに渡す情報: 現地情報が追加された旅行計画
```

#### 3. TravelSummaryAgent

```
Agent name: TravelSummaryAgent
Description: 旅行計画を要約し最終チェックリストを作成するエージェント
Model: gpt-5.1

Instructions:
あなたは旅行計画整理の専門家です。

役割：
1. 前のエージェントの情報を総合します
2. 実行可能な最終計画に整理します
3. チェックリストを生成します

出力形式：
�� 旅行概要
- 目的地: 
- 期間:
- 予算:

📅 スケジュール概要（一目で見るスケジュール）

✅ 出発前チェックリスト
- [ ] 項目1
- [ ] 項目2

🎒 準備物チェックリスト

📞 緊急連絡先と便利な情報

最終出力: 印刷可能な旅行ガイド
```

### Sequential Workflowの作成

1. **Workflowsセクションへ移動**

   - Foundryポータル右上メニューで**Build**を選択します。
   - **Workflows**メニューをクリックします。
   
   ![Build > Workflowsメニュー](../assets/05-01-workflows-menu.png)

2. **新しいワークフローの作成**

   - **+ Create workflow**または**New workflow**ボタンをクリックします。
   - **Sequential Workflow**を選択します。
   
   ![Create workflowボタン](../assets/05-02-create-workflow.png)

   ![Create workflowボタン2](../assets/05-02-create-workflow-2.png)

3. **エージェントの追加**

   順番にエージェントを追加します：
   
   ![Select an agent to invokeボタン](../assets/05-04-workflow-add-agent.png)

   ```
   Step 1: TravelPlannerAgent
     ↓
   Step 2: LocalAgent
     ↓
   Step 3: TravelSummaryAgent
   ```

   - 各ステップで**Select an agent to invoke**ボタンをクリックしてエージェントを選択します。

   ![Select an agent to invokeボタン1](../assets/05-04-workflow-add-agent1.png)
   
   ![Select an agent to invokeボタン2](../assets/05-04-workflow-add-agent2.png)

   ![Select an agent to invokeボタン3](../assets/05-04-workflow-add-agent3.png)

   ![全体workflow](../assets/05-02-overall-workflow.png)

4. **ワークフローの保存**

   - **Save**ボタンをクリックします。

   ![Workflow名登録](../assets/05-02-workflow-save.png)

   ![Workflow名保存](../assets/05-02-workflow-saved.png)

### ワークフローのテスト

1. **Previewモード**

   - **Preview**ボタンをクリックします。

2. **テスト質問**

   ```
   ユーザー: 東京2泊3日の旅行計画を立てるのを手伝ってください。
   ```

3. **実行プロセスの観察**

   各ステップでの出力を確認します：

   - **Step 1 (TravelPlannerAgent)**: 基本旅行スケジュールの生成
   - **Step 2 (LocalAgent)**: 現地情報の追加（天気、交通、イベント）
   - **Step 3 (TravelSummaryAgent)**: 最終要約とチェックリスト

   ![Workflow Preview](../assets/05-05-workflow-preview.png)

4. **Tracesの確認**

   - 各エージェントの実行時間
   - エージェント間のデータ転送
   - 最終出力生成プロセス

### ワークフローのデプロイと呼び出し

1. **Publish**

   - **Publish**ボタンをクリックします。

   ![Workflow Publish-1](../assets/05-05-workflow-publish1.png)

   - バージョンを確認して公開します。

   ![Workflow Publish-2](../assets/05-05-workflow-publish2.png)

   ![Workflow Publish-3](../assets/05-05-workflow-publish3.png)

2. **Python SDKでの呼び出し**

   > 💡 **実習のヒント**: 以下のコードは参考用です。実際の実習時にはこのリポジトリのルートパスにある`invokeWorkflow.py`ファイルを開いて`PROJECT_ENDPOINT`と`WORKFLOW_NAME`の値を自分の環境に合わせて修正してから実行してください。

   `invokeWorkflow.py`ファイル例：

   ```python
   # Microsoft Foundry Workflow Invocation using Foundry SDK
   # Before running: pip install --pre azure-ai-projects>=2.0.0b1
   from azure.identity import DefaultAzureCredential
   from azure.ai.projects import AIProjectClient
   from azure.ai.projects.models import ResponseStreamEventType
   
   # Project configuration
   PROJECT_ENDPOINT = "https://<foundry-resource-name>.services.ai.azure.com/api/projects/proj-default"
   WORKFLOW_NAME = "Sequential-Workflow"
   WORKFLOW_VERSION = "1"  # 公開されたバージョンに更新
   
   # Create AI Project client
   project_client = AIProjectClient(
       endpoint=PROJECT_ENDPOINT,
       credential=DefaultAzureCredential(),
   )
   
   with project_client:
       workflow = {
           "name": WORKFLOW_NAME,
           "version": WORKFLOW_VERSION,
       }
       
       # Get OpenAI client from project
       openai_client = project_client.get_openai_client()

       # Create a conversation
       conversation = openai_client.conversations.create()
       print(f"Created conversation (id: {conversation.id})")

       # Call the workflow with streaming
       print(f"\nCalling workflow: {WORKFLOW_NAME}...\n")
       stream = openai_client.responses.create(
           conversation=conversation.id,
           extra_body={"agent": {"name": workflow["name"], "type": "agent_reference"}},
           input="東京2泊3日の旅行スケジュールを作成してください",
           stream=True,
           metadata={"x-ms-debug-mode-enabled": "1"},
       )

       # Process streaming events
       for event in stream:
           if event.type == ResponseStreamEventType.RESPONSE_OUTPUT_TEXT_DONE:
               print("\t", event.text)
           elif event.type == ResponseStreamEventType.RESPONSE_OUTPUT_ITEM_ADDED and event.item.type == "workflow_action":
               print(f"\n{'='*60}")
               print(f"Actor - '{event.item.action_id}':")
               print(f"{'='*60}")
           elif event.type == ResponseStreamEventType.RESPONSE_OUTPUT_ITEM_DONE and event.item.type == "workflow_action":
               print(f"\n✓ Workflow Item '{event.item.action_id}' is '{event.item.status}'")
               print(f"  (previous item was: '{event.item.previous_action_id}')")
           elif event.type == ResponseStreamEventType.RESPONSE_OUTPUT_TEXT_DELTA:
               print(event.delta, end="", flush=True)

       # Clean up
       print("\n\n✅ Workflow completed!")
       openai_client.conversations.delete(conversation_id=conversation.id)
       print("Conversation deleted")
   ```

3. **実行**

   ```bash
   pip install --pre azure-ai-projects>=2.0.0b1
   python invokeWorkflow.py
   ```

### ✅ 確認事項

- すべてのエージェントが順番に実行されることを確認
- 各エージェントの出力が次のエージェントに渡されることを確認
- 最終出力が正しく生成されることを確認

---

## Group Chat Workflow

複数のエージェントが対話を通じて協調して問題を解決するワークフローです。


### 必要なエージェントの作成

#### 1. StudentAgent

```
Agent name: StudentAgent
Description: 質問に回答する学生役
Model: gpt-5.1

Instructions:
あなたは質問に回答するエージェントです。質問が来たら常に回答してください。

役割：
1. ユーザーの質問を理解して回答を生成します
2. 最初の試みでは基本的な回答を提供します
3. TeacherAgentのフィードバックを受けて回答を改善します
4. すべての要件が満たされるまで回答を修正します

回答時の考慮事項：
- スケジュール（日付、時間）
- コスト（予算、価格）
- 好み（嗜好、スタイル）
- 制約事項（制限事項、条件）

改善が必要な場合はTeacherAgentのフィードバックを反映して回答を補完します。
```

#### 2. TeacherAgent

```
Agent name: TeacherAgent
Description: 回答を評価し改善を要求する教師役
Model: gpt-5.1

Instructions:
あなたは回答を評価するエージェントです。回答がスケジュール、コスト、好みなど様々な条件を考慮していれば[COMPLETE]と回答してください。そうでなければ、COMPLETEを表示せずに修正を要求してください。

評価基準：
1. スケジュール：具体的な日付、時間、期間が含まれているか？
2. コスト：予算、価格、費用情報が含まれているか？
3. 好み：ユーザーの嗜好やスタイルを考慮したか？
4. 実用性：実際に実行可能な計画か？
5. 完成度：すべての必要な情報が含まれているか？

応答形式：
評価完了時: "[COMPLETE] すべての条件が満たされました。"
改善が必要な場合: "以下の事項を補完してください: [具体的なフィードバック]"

重要: [COMPLETE]はすべての基準が満たされた場合のみ使用します。
```

### Group Chat Workflowの作成

1. **新しいワークフローの作成**

   - Workflowsセクションで**+ Create workflow**ボタンをクリックします。
   - **Group Chat Workflow**を選択します。
   
   ![Group Chat Workflow作成](../assets/05-09-group-chat-create.png)


2. **エージェントの追加**

   ```
   Participants:
   - StudentAgent
   - TeacherAgent
   
   Termination condition: TeacherAgentが[COMPLETE]を応答した時
   Max turns: 4 (無限ループ防止)
   ```

   ![複数エージェントの追加](../assets/05-10-group-chat-agents.png)

3. **対話フローの設定**

   ```
   User → StudentAgent → TeacherAgent → StudentAgent → ...
   ```

   - StudentAgentが最初に回答を提供
   - TeacherAgentが評価とフィードバック
   - [COMPLETE]が出るまで繰り返し

5. **ワークフローの保存**

   - **Save**ボタンをクリックします。
   
   ![Group Chat Workflow保存](../assets/05-09-group-chat-save.png)
      
   ![Group Chat Workflow保存完了](../assets/05-09-group-chat-saved.png)

### ワークフローのテスト

1. **Previewモード**

   - **Preview**ボタンをクリックします。

   ![Group Chat Workflow Preview](../assets/05-09-group-chat-preview.png)

2. **テスト質問**

   ```
   ユーザー: 東京2泊3日の旅行スケジュールを作成してください。
   ```

3. **対話フローの観察**

   ```
   Turn 1:
   StudentAgent: "東京のおすすめスケジュールです。1日目: 浅草寺..."
   
   Turn 2:
   TeacherAgent: "コスト情報が欠けています。予算を含めてください。"
   
   Turn 3:
   StudentAgent: "修正されたスケジュールです。総予算5万円... 1日目: 浅草寺 (入場料無料)..."
   
   Turn 4:
   TeacherAgent: "具体的な時間帯がありません。時間別のスケジュールを追加してください。"
   
   Turn 5:
   StudentAgent: "最終スケジュールです。1日目 午前9時: 浅草寺..."
   
   Turn 6:
   TeacherAgent: "[COMPLETE] すべての条件が満たされました。"
   ```

### 💡 Group Chat活用のヒント

- **役割分担**: 各エージェントに明確な役割を付与
- **終了条件**: 無限ループを防止するための明確な終了条件
- **最大ターン数**: 安全装置として最大ターン数を設定
- **フィードバックの具体性**: TeacherAgentのフィードバックが具体的であるほど改善効果が向上

### ✅ 確認事項

- エージェント間の対話が自然に続くことを確認
- TeacherAgentの評価基準が適切かを確認
- [COMPLETE]条件でワークフローが終了することを確認

---

## Human-in-loop Workflow

人間の承認や入力が必要なポイントでワークフローを一時停止するパターンです。


### コンセプト

```
Agent 1 → [Human Approval] → Agent 2 → [Human Input] → Agent 3
```

Human-in-loopは以下の状況で有用です：
- 重要な決定の承認
- 機密情報の検証
- 予算承認
- 個人の好みの入力

### ワークフロー設計

1. **エージェント構成**

   以前作成したSequential Workflowをベースにします：

   ```
   TravelPlannerAgent → [ユーザー承認] → LocalAgent → TravelSummaryAgent
   ```

2. **Human Approval Pointの追加**

   - TravelPlannerAgentの後に**Human approval**ステップを追加します。
   - ユーザーは初期の旅行計画をレビューして：
     - ✅ 承認 → LocalAgentへ進行
     - ❌ 拒否 → TravelPlannerAgentに戻って再生成
     - 📝 修正要求 → フィードバックと共に再生成

3. **ワークフロー設定**

   ```
   Workflow name: Human-in-loop-Workflow
   Description: ユーザー承認を含む旅行計画ワークフロー
   
   Steps:
   1. TravelPlannerAgent (初稿作成)
   2. Human Approval (ユーザーレビュー)
   3. LocalAgent (承認時に現地情報追加)
   4. TravelSummaryAgent (最終要約)
   ```

4. **Approval設定**

   ```
   Approval message: "生成された旅行計画をレビューしてください。承認しますか？"
   
   Options:
   - Approve: 次のステップへ進行
   - Reject: TravelPlannerAgentに戻る
   - Modify: 修正リクエスト入力を受付
   
   Timeout: 24時間 (応答がなければ自動拒否)
   ```

### テストシナリオ

1. **承認シナリオ**

   ```
   ユーザー: こんにちは
   TravelPlannerAgent: 旅行スケジュール初稿を生成
   [System]: ユーザー承認待機...
   ユーザー: 承認
   LocalAgent: 現地情報を追加
   TravelSummaryAgent: 最終要約
   ```

2. **拒否と再生成シナリオ**

   ```
   ユーザー: 東京旅行の計画を立ててください
   TravelPlannerAgent: 初稿を生成（ホテル中心）
   [System]: ユーザー承認待機...
   ユーザー: 拒否。ゲストハウスに変更してください
   TravelPlannerAgent: 修正された計画を生成（ゲストハウス中心）
   [System]: ユーザー承認待機...
   ユーザー: 承認
   LocalAgent: 現地情報を追加
   TravelSummaryAgent: 最終要約
   ```

   ![Human-in-Loop Workflow Preview](../assets/05-10-human-in-loop-workflow-preview.png)

### 💡 Human-in-loopのベストプラクティス

```
✅ 推奨事項：
- 承認ポイントを明確に表示
- タイムアウト設定で無限待機を防止
- ユーザーにコンテキストを提供（以前の対話要約）
- シンプルな承認オプションを提供（はい/いいえ/修正）

❌ 避けるべきこと：
- 承認ポイントが多すぎる
- 不明確な承認質問
- 長いタイムアウト（ユーザー体験低下）
- 承認後に戻れない構造
```

### ✅ 確認事項

- 承認ポイントでワークフローが正しく停止することを確認
- 承認/拒否に応じて適切に分岐することを確認
- タイムアウトが正常に動作することを確認

---

## 📚 追加リソース

- [Microsoft Foundry Workflows概要](https://learn.microsoft.com/en-us/azure/ai-foundry/agents/concepts/workflow?view=foundry)
- [Microsoft Agent Framework Workflows Orchestrationsパターン](https://learn.microsoft.com/en-us/agent-framework/user-guide/workflows/orchestrations/overview)

## 次のステップ

複雑なワークフローを構築しました！次はエージェントとワークフローのパフォーマンスを評価する方法を学習します：

➡️ **[06. 評価](./06-evaluations.md)**: エージェントとワークフローの品質を体系的に評価します。

---

[← 前へ: Foundry IQ](./04-foundry-iq.md) | [メインへ](./README.md) | [次へ: 評価 →](./06-evaluations.md)
