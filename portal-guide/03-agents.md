# 03. エージェント開発

このモジュールでは、各種機能を持つAIエージェントを作成しデプロイする方法を学習します。

## 📋 目次

- [エージェント概要](#エージェント概要)
- [ModelRouterAgentの作成](#modelrouteragentの作成)
- [FileSearchAgentの作成](#filesearchagentの作成)
- [WebSearchAgentの作成](#websearchagentの作成)
- [エージェントのデプロイと呼び出し](#エージェントのデプロイと呼び出し)
- [次のステップ](#次のステップ)

## 🎯 学習目標

- Microsoft Foundryエージェントのコア概念を理解
- Model Routerベースのエージェント構築
- File Search機能を活用したドキュメントベースのエージェント作成
- Web Search機能を活用したリアルタイム情報検索エージェント作成
- エージェントのデプロイとプログラマティック呼び出し方法の学習

## ⏱️ 予想所要時間

約30分

---

## エージェント概要

### Microsoft Foundry Agentとは？

AI Agentはユーザーのリクエストを理解し、必要なツールを活用してタスクを実行するインテリジェントシステムです。

### 主要構成要素

```
Agent = Model + Instructions + Tools + Knowledge
```

- **Model**: 基本言語モデル（GPT-5.1、Claudeなど）
- **Instructions**: エージェントの行動指針とペルソナ
- **Tools**: File Search、Web Search、Function Callingなど
- **Knowledge**: 接続されたナレッジベース（Foundry IQ）

### エージェントタイプ

| タイプ | 説明 | ユースケース |
|------|------|-----------|
| **Conversational** | 対話型エージェント | チャットボット、カスタマーサポート |
| **Task-oriented** | タスク中心エージェント | データ分析、ドキュメント生成 |
| **Retrieval-augmented** | 検索ベースエージェント | ナレッジベースQA |
| **Multi-agent** | マルチエージェント協調 | 複雑なワークフロー |

---

## ModelRouterAgentの作成

Model Routerを活用してインテリジェントにモデルを選択するエージェントを作成します。

### ステップバイステップガイド

1. **Agentsセクションへ移動**
   - Foundryポータル右上メニューで**Build**を選択します。
   - **Agents**メニューをクリックします。
   
   ![Build > Agents メニュー](../assets/03-01-agents-menu.png)

2. **新しいエージェントの作成**
   - **+ Create agent**または**New agent**ボタンをクリックします。
   
   ![Create agentボタン](../assets/03-02-create-agent.png)

3. **Playgroundでの構成**
   ```
   Agent name: ModelRouterAgent
   Model: model-router (以前にデプロイしたModel Router)
   ```

   **Instructions設定**：
   ```
   あなたは質問に回答するエージェントです。
   リクエストの複雑さと要件に応じて最も適切なモデルを使用してください。
   常に明確で正確、かつ役立つ回答を提供してください。
   ```
   
   **Save**ボタンをクリックして保存します。

   ![エージェント基本設定](../assets/03-03-agent-basic-settings.png)

4. **エージェントのテスト**

   **Chatタブで以下の質問をテストしてみます：**

   ```
   ユーザー: こんにちは
   ```
   → シンプルな挨拶なので軽量モデルを使用

   ```
   ユーザー: あなたはいつまでのデータで学習されていますか？
   ```
   → モデル情報の質問、基本モデルで回答

   ```
   ユーザー: microsoft foundry new portalの実習ガイドを作成してください。
   foundry models、model-router、foundry agents、foundry tools、foundry knowledge、
   foundry control planeなどすべてをfoundry portalで実習するガイドが必要です
   ```
   → 複雑なドキュメント生成リクエストなので高性能モデルを使用
   
   ![Chatタブでのテスト](../assets/03-05-agent-chat-test.png)

5. **追加タブの探索**

   **YAMLタブ**：
   - エージェント設定をYAML形式で確認
   - Infrastructure as Codeで管理可能
   
   ![YAMLタブ画面](../assets/03-06-agent-yaml.png)
   
   **Codeタブ**：
   - エージェントをコードで呼び出すサンプルを確認
   - Python、JavaScript、C#など各種言語をサポート
   
   ![Codeタブ画面](../assets/03-07-agent-code.png)

   **Tracesタブ**：
   - エージェント実行過程のトレーシング
   - モデル選択の決定を確認
   - パフォーマンスとコストの分析

   **Tracingの有効化**には**App Insightsの作成と接続**が必要です。
   **Agent Tracing**はFoundry(New)の**Sweden Central**でのみ可能です。
   
   ![Tracesタブ画面 - Connect](../assets/03-08-agent-traces-connect.png)

   ![Tracesタブ画面 - Create](../assets/03-08-agent-traces-create.png)

   ![Tracesタブ画面 - Traces](../assets/03-08-agent-traces.png)

   ![Tracesタブ画面 - Traces - Details](../assets/03-08-agent-traces-details.png)

   **Monitorタブ**：
   - リアルタイムメトリクスモニタリング
   - エラー率、レスポンス時間などを確認
   
   ![Monitorタブ画面](../assets/03-09-agent-monitor.png)

6. **エージェントの保存**
   - **Save**ボタンをクリックしてエージェントを保存します。

### ✅ 確認事項

- ModelRouterAgentがAgentsリストに表示されることを確認
- 様々な複雑度の質問に適切に応答するかテスト
- Tracesでどのモデルが選択されたかを確認

---

## FileSearchAgentの作成

ファイル検索機能を活用してアップロードされたドキュメントから情報を検索するエージェントを作成します。

### ステップバイステップガイド

1. **新しいエージェントの作成**
   ```
   Agent name: FileSearchAgent
   Model: gpt-5.1
   ```

2. **Instructions設定**

   Playgroundの**Instructions**セクションに以下を入力：
   ```
   あなたはToolsに登録されたFile searchに基づいて回答するエージェントです。
   
   重要ルール：
   1. 必ずアップロードされたファイルの内容に基づいてのみ回答してください
   2. ファイルにない情報は「提供されたドキュメントで該当情報が見つかりません」と回答してください
   3. 回答時にソースファイル名を記載してください
   4. 正確な引用を使用してください
   ```
   
   **Save**ボタンをクリックして保存します。

   ![FileSearchAgent作成](../assets/03-10-filesearch-create.png)

3. **File Search Toolの追加**

   - **Tools**セクションで**+ Add**ボタンをクリックします。
   
   - **File Search**オプションを選択します。
   - File SearchがToolsリストに追加されたことを確認します。
   
   ![File Search ツール選択](../assets/03-13-filesearch-tool-selection.png)

4. **ファイルのアップロード**

   - **Tools > File Search**セクションで**Attach files**ボタンをクリックします。
   
   ![Attach filesボタン](../assets/03-14-filesearch-attach-files.png)
   
   - `knowledge-base.json`ファイルをアップロードします。
   - ファイルが正常にアップロードされたことを確認します。
   
   ![ファイルアップロード完了](../assets/03-15-filesearch-file-uploaded.png)

5. **エージェントの保存**
   - **Save**ボタンをクリックします。

6. **エージェントのテスト**

   **Chatタブで以下の質問を試してみます：**

   ```
   ユーザー: サーフィンにおすすめの場所を教えてください
   ```
   期待される回答: 陽陽サーフビーチと済州中文色達海辺を推奨

   ```
   ユーザー: ヒーリングに良い海辺を探してください
   ```
   期待される回答: 江陵鏡浦海辺と泰安万里浦海辺の紹介

   ```
   ユーザー: 四季可能なサーフィン場所は？
   ```
   期待される回答: 済州中文色達海辺
   
   ![FileSearchAgentテスト](../assets/03-16-filesearch-chat-test.png)

7. **Tracesの確認**

   - **Traces**タブでFile Searchがどのように動作したかを確認します。
   - 検索されたドキュメントチャンクと関連性スコアを確認できます。
   
   ![File Search Traces確認](../assets/03-17-filesearch-traces.png)

   ![File Search Traces確認](../assets/03-17-filesearch-traces-2.png)

### ✅ 確認事項

- File Search toolが有効化されていることを確認
- アップロードされたファイルの内容に基づいて正確に回答するかテスト
- ファイルにない情報については知らないと回答するか確認

---

## WebSearchAgentの作成

リアルタイムWeb検索を実行して最新情報を提供するエージェントを作成します。

### ステップバイステップガイド

1. **新しいエージェントの作成**
   ```
   Agent name: WebSearchAgent
   Model: gpt-4.1
   ```
   
   **Instructions設定**

   ```
   あなたはToolsに登録されたWeb searchに基づいて回答するエージェントです。
   
   重要ルール：
   1. 最新情報が必要な質問には必ずWeb検索を使用してください
   2. 検索結果に基づいて正確で最新の情報を提供してください
   3. 回答時にソースURLを含めてください
   4. 複数のソースの情報を総合してバランスの取れた回答を提供してください
   5. 検索結果が不十分な場合は追加検索を実行してください
   ```
   
   ![WebSearchAgent作成](../assets/03-18-websearch-create.png)

2. **Web Search Toolの追加**

   - **Tools**セクションで**+ Add**ボタンをクリックします。
   - **Web search**オプションを選択します。
   - Web Searchが有効化されたことを確認します。
   
   ![Web searchツール追加](../assets/03-20-websearch-add-tool.png)

3. **エージェントの保存**
   - **Save**ボタンをクリックします。

4. **エージェントのテスト**

   **Chatタブで最新情報の質問をテストします：**

   ```
   ユーザー: Microsoft Ignite 2025で発表されたMicrosoft Foundryの主要な新機能を要約してください
   ```
   → Web検索を通じて最新発表内容を検索し要約

   ```
   ユーザー: Foundry IQについてもっと詳しく教えてください
   ```
   → Foundry IQの最新機能と特徴を説明

   ```
   ユーザー: 従来通りAzure AI Searchを使用することと比較してどのような点が改善されますか？
   ```
   → 比較分析と利点の説明
   
   ![WebSearchAgentテスト](../assets/03-21-websearch-chat-test.png)

5. **Traces分析**

   - **Traces**タブでWeb検索プロセスを確認：
     - 検索クエリ
     - 検索されたWebサイトリスト
     - 抽出された情報
     - 最終レスポンス生成プロセス
   
   ![Web Search Traces確認](../assets/03-22-websearch-traces.png)

   ![Web Search Traces確認](../assets/03-22-websearch-traces-2.png)

### 💡 Web Search活用のヒント

- **具体的な質問**: 明確な検索結果のために質問を具体的に
- **最新情報**: ニュース、イベント、技術発表などに有用
- **比較分析**: 複数のソースの情報を総合してバランスの取れた回答を提供
- **ソース確認**: 回答の信頼性のためにソースURLを確認

### ✅ 確認事項

- Web Search toolが有効化されていることを確認
- 最新情報を正確に検索し要約するかテスト
- ソースURLがレスポンスに含まれているか確認

---

## エージェントのデプロイと呼び出し

作成したエージェントをデプロイし、外部から呼び出す方法を学習します。

### Publish（公開）

1. **Previewステージ**

   - Playgroundで**Preview**ボタンをクリックします。
   - 以下のオプションを確認できます：
     - **Preview agent**: Webインターフェースでエージェントをプレビュー
     - **View sample app code**: サンプルアプリケーションコードを確認
   
   ![Previewボタン](../assets/03-23-agent-preview-button.png)

   ![Preview](../assets/03-23-agent-preview.png)

2. **Publishの実行**

   - **Publish agent**ボタンをクリックします。
   
   ![Publish agentボタンクリック](../assets/03-24-agent-publish-agent.png)

   - **Publish**ボタンをクリックします。
   
   ![Publishボタンクリック](../assets/03-24-agent-publish.png)
   
   - 公開設定の確認：
     ```
     Version: 1.0
     Status: Published
     Endpoint: [自動生成されたエンドポイント]
     ```
   
   ![公開完了確認](../assets/03-25-agent-published.png)

### エージェントの呼び出し

#### 1. Azure CLIログイン

まずAzureにログインします：

```bash
az login 
```

マルチテナントを使用する場合、テナントIDを指定します。
```bash
az login --tenant <tenant-id>
```

#### 2. Python SDKを使用した呼び出し

> 💡 **実習のヒント**: 以下のコードは参考用です。実際の実習時にはこのリポジトリのルートパスにある`invokeAgent.py`ファイルを開いて`FOUNDRY_ENDPOINT`と`AGENT_NAME`の値を自分の環境に合わせて修正してから実行してください。

`invokeAgent.py`ファイル例：

```python
# Microsoft Foundry Agent Invocation using Activity Protocol
from openai import OpenAI
from azure.identity import DefaultAzureCredential, get_bearer_token_provider

# TODO: Update these values with your actual Microsoft Foundry details
# Get these from: https://ai.azure.com → Your Project → Deployments
FOUNDRY_ENDPOINT = "https://<foundry-resource-name>.services.ai.azure.com/api/projects/<project-name>"
AGENT_NAME = "ModelRouterAgent"  # 呼び出すエージェント名
API_VERSION = "2025-11-15-preview"

# Create OpenAI client with Azure authentication
client = OpenAI(
    api_key=get_bearer_token_provider(
        DefaultAzureCredential(), 
        "https://ai.azure.com/.default"
    ),
    base_url=f"{FOUNDRY_ENDPOINT}/applications/{AGENT_NAME}/protocols/openai",
    default_query={"api-version": API_VERSION}
)

try:
    # Call the agent using responses API
    response = client.responses.create(
        input="東京2泊3日の旅行コースを推薦してください"
    )
    
    print(f"Response: {response.output_text}")
    
except Exception as e:
    print(f"Error: {e}")
    print("\n🔍 Troubleshooting:")
    print("1. Check your endpoint URL at https://ai.azure.com")
    print("2. Verify the project name and agent name exist")
    print("3. Ensure you're logged in: az login")
    print("4. Confirm the agent is deployed and running")
```

#### 3. エンドポイント情報の確認

Foundryポータルでエンドポイント情報を確認する方法：

1. Build > Agentsで公開されたエージェントを選択
2. **Publish**ボタンをクリック後、**View details**をクリック
3. 以下の情報をコピー：
   - Agent application
   - Activity Protocol endpoint
   - Response API endpoint

![Endpoint情報確認](../assets/03-26-agent-endpoint.png)

#### 4. 実行

```bash
# 仮想環境の作成（オプション）
python -m venv .venv
source .venv/bin/activate  # Windows: venv\Scripts\activate

# 必要なパッケージのインストール（pre-releaseバージョン含む）
pip install openai azure-identity
pip install --pre azure-ai-projects

# スクリプトの実行
python invokeAgent.py
```

### 🔐 認証オプション

#### Option 1: DefaultAzureCredential（推奨）
```python
from azure.identity import DefaultAzureCredential
credential = DefaultAzureCredential()
```

#### Option 2: Managed Identity（Azureリソースで実行時）
```python
from azure.identity import ManagedIdentityCredential
credential = ManagedIdentityCredential()
```

#### Option 3: Service Principal
```python
from azure.identity import ClientSecretCredential
credential = ClientSecretCredential(
    tenant_id="YOUR_TENANT_ID",
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET"
)
```

### ✅ 確認事項

- エージェントが正常に公開されたことを確認
- Pythonスクリプトがエラーなく実行されることを確認
- レスポンスが期待通りに返されることを確認

---

## 📚 追加リソース

- [Microsoft Foundry Agents概要](https://learn.microsoft.com/en-us/azure/ai-foundry/agents/overview?view=foundry)
- [Agent SDKドキュメント](https://learn.microsoft.com/en-us/azure/ai-foundry/how-to/develop/sdk-overview?view=foundry&pivots=programming-language-python)
- [File Searchガイド](https://learn.microsoft.com/en-us/azure/ai-foundry/agents/how-to/tools/file-search?view=foundry&pivots=python)
- [Web Search統合](https://learn.microsoft.com/en-us/azure/ai-foundry/agents/how-to/tools/web-search?view=foundry&pivots=python)

---

## 次のステップ

各種エージェントを作成しました！次はFoundry IQを使用して高度なナレッジベースを構築しましょう：

➡️ **[04. Foundry IQ](./04-foundry-iq.md)**: AI SearchとBlob Storageを活用したナレッジベース構築を学習します。

---

[← 前へ: モデルとデプロイ](./02-models.md) | [メインへ](./README.md) | [次へ: Foundry IQ →](./04-foundry-iq.md)
