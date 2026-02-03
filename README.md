# Microsoft Foundry ハンズオンワークショップ

Microsoft Foundryのコア機能をハンズオンで学ぶワークショップです。このワークショップでは、モデルデプロイ、エージェント作成、ナレッジベース構築、ワークフロー設計など、Foundryの主要機能を段階的に体験できます。

> 🌏 **Language / 言語**: [日本語ガイド](./README.md) | [English Guide](./portal-guide/en/README.md)

## 📓 実習方式の選択

このワークショップは2つの実習方式を提供しています：

### 1️⃣ ポータルベースの実習 ([portal-guide/](./portal-guide/))
- Microsoft Foundry Portalを使用したUIベースの実習
- コード作成不要でポータルから直接設定
- **開始する**: [portal-guide/01-setup.md](./portal-guide/01-setup.md)

### 2️⃣ コードベースの実習 ([code-guide/](./code-guide/))
- Pythonコードでリソースの作成と管理
- 自動化およびスクリプト作成に有用
- **開始する**: [code-guide/01-setup.ipynb](./code-guide/01-setup.ipynb)

> 💡 **推奨**: ポータル実習で概念を学んでから、コード実習で自動化を学習しましょう！

## 📚 ワークショップ概要

このワークショップはMicrosoft Foundryの新しいポータルを使用して以下の内容を扱います：

- **モデル管理**: 各種AIモデルのデプロイおよびModel Router構成
- **エージェント開発**: File Search、Web Search、Knowledgeベースのエージェント構築
- **Foundry IQ**: AI SearchおよびBlob Storageベースのナレッジベース構築
- **ワークフロー**: Sequential、Group Chat、Human-in-loopワークフロー設計
- **評価**: エージェントパフォーマンスの評価と分析
- **管理**: Control Planeを通じた運用モニタリング

## 🎯 前提条件

### 必須要件

- **Microsoft Entra IDアカウント**（旧Azure Active Directory）
- **Azureサブスクリプション**（有効なアカウント）
  - サブスクリプションに対する**所有者（Owner）ロール**が必要
  - リソース作成およびロール割り当て権限が必要
- **GitHubアカウント**
- Azure Portalへのアクセス権限
- テキストエディタまたはIDE（VS Code推奨）
- Python 3.8以上（コード実行実習用）

### 推奨事項

- **GitHub Codespacesの使用を推奨**（ブラウザから直接実習可能）
  - 別途の開発環境設定が不要
  - Python、Azure CLIなどが事前インストール済み
  - 無料使用時間を提供（月120コア時間）
- Azure CLIのインストール（ローカル環境使用時）
- Gitのインストール（ローカル環境使用時）
- 基本的なPythonプログラミング知識
- REST APIおよびJSONの基礎知識

## 📖 ワークショップ構成

各モジュールは独立して実習できるように構成されています：

### 01. 環境設定
**[Portal Guide](./portal-guide/01-setup.md)** | **[Code Guide](./code-guide/01-setup.ipynb)**
- Resource Groupの作成
- Foundryリソースの作成
- New Foundryポータルの有効化

### 02. モデルとデプロイ
**[Portal Guide](./portal-guide/02-models.md)** | **[Code Guide](./code-guide/02-models.ipynb)**
- モデルリーダーボードの探索
- モデルの比較とデプロイ
- Model Routerの構成

### 03. エージェント開発
**[Portal Guide](./portal-guide/03-agents.md)** | **[Code Guide](./code-guide/03-agents.ipynb)**
- ModelRouterAgentの作成
- FileSearchAgentの構築
- WebSearchAgentの構築
- KnowledgeAgentの構築
- エージェントのデプロイと呼び出し

### 04. Foundry IQ
**[Portal Guide](./portal-guide/04-foundry-iq.md)** | **[Code Guide](./code-guide/04-foundry-iq.ipynb)**
- Foundry IQの概要
- AI Searchの接続
- Knowledge Baseの作成（AI Search Index）
- Knowledge Baseの作成（Blob Storage）
- KnowledgeAgentの統合

### 05. ワークフロー
**[Portal Guide](./portal-guide/05-workflows.md)** | **[Code Guide](./code-guide/05-workflows.ipynb)**
- Sequential Workflowの構築
- Group Chat Workflowの構築
- Human-in-loop Workflowの構築

### 06. 評価
**[Portal Guide](./portal-guide/06-evaluations.md)** | **[Code Guide](./code-guide/06-evaluations.ipynb)**
- エージェント評価の設定
- 評価基準の定義
- 評価結果の分析

### 07. Control Plane
**[Portal Guide](./portal-guide/07-control-plane.md)** | **[Code Guide](./code-guide/07-control-plane.ipynb)**
- Fleet Overviewモニタリング
- Assets管理
- Complianceとセキュリティ
- Quota管理
- Admin機能

## 🚀 始め方

### ポータルベースの実習
1. **環境設定から始めてください**: [portal-guide/01-setup.md](./portal-guide/01-setup.md)に従ってAzure Portalでリソースを作成します。
2. **順次学習を推奨**: 各モジュールが前のモジュールのリソースを活用するため、順番に進めてください。

### コードベースの実習（Jupyter Notebook）
1. **環境変数の設定**: 各ノートブックの開始部分の`FOUNDRY_NAME`をユニークな名前に変更してください。
2. **Azure認証**: Azure CLIを使用してログイン（`az login`）
3. **順次実行**: [code-guide/01-setup.ipynb](./code-guide/01-setup.ipynb)からセルを順番に実行して進めてください。

> ⚠️ **重要**: ノートブック実習時は必ず`FOUNDRY_NAME`を変更してください（例：`foundry-myname`）

### 共通事項
- **必要な部分のみ選択**: 特定の機能に興味がある場合は、該当セクションのみを選択して実習できます。
- **リソースのクリーンアップ**: 実習後、不要なリソースは削除してコストを削減してください。

## 📚 参考ドキュメント

- [Microsoft Foundry Documentation](https://ai.azure.com/docs)
- [What is Microsoft Foundry](https://ai.azure.com/docs/what-is-azure-ai-foundry)
- [Get Started with Code](https://ai.azure.com/docs/quickstarts/get-started-code)
- [Foundry Agent Service at Ignite 2025](https://techcommunity.microsoft.com/blog/azure-ai-foundry-blog/foundry-agent-service-at-ignite-2025-simple-to-build-powerful-to-deploy-trusted-/4469788)
- [Agents Overview](https://ai.azure.com/docs/agents/overview)

## 💡 ヒント

- 各実習後にリソースを整理してコストを削減してください
- エラー発生時はAzure PortalのActivity Logを確認してください
- 実習中に作成したコードは保存して再利用してください
- Control Planeでリソース使用量を定期的に確認してください

## 🤝 貢献

このワークショップに対するフィードバックや改善点があれば、Issueを作成してください。

## 📝 ライセンス

このワークショップ資料は教育目的で提供されています。

---

**次のステップ**: [ポータルガイドを始める](./portal-guide/01-setup.md) | [コードガイドを始める](./code-guide/01-setup.ipynb)
