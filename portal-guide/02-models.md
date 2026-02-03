# 02. モデルとデプロイ

このモジュールでは、Microsoft Foundryで提供される各種LLMモデルを探索しデプロイする方法を学習します。

## 📋 目次

- [モデル探索 (Discover)](#モデル探索-discover)
- [モデル比較とデプロイ](#モデル比較とデプロイ)
- [Embeddingモデルのデプロイ](#embeddingモデルのデプロイ)
- [Model Routerのデプロイ](#model-routerのデプロイ)
- [Model Routerの構成](#model-routerの構成)
- [次のステップ](#次のステップ)

## 🎯 学習目標

- モデルリーダーボードを通じたモデルパフォーマンスの比較
- 各種AIモデルのデプロイ方法の理解
- Model Routerの設定と構成
- モデルルーティング戦略の理解

## ⏱️ 予想所要時間

約15分

---

## モデル探索 (Discover)

FoundryポータルのDiscoverセクションで各種AIモデルを探索できます。

### ステップバイステップガイド

1. **Discoverセクションへ移動**
   - Foundryポータル右上メニューで**Discover**をクリックします。

   ![Discover > Models メニュー](../assets/02-00-discover-overview.png)

   - **Models**メニューを選択します。
   
   ![Discover > Models メニュー](../assets/02-01-discover-models.png)

2. **モデルリーダーボードの確認**
   - **View leaderboard**オプションをクリックします。
   - 各種モデルのパフォーマンス指標を確認できます：
     - Quality scores
     - Latency
     - Cost
     - Context window
     - Modality support (text, vision, audio)
   
   ![Model Leaderboard画面](../assets/02-02-model-leaderboard.png)

3. **モデルカテゴリの理解**
   - **Language Models**: GPT-5.1、GPT-5、Claudeなど
   - **Embedding Models**: text-embedding-3-large、text-embedding-ada-002など

### 💡 ヒント

- リーダーボードは定期的に更新されるため、最新モデルを確認してください
- 各モデルの詳細ページでcapabilitiesとlimitationsを確認してください

---

## モデル比較とデプロイ

### GPT-5.1モデルのデプロイ

1. **モデル比較機能の使用**
   - Modelsページで**Compare models**ボタンをクリックします。
   - 比較したいモデルを選択します（例：GPT-5.1、GPT-5、Claude 4.5 Sonnet）。
   - パフォーマンス、コスト、機能を比較します。
   
   ![Compare models機能](../assets/02-03-model-compare.png)

2. **GPT-5.1の選択とデプロイ**
   - モデルリストから**gpt-5.1**を探します。
   - モデルカードをクリックして詳細情報を確認します。
   
   ![GPT-5.1モデルカード](../assets/02-04-gpt51-model-card.png)

3. **デプロイ設定**
   - **Deploy**ボタンをクリックします。
   
   ![Deployボタン](../assets/02-05-gpt51-deploy-button.png)

4. **デプロイ完了**
   - **Default settings**をクリックしてデプロイを開始します。
   - デプロイ完了まで1-2分程度かかります。

### ✅ 確認事項

- Build > Modelsセクションでデプロイされた`gpt-5.1`モデルを確認
- デプロイステータスが「Succeeded」であることを確認
- Endpoint URLが生成されたことを確認

![Build > Modelsでデプロイされたgpt-5.1を確認](../assets/02-07-gpt51-deployed.png)

---

## Embeddingモデルのデプロイ

Embeddingモデルはテキストをベクトルに変換し、意味的検索や類似度計算に使用されます。

### ステップバイステップガイド

1. **Embeddingモデルの検索**
   - Discover > Modelsページで検索バーに**「text-embedding」**を入力します。
   - フィルターを使用してEmbeddingモデルのみを表示できます。
   
   ![text-embedding検索](../assets/02-08-embedding-search.png)

2. **text-embedding-3-largeの選択**
   - **text-embedding-3-large**モデルを選択します。
   - モデル詳細情報の確認：
     - Dimensions: 3072
   
   ![text-embedding-3-largeモデルカード](../assets/02-09-embedding-model-card.png)

3. **デプロイ設定**
   ```
   Deployment name: text-embedding-3-large
   Model version: [最新バージョン]
   Deployment type: Standard
   ```

4. **デプロイ実行**
   - **Deploy**ボタンをクリックしてデプロイします。
   
   ![デプロイ完了確認](../assets/02-10-embedding-deployed.png)

---

## Model Routerのデプロイ

Model Routerは複数のモデル間でインテリジェントなルーティングを提供し、コスト、品質、パフォーマンスを最適化します。

### ステップバイステップガイド

1. **Model Routerの検索**
   - Discover > Modelsで**「model-router」**を検索します。
   
   ![model-router検索](../assets/02-11-model-router-search.png)

2. **Model Router情報の確認**
   - Model Routerの主な機能：
     - 自動モデル選択
     - ロードバランシング
     - コスト最適化
     - 品質ベースのルーティング

3. **デプロイ設定**
   ```
   Deployment name: model-router
   Routing strategy: Balanced (デフォルト)
   Included models: [利用可能なモデルを自動検出]
   ```
   
   ![Model Routerデプロイ設定](../assets/02-12-model-router-deploy.png)

4. **デプロイ完了**
   - **Deploy**ボタンをクリックします。
   - Model Routerが使用可能なデプロイ済みモデルを自動検出します。

### ✅ 確認事項

- Build > Modelsで`model-router`デプロイを確認
- デプロイステータスを確認
- Routerがアクセス可能なモデルリストを確認

![Build > Models全体デプロイリスト](../assets/02-15-models-overview.png)

---

## Model Routerの構成

Model Routerのルーティング戦略を設定してアプリケーション要件に合わせて最適化します。

### ステップバイステップガイド

1. **Model Router詳細ページへ移動**
   - Build > Modelsセクションに移動します。
   - デプロイされた**model-router**をクリックします。

2. **Editモードへ進入**
   - **Details**タブを選択します。
   - **Edit**ボタンをクリックします。
   
   ![Model Router設定画面 (Editモード)](../assets/02-13-model-router-config.png)

3. **Model Router Configuration設定**
   
   #### Routing Modeオプション：
   
   ![Routing Modeオプション](../assets/02-14-model-router-modes.png)
   
   **a) Balanced Mode（バランスモード）**
   ```
   Description: コスト、品質、パフォーマンスのバランスを維持
   Use case: 一般的なプロダクションワークロード
   Behavior: リクエストに応じて適切なモデルを自動選択
   ```

   **b) Quality Mode（品質モード）**
   ```
   Description: 最高品質のレスポンスを優先
   Use case: 精度が重要なアプリケーション
   Behavior: 最も性能の良いモデルを優先使用
   Cost: 相対的に高コスト
   ```

   **c) Cost Mode（コストモード）**
   ```
   Description: コスト最適化を優先
   Use case: 大量のシンプルなリクエスト処理
   Behavior: コスト効率の良いモデルを優先使用
   Quality: 基本品質を維持
   ```

4. **ルーティングモードの選択**
   - ワークショップでは**Balanced**モードを選択します。
   - 必要に応じて他のモードに変更可能です。

5. **保存と適用**
   - **Save**ボタンをクリックして設定を保存します。
   - 変更は即座に適用されます。

### 📊 Model Router動作例

```
ユーザーリクエスト → Model Router → 判断：
  - シンプルな質問 → GPT-5-nano (低コスト)
  - 複雑な分析 → GPT-5-mini (高品質)
  - コード生成 → Codex系
  - 高負荷 → 負荷分散
```

### 💡 最適化のヒント

- **開発環境**: Cost Modeでコスト削減
- **プロダクション**: Balanced Modeで安定性確保
- **顧客向けサービス**: Quality Modeでユーザー体験向上
- **A/Bテスト**: モード別パフォーマンス比較分析

---

## 📚 追加リソース

- [Model Catalogガイド](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-models/concepts/models-sold-directly-by-azure?view=foundry&tabs=global-standard-aoai%2Cstandard-chat-completions%2Cglobal-standard&pivots=azure-openai)
- [Model Router概要](https://learn.microsoft.com/en-us/azure/ai-foundry/openai/concepts/model-router?view=foundry)
- [Embedding Modelsガイド](https://learn.microsoft.com/en-us/azure/ai-foundry/openai/how-to/embeddings?view=foundry&tabs=python-new)

---

## 次のステップ

モデルデプロイが完了しました！これらのモデルを活用してエージェントを構築しましょう：

➡️ **[03. エージェント開発](./03-agents.md)**: 各種機能を持つAIエージェントを作成します。

---

[← 前へ: 環境設定](./01-setup.md) | [メインへ](./README.md) | [次へ: エージェント開発 →](./03-agents.md)
