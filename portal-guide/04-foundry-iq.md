# 04. Foundry IQ

このモジュールでは、Microsoft Foundry IQを活用して高度なナレッジベースを構築し、エージェントと統合する方法を学習します。

## 📋 目次

- [Foundry IQ概要](#foundry-iq概要)
- [AI Searchの接続](#ai-searchの接続)
- [Knowledge Baseの作成 (AI Search Index)](#knowledge-baseの作成-ai-search-index)
- [Knowledge Baseの作成 (Blob Storage)](#knowledge-baseの作成-blob-storage)
- [KnowledgeAgentの統合](#knowledgeagentの統合)
- [次のステップ](#次のステップ)

## 🎯 学習目標

- Foundry IQの概念とメリットを理解
- Azure AI Searchリソースの接続と構成
- AI Search IndexベースのKnowledge Base作成
- Blob StorageベースのKnowledge Base
- Knowledge Baseをエージェントに統合する方法の学習

## ⏱️ 予想所要時間

約40分

---

## Foundry IQ概要

### Foundry IQとは？

Foundry IQはMicrosoft Foundryのインテリジェントナレッジ管理システムで、様々なデータソースを統合してAIエージェントにコンテキスト情報を提供します。

### 主な特徴

```
Foundry IQ = Retrieval + Reasoning + Ranking
```

- **Retrieval**: 関連情報を効率的に検索
- **Reasoning**: 検索された情報を理解し解釈
- **Ranking**: 最も関連性の高い情報を優先順位付け

### 従来のRAG vs Foundry IQ

| 特徴 | 従来のRAG (Azure AI Search) | Foundry IQ |
|------|---------------------------|------------|
| **設定の複雑さ** | 高い（手動設定が必要） | 低い（自動化された設定） |
| **ベクトルインデックス** | 手動設定 | 自動管理 |
| **Chunking戦略** | 手動実装 | 最適化されたデフォルト提供 |
| **Retrieval最適化** | 直接チューニング | AIベースの自動最適化 |
| **複数ソース統合** | 複雑な実装 | 簡単な統合 |
| **Semantic Ranking** | 別途設定 | デフォルト含む |

### サポートされるデータソース

- **Azure AI Search Index**: 既存インデックスの再利用
- **Azure Blob Storage**: ドキュメントの自動インデックス
- **Azure Data Lake Storage Gen2**: 大容量データ処理
- **SharePoint**: エンタープライズドキュメント連携
- **OneDrive**: 個人およびビジネスドキュメント

---

## AI Searchの接続

Foundry IQを使用するには、まずAzure AI Searchリソースを接続する必要があります。

### Azure AI Searchリソースの作成

1. **Search Serviceの作成**

   - Foundryポータルで**Foundry IQ**セクションに移動します。
   
   ![Foundry IQセクション](../assets/04-01-foundry-iq-menu.png)
   
   - **Connect to an AI Search resource to get started**メッセージが表示されます。
   
   ![Connect to AI Search resourceメッセージ](../assets/04-02-foundry-iq-connect.png)
   
   - **Create new resource**ボタンをクリックします。

2. **Search Serviceの設定**

   Azure PortalのSearch Service作成ページに移動します：

   ```
   Resource group: foundry
   Service name: foundry<Your unique name>
   Location: Sweden Central
   Pricing tier: Basic
   ```
   
   ![Search Service作成設定](../assets/04-04-ai-search-settings.png)

   **Pricing Tier選択ガイド**：
   - **Free**: テスト用、50MB、3インデックス（サブスクリプションごとに1つのみ可能）
   - **Basic**: 開発/小規模、160GB、15インデックス
   - **Standard**: プロダクション、512GB+、50インデックス
   - **Storage Optimized**: 大容量データ、2TB+
   
   ![Pricing tier選択画面](../assets/04-05-ai-search-pricing-tiers.png)

3. **コンピュート設定**

   ```
   Compute type: Default
   Replicas: 1 (開発用)
   Partitions: 1 (開発用)
   ```

4. **作成完了**

   - **Review + create**をクリックします。
   - 検証後、**Create**ボタンをクリックします。
   - 作成には約3-5分かかります。

### Managed Identityの有効化

AI SearchがFoundryリソースにアクセスできるようにManaged Identityを設定します。

1. **AI Searchリソースの設定**

   - Azure Portalで作成したSearch Serviceを開きます。
   - 左側メニューで**Settings > Identity**を選択します。
   
   ![Managed Identity設定](../assets/04-06-ai-search-identity.png)

2. **System Assigned Identityの有効化**

   ```
   Status: On
   ```

   - **Save**ボタンをクリックします。
   - Object IDが生成されたことを確認します。

   ![Managed Identity有効化](../assets/04-06-ai-search-identity-enable.png)

### FoundryにAI Searchを接続

1. **Foundry IQに戻る**

   - Foundryポータルの**Foundry IQ**セクションに戻ります。

2. **Search Resourceの選択**

   - **Select a resource**または**Connect**ボタンをクリックします。
   - ドロップダウンから作成したSearch Serviceを選択します。

   ![AI Search接続](../assets/04-07-foundry-iq-connect.png)

3. **接続完了**

   - **Connect**ボタンをクリックします。
   - 接続が成功するとFoundry IQダッシュボードが有効化されます。
   
   ![AI Search接続完了](../assets/04-07-foundry-iq-connected.png)

### ✅ 確認事項

- AI Searchリソースが作成され「Running」状態であることを確認
- Managed Identityが有効化されていることを確認
- Foundry IQに接続が完了していることを確認

---

## Knowledge Baseの作成 (AI Search Index)

既存のAI Search Indexを使用してKnowledge Baseを作成します。

### Storage AccountとContainerの作成

1. **Storage Accountの作成**

   - Azure Portalで**Storage accounts**を検索します。

   ![Storage Accounts](../assets/04-08-storage-account.png)

   - **+ Create**ボタンをクリックします。
   
   ![Storage Account作成ボタン](../assets/04-08-storage-create-button.png)

   ```
   Resource group: foundry
   Storage account name: foundry<Your unique name>
   Region: Sweden Central
   Preferred storage type: Azure Blob Storage
   Primary workload: Cloud native
   Performance: Standard
   Redundancy: Locally-redundant storage (LRS)
   ```
   ![Storage Account作成](../assets/04-08-storage-create.png)

   - **Review + create** > **Create**をクリックします。

2. **Containerの作成**

   - 作成されたStorage Accountを開きます。
   - 左側メニューで**Containers**を選択します。
   - **+ Container**ボタンをクリックします。
   
   ![Containerボタン](../assets/04-09-container-button.png)

   - **+Add container**ボタンをクリックします。

   ```
   Name: foundry
   Public access level: Private
   ```

   ![Add containerボタン](../assets/04-09-add-container-button.png)

   - **Create**をクリックします。

   ![Container作成](../assets/04-09-container-create.png)

### IAM権限の設定

Storage AccountとAI Search間の権限を設定します。

1. **Storage Blob Data Contributor - ユーザーアカウント**

   - 作成したStorage Accountに移動します。

   ![Storage Account](../assets/04-10-storage-account.png)

   - **Access Control (IAM)** > **+ Add** > **Add role assignment**をクリックします。

   ![Storage Account IAMメニュー Add role assignment](../assets/04-11-storage-iam-add-role-assignment.png)

   ```
   Role: Storage Blob Data Contributor
   Assign access to: User, group, or service principal
   Members: [自分のEntra IDアカウントを選択]
   ```

   - **Storage Blob Data Contributor**を検索して選択し、「Next」ボタンをクリックします。

   ![Storage Account IAMメニュー Role選択](../assets/04-11-storage-iam-role-select.png)

   - **+Select members**をクリックし、自分のEntra IDアカウントを検索して選択し、「Select」ボタンをクリックします。

   ![Storage Account IAMメニュー Members選択](../assets/04-11-storage-iam-member-select.png)

   - **Review + assign**をクリックします。
   
   ![Storage Blob Data Contributorロール割り当て（ユーザー）](../assets/04-12-storage-role-user.png)

2. **Storage Blob Data Contributor - Search Service**

   - 同様に再度**Add role assignment**をクリックします。

   ```
   Role: Storage Blob Data Contributor
   Assign access to: Managed identity
   Members:
     - Subscription: [使用中のサブスクリプション]
     - Managed identity: Search service
     - Select: foundry<Your unique name>
   ```

   - **Storage Blob Data Contributor**を検索して選択し、「Next」ボタンをクリックします。
   - **Assign access to**でManaged identityを選択します。
   - **+Select members**をクリックし、使用中のサブスクリプション、Search service、Search service nameを選択し、「Select」ボタンをクリックします。

   ![Storage Blob Data Contributorロール割り当て（Search Service）- Managed Identity](../assets/04-13-storage-role-search-managed-identity.png)

   - **Review + assign**をクリックします。
   
   ![Storage Blob Data Contributorロール割り当て（Search Service）](../assets/04-13-storage-role-search.png)

   ![Storage Blob Data Contributorロール割り当て（Search Service）](../assets/04-13-storage-role-search-2.png)


Microsoft FoundryとAI Search間の権限を設定します。

1. **Azure AI Project Managerロールの割り当て**

   - **Microsoft Foundry**に移動します。

   ![Foundry](../assets/04-14-foundry.png)

   - **Microsoft Foundry**リソースに移動します。

   ![Foundryリソース](../assets/04-14-foundry-resource.png)

   - 作成した**Foundryリソース**をクリックし、**Access Control (IAM)**をクリックします。

   ![Foundryリソースクリック](../assets/04-14-foundry-resource-click.png)

   - **Access Control (IAM)** > **+ Add** > **Add role assignment**

   - **Azure AI Project Manager**を検索して選択し、「Next」ボタンをクリックします。

   ![Foundryリソース IAM](../assets/04-14-foundry-iam.png)

   - **Assign access to**でManaged identityを選択します。
   - **+Select members**をクリックし、使用中のサブスクリプション、Search service、Search service nameを選択し、「Select」ボタンをクリックします。

   ```
   Role: Azure AI Project Manager
   Assign access to: Managed identity
   Members:
     - Subscription: [使用中のサブスクリプション]
     - Managed identity: Search service
     - Select: foundry<Your unique name>
   ```

   ![Foundryリソース IAM](../assets/04-14-foundry-iam-2.png)

   - **Review + assign**をクリックします。
   
   ![Azure AI Project Managerロール割り当て](../assets/04-15-foundry-role-search.png)

   ![Azure AI Project Managerロール割り当て](../assets/04-15-foundry-role-search-2.png)


### **サンプルデータのアップロード**

   Microsoftが提供するサンプルデータをダウンロードします：

   [サンプルデータリンク](https://github.com/Azure-Samples/azure-search-sample-data/tree/main/health-plan)

   上記リンクから以下のPDFファイルをダウンロードしてContainerにアップロードします：
   - `Benefit_Options.pdf`
   - `employee_handbook.pdf`
   - `Northwind_Health_Plus_Benefits_Details.pdf`
   - `Northwind_Standard_Benefits_Details.pdf`
   - `PerksPlus.pdf`
   - `role_library.pdf`
   
   ![サンプルデータアップロード](../assets/04-10-container-upload.png)

   ![サンプルデータアップロード](../assets/04-10-container-upload-2.png)


### Import Data Wizardの実行

1. **AI SearchでImport Wizardを開始**

   - Azure Portalで作成したAI Searchを開きます。
   - **Import data (new)**ボタンをクリックします。
   
   ![Import data (new)ボタン](../assets/04-16-import-data-button.png)

2. **データソースの選択**

   - **Data Source**: Azure Blob Storage
   
   ![Azure Blob Storage選択](../assets/04-17-import-data-source.png)

   - **Scenario**: RAG (Retrieval Augmented Generation)

   ![Scenario選択](../assets/04-17-import-data-source-2.png)

3. **Azure Blob Storageの構成**

   ```
   Subscription: [使用中のサブスクリプション]
   Storage account: foundry<Your unique name>
   Blob container: foundry
   ```

   - **Next**をクリックします。
   
   ![Blob Storage構成](../assets/04-18-import-blob-config.png)

4. **テキストベクトル化設定**

   ```
   Kind: Microsoft Foundry
   Subscription: [使用中のサブスクリプション]
   Foundry project: proj-default
   Model deployment: text-embedding-3-large
   Authentication type: API key
   ```

   - **Check**ボタンをクリックして接続を確認
   - **Next**をクリックします。
   
   ![テキストベクトル化設定](../assets/04-19-import-vectorize-text.png)

5. **画像ベクトル化（オプション）**

   - **Next**をクリックします。

   ![画像ベクトル化](../assets/04-19-image-vectorize.png)

6. **高度なランキング設定**

   ```
   ☑ Enable semantic ranker
   Schedule: Once (初期インデックスのみ)
   ```

   - Semantic Rankerは検索結果の関連性を向上させます。
   
   ![Semantic ranker設定](../assets/04-20-import-semantic-ranker.png)

7. **レビューと作成**

   - **Create**をクリックします。
   - インデックスには5-10分程度かかります。
   
   ![Review and create](../assets/04-21-import-review-create.png)

   ![Review and create](../assets/04-21-import-review-create-2.png)
   
   ![Start Searching](../assets/04-22-start-searching.png)


### Knowledge Baseの作成

1. **Foundry IQに戻る**

   - Foundryポータルの**Foundry IQ**セクションに移動します。

   ![Foundry IQ](../assets/04-23-foundry-iq.png)

2. **Knowledge Baseの作成**

   - **Create a knowledge base**ボタンをクリックします。
   - **Azure AI Search Index**を選択し、**Connect**ボタンをクリックします。

   ![Knowledge Base作成](../assets/04-25-knowledge-base-create.png)

   - **Knowledge source name**のsuffix番号を**100**に変更します。
   - **Select Azure AI Search Index**を選択した後、**Create**ボタンをクリックします。
   
   ![Create knowledge source](../assets/04-23-knowledge-source-create.png)

   ```
   Knowledge base name: knowledgebase100
   Chat completions model: gpt-4.1
   Retrieval reasoning effort: minimal
   ```

   - 作成された**Knowledge source**を確認し、**Save knowledge base**ボタンをクリックします。
   
   ![Knowledge Base設定](../assets/04-24-knowledge-base-settings.png)

   ![Knowledge Base一覧](../assets/04-24-knowledge-base-list.png)

---

## Knowledge Baseの作成 (Blob Storage)

Blob Storageを直接接続して自動インデックスされるKnowledge Baseを作成します。

### ステップバイステップガイド

1. **新しいKnowledge Baseの作成**

   - Foundry IQで**+ Create knowledge base**ボタンをクリックします。

2. **データソースの選択**

   - **Azure Blob Storage**を選択し、**Connect**ボタンを選択します。

   ![Blob Storage直接接続](../assets/04-28-blob-knowledge-create.png)

3. **Knowledge Source設定**

   ```
   Name: ks-azureblob-200
   Storage account: foundry<Your unique name>
   Use managed identity: Yes
   Container name: foundry
   Content extraction mode: minimal
   Embedding model: text-embedding-3-large
   Chat completions model: gpt-4.1
   ```
   
   ![Blob Storage Knowledge Source設定](../assets/04-29-blob-knowledge-settings.png)

4. **Create Knowledge Source**

   - **Create**ボタンをクリックします。
   - FoundryがBlob Storageを自動的にモニタリングしてインデックスします。

5. **Knowledge Baseの作成**

   ```
   Knowledge base name: knowledgebase200
   Description: Auto-indexed employee handbook
   Chat completions model: gpt-4.1
   Retrieval reasoning effort: minimal
   Knowledge sources: ks-azureblob-200
   ```

   - **Save knowledge base**ボタンをクリックします。
   
   ![Blob Storage Knowledge Base作成](../assets/04-30-blob-knowledge-create.png)

   ![Blob Storage Knowledge Base作成完了](../assets/04-30-blob-knowledge-created.png)

   ![Knowledge Baseリスト](../assets/04-30-knowledge-base-list.png)

### Blob Storage方式のメリット

| 特徴 | AI Search Index | Blob Storage Direct |
|------|-----------------|---------------------|
| **設定の複雑さ** | 高い | 低い |
| **自動更新** | 手動再インデックスが必要 | 自動検出とインデックス |
| **カスタマイズ** | 高い（フィールド、スキーマなど） | 低い（自動構成） |
| **パフォーマンス** | 高い（最適化可能） | 中程度 |
| **ユースケース** | 複雑な検索要件 | シンプルなドキュメント検索 |


---

## KnowledgeAgentの統合

作成したKnowledge Baseをエージェントと統合してナレッジベースのレスポンスを提供します。

### KnowledgeAgent (AI Search Index接続)

1. **新しいエージェントの作成**

   - Build > Agentsに移動します。
   - **+ Create agent**ボタンをクリックします。

   ```
   Agent name: KnowledgeAgent
   Model: gpt-5.1
   ```
   
   ![KnowledgeAgent作成](../assets/04-31-knowledge-agent-create.png)

2. **Instructions設定**

   ```
   あなたは接続されたナレッジベースに基づいて回答するエージェントです。
   
   重要ルール：
   1. 必ずKnowledge Baseの情報に基づいて回答してください
   2. 正確な情報を提供し、不確実な場合は明示してください
   3. ドキュメントから直接引用して回答の信頼性を高めてください
   4. Knowledge Baseにない情報は正直に分からないと回答してください
   ```
   
   ![KnowledgeAgent Instructions](../assets/04-32-knowledge-agent-instructions.png)

3. **Knowledgeの接続**

   - **Knowledge**セクションで**Add**ボタンをクリックします。
   - **Connect to Foundry IQ**を選択します。
   
   ![Knowledge接続（Addボタン）](../assets/04-33-knowledge-connect.png)

   ```
   Connection: foundry<Your unique name> (AI Search)
   Knowledge base: knowledgebase100
   ```

   - **Connect**ボタンをクリックします。
   
   ![Knowledge base選択](../assets/04-34-knowledge-select.png)

   - **Save**ボタンをクリックします。

   ![Knowledge base保存](../assets/04-34-knowledge-complete.png)

4. **エージェントのテスト**

   Chatタブで以下の質問をテストします：

   ```
   ユーザー: PerkPlusがカバーする項目を教えてください
   ```
   期待される回答: Health & Wellness、Professional Development、Work-Life Balance、Financial Benefitsの説明

   ```
   ユーザー: カバーされない項目を教えてください
   ```
   期待される回答: 個人旅行費用、個人食事費用などNon-Covered Itemsの説明

   ```
   ユーザー: CPA資格が必要なロールを教えてください
   ```
   期待される回答: Financial Analyst、Controller、Tax Specialistロールの説明
   
   ![KnowledgeAgentテスト](../assets/04-35-knowledge-agent-test.png)


### KnowledgeAgent2 (Blob Storage接続)

同様の方法でBlob StorageベースのKnowledge Baseを使用するエージェントを作成します。

1. **新しいエージェントの作成**

   ```
   Agent name: KnowledgeAgent2
   Model: gpt-5.1
   ```

2. **Instructions設定**

   （上記のKnowledgeAgentと同じInstructionsを使用）

3. **Knowledgeの接続**

   ```
   Connection: foundry<Your unique name> (AI Search)
   Knowledge base: knowledgebase200
   ```

4. **エージェントのテスト**

   同じ質問でテストし、2つのエージェントのレスポンスを比較してみます。

---

## 📚 追加リソース

- [Foundry IQ概要](https://learn.microsoft.com/en-us/azure/ai-foundry/agents/how-to/tools/knowledge-retrieval?view=foundry&tabs=foundry%2Cpython)
- [Azure AI Searchドキュメント](https://learn.microsoft.com/en-us/azure/search/)
- [RAGパターンガイド](https://learn.microsoft.com/en-us/azure/search/retrieval-augmented-generation-overview?tabs=docs)
- [ベクトル検索の最適化](https://learn.microsoft.com/en-us/azure/search/vector-search-overview)

---

## 次のステップ

Knowledge Baseの構築が完了しました！次は複数のエージェントを組み合わせて複雑なワークフローを作成しましょう：

➡️ **[05. ワークフロー](./05-workflows.md)**: Sequential、Group Chat、Human-in-loopワークフローを構築します。

---

[← 前へ: エージェント開発](./03-agents.md) | [メインへ](./README.md) | [次へ: ワークフロー →](./05-workflows.md)
