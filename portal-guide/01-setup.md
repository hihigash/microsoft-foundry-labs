# 01. 環境設定

このモジュールでは、Microsoft Foundryワークショップを始めるための基本環境を設定します。

## 📋 目次

- [Resource Groupの作成](#resource-groupの作成)
- [Foundryリソースの作成](#foundryリソースの作成)
- [New Foundryポータルの有効化](#new-foundryポータルの有効化)
- [次のステップ](#次のステップ)

## 🎯 学習目標

- Azure Resource Groupの作成方法を理解
- Microsoft Foundryリソースの作成と構成
- 新しいFoundryポータルインターフェースの有効化

## ⏱️ 予想所要時間

約10分

---

## Resource Groupの作成

Resource GroupはAzureリソースを論理的にグループ化するコンテナです。

### ステップバイステップガイド

1. **Azure Portalにアクセス**
   - [Azure Portal](https://portal.azure.com)にログインします。

2. **Resource Groupの作成**
   - 上部の検索バーで「Resource groups」を検索します。
   
   ![Resource groups検索](../assets/01-01-resource-group-search.png)
   
   - **+ Create**ボタンをクリックします。
   
   ![Resource Group作成画面](../assets/01-02-resource-group-create.png)

3. **基本情報の入力**
   ```
   Subscription: [使用中のサブスクリプションを選択]
   Resource group: foundry
   Region: Sweden Central
   ```
   
   ![基本情報入力](../assets/01-03-resource-group-basics.png)

4. **レビューと作成**
   - **Review + create**ボタンをクリックします。
   - 検証完了後、**Create**ボタンをクリックします。

   ![基本情報確認](../assets/01-03-resource-group-basics-2.png)

### ✅ 確認事項

- Resource Groupが正常に作成されたことを確認
- Resource Group名: `foundry`

---

## Foundryリソースの作成

Microsoft FoundryはAIアプリケーション開発のための統合プラットフォームです。

### ステップバイステップガイド

1. **Microsoft Foundryリソースの検索**
   - Azure Portal上部の検索バーで「Microsoft Foundry」を検索します。
   - または直接[Microsoft Foundry Portal](https://ai.azure.com)にアクセスします。
   
   ![Microsoft Foundry検索](../assets/01-04-foundry-search.png)

2. **新しいFoundryリソース＆プロジェクトの作成**
   - **Create a Foundry Resource**ボタンをクリックします。
   
   ![Foundry Resource選択](../assets/01-05-foundry-select-resource.png)

   ```
   Resource group: foundry
   Name: foundry<Your unique name>
   Location: Sweden Central
   Default project name: proj-default
   ```

   - 必須情報を入力してFoundryリソースを作成します。
   - **Review + create**をクリックします。
   - すべての設定を確認した後、**Create**をクリックします。
   - リソースの作成には2-5分程度かかります。

   ![Foundry Resource作成](../assets/01-06-foundry-create-resource.png)

   - **Foundry Resource**概要ページに移動します。

   ![Foundry Resource概要](../assets/01-07-foundry-resource.png)

   - **Go to Foundry portal**をクリックします。 

   ![New Foundry portalホーム](../assets/01-08-foundry-portal.png)

### ✅ 確認事項

- Foundryプロジェクトが正常に作成されたことを確認
- プロジェクト名: `proj-default`

---

## New Foundryポータルの有効化

新しいFoundryポータルは向上したユーザーインターフェースと追加機能を提供します。

### ステップバイステップガイド

1. **New Foundryの有効化**
   - ポータル上部または設定メニューで**「Enable New Foundry」**または**「Try new experience」**オプションを探します。
   - トグルスイッチをオンにして新しいインターフェースを有効化します。
   
   ![New Foundry有効化](../assets/01-09-foundry-new-experience.png)

2. **インターフェースの確認**
   - 新しいポータルインターフェースがロードされることを確認します。
   - 右上メニューで以下のセクションが表示されることを確認：
     - **Discover**: モデル、テンプレートなどの探索
     - **Build**: エージェント、ワークフロー、モデルなどの開発
     - **Operate**: コントロールプレーンなどの管理
   
   ![ポータルナビゲーション](../assets/01-10-foundry-portal-navigation.png)

### ✅ 確認事項

- New Foundryポータルが有効化されたことを確認
- 左側メニューでDiscover、Build、Operateセクションを確認
- プロジェクトホームが正常に表示されることを確認

---

## 📚 追加リソース

- [Microsoft Foundryドキュメント](https://learn.microsoft.com/en-us/azure/ai-foundry/what-is-azure-ai-foundry?view=foundry)
- [Azure Resource Manager概要](https://learn.microsoft.com/azure/azure-resource-manager/management/overview)
- [Azureリージョンと可用性ゾーン](https://learn.microsoft.com/azure/reliability/availability-zones-overview)

---

## 次のステップ

環境設定が完了しました！次のモジュールに進んでください：

➡️ **[02. モデルとデプロイ](./02-models.md)**: 各種AIモデルを探索しデプロイする方法を学習します。

---

[← メインへ](./README.md) | [次へ: モデルとデプロイ →](./02-models.md)
