# Code Guide - Microsoft Foundry コードベースの実習

> ⚠️ **作業中 (Work in Progress)**: このガイドは現在開発中です。一部の内容が不完全であったり変更される可能性があります。

PythonコードとAzure CLIを使用してMicrosoft Foundryリソースを自動化する実習ガイドです。

## �� コードベースの実習の特徴

- ✅ **自動化**: Pythonコードでリソースの作成と管理
- ✅ **再現可能**: コードを保存していつでも再実行
- ✅ **スクリプト作成**: 実務に即座に適用可能なコード作成
- ✅ **Infrastructure as Code**: Azure CLIとREST APIの活用

## 🎯 前提条件

### 必須
- Python 3.8以上
- Azure CLI（`az --version`で確認）
- Azureサブスクリプションとログイン（`az login`）
- Jupyter Notebook実行環境

### 推奨
- **GitHub Codespaces**の使用（すべてのツールが事前インストール済み）
- VS Code + Jupyter Extension
- Python仮想環境（venv）

## 📚 実習モジュール（Jupyter Notebooks）

1. **[01-setup.ipynb](./01-setup.ipynb)** - Resource GroupおよびFoundryリソースの作成
2. **[02-models.ipynb](./02-models.ipynb)** - モデルデプロイおよびModel Router構成
3. **[03-agents.ipynb](./03-agents.ipynb)** - 各種エージェントの構築とデプロイ
4. **[04-foundry-iq.ipynb](./04-foundry-iq.ipynb)** - AI Searchおよびナレッジベース構築
5. **[05-workflows.ipynb](./05-workflows.ipynb)** - Sequential、Group Chat、Human-in-loopワークフロー
6. **[06-evaluations.ipynb](./06-evaluations.ipynb)** - エージェントパフォーマンス評価
7. **[07-control-plane.ipynb](./07-control-plane.ipynb)** - 運用モニタリングと管理

## 🔧 追加スクリプト

- **[invokeAgent.py](../invokeAgent.py)** - デプロイされたAgentを外部から呼び出す例
- **[invokeWorkflow.py](../invokeWorkflow.py)** - デプロイされたWorkflowをプログラム的に実行する例
- **[knowledge-base.json](../knowledge-base.json)** - FileSearchAgent実習用サンプルデータ

## 🚀 始め方

### 1️⃣ 環境設定（ローカル環境）
```bash
# 仮想環境の作成と有効化
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate

# 必要なパッケージのインストール
pip install azure-identity azure-ai-projects openai requests
```

### 2️⃣ Azureログイン
```bash
az login
az account set --subscription "Your-Subscription-Name"
```

### 3️⃣ ノートブックの実行
1. **[01-setup.ipynb](./01-setup.ipynb)**を開く
2. 最初のセルの`FOUNDRY_NAME`変数をユニークな名前に変更（例：`foundry-myname`）
3. セルを順番に実行

> ⚠️ **重要**: `FOUNDRY_NAME`はグローバルでユニークである必要があります。自分の名前やイニシャルを含めてください。

### 4️⃣ GitHub Codespacesの使用（推奨）
1. このリポジトリをフォーク
2. 「Code」→「Create codespace on main」をクリック
3. Codespaceが開いたら即座にノートブックを実行可能

## 💡 学習のヒント

- **順次学習**: 各ノートブックは前のモジュールで作成したリソースを使用します
- **環境変数の共有**: `.foundry_config.json`ファイルで設定値を保存・共有します
- **エラー処理**: 各セルのレスポンスコードを確認し、エラーメッセージを読んでください
- **コードの修正**: 提供されたコードを自由に修正しながら学習してください

## 🔄 ポータルガイドとの関係

- **同じ目標**: ポータルガイドとコードガイドは同じ成果物を作成します
- **学習順序**: ポータルで概念を学んでからコードで自動化することを推奨します
- **選択可能**: 希望する方式のみを選択して実習できます

## 📚 関連ドキュメント

- [Azure AI Foundry SDK for Python](https://learn.microsoft.com/python/api/overview/azure/ai-projects-readme)
- [Azure CLI Reference](https://learn.microsoft.com/cli/azure/)
- [Foundry REST API Documentation](https://learn.microsoft.com/rest/api/aiservices/)

## 💡 次のステップ

コード実習を完了した後：
- 作成したリソースを[ポータル](https://ai.azure.com)で確認してみてください
- `invokeAgent.py`と`invokeWorkflow.py`スクリプトを実行してみてください
- 自分だけのエージェントやワークフローを作成してみてください

---

**開始する**: [01-setup.ipynb](./01-setup.ipynb)
