# 06. 評価 (Evaluations)

このモジュールでは、AIエージェントとワークフローのパフォーマンスを体系的に評価する方法を学習します。

## 📋 目次

- [評価概要](#評価概要)
- [評価の作成](#評価の作成)
- [評価基準の理解](#評価基準の理解)
- [評価の実行と結果分析](#評価の実行と結果分析)
- [評価のベストプラクティス](#評価のベストプラクティス)
- [次のステップ](#次のステップ)

## 🎯 学習目標

- AIエージェント評価の重要性を理解
- Foundryの自動評価機能を活用
- 各種評価指標の意味と活用法を学習
- 合成データを使用した評価の実行
- 評価結果の解釈と改善策の導出

## ⏱️ 予想所要時間

約10分

---

## 評価概要

### なぜ評価が重要か？

AIエージェントをプロダクションにデプロイする前に以下の事項を検証する必要があります：

```
正確性 → 関連性 → 一貫性 → 自然さ → 安全性
```

評価なしでデプロイすると：
- ❌ 不正確な回答でユーザーの信頼低下
- ❌ 関連のないレスポンスでユーザー体験悪化
- ❌ 一貫性のない品質でブランドイメージ損傷
- ❌ 不適切なコンテンツ生成で法的問題

### 評価タイプ

| 評価タイプ | 説明 | 使用時期 |
|---------|------|---------|
| **Offline Evaluation** | デプロイ前のテストデータで評価 | 開発段階 |
| **A/B Testing** | 2つのバージョン比較 | プロダクションデプロイ時 |
| **Online Monitoring** | リアルタイムパフォーマンスモニタリング | 運用中 |
| **Human Evaluation** | 人が直接評価 | 品質検証 |

### Microsoft Foundryの評価機能

Foundryは以下を自動化します：
- ✅ テストデータ生成（Synthetic generation）
- ✅ 各種評価指標の適用
- ✅ 大規模評価の実行
- ✅ 結果の可視化と分析

---

## 評価の作成

以前作成した`ModelRouterAgent`を評価します。

### ステップバイステップガイド

1. **Evaluationsセクションへ移動**

   - Foundryポータル右上メニューで**Build**を選択します。
   - **Evaluations**メニューをクリックします。
   
   ![Build > Evaluationsメニュー](../assets/06-01-evaluations-menu.png)

2. **Evaluation Catalog**

   ![Evaluations Catalog](../assets/06-01-evaluations-catalog.png)

3. **新しい評価の作成**

   - **+ Create new evaluation**または**New evaluation**ボタンをクリックします。
   
   ![Create new evaluationボタン](../assets/06-02-create-evaluation.png)

4. **Targetの選択**

   評価対象を選択します：
   
   ![Target選択 (Agent)](../assets/06-03-evaluation-target.png)

   ```
   Target type: Agent
   Agent: ModelRouterAgent
   Version: Latest (または特定のバージョン)
   ```

   **他のTargetオプション**：
   - **Agent**: 単一エージェント評価
   - **Workflow**: ワークフロー評価
   - **Model**: モデル直接評価
   - **Endpoint**: 外部APIエンドポイント評価

5. **Data設定**

   テストデータを選択します：
   
   ![Data設定 (Synthetic generation)](../assets/06-04-evaluation-data1.png)

   ![Data設定 (Synthetic generation)](../assets/06-04-evaluation-data2.png)

   ![Data設定 (Synthetic generation)](../assets/06-04-evaluation-data3.png)

   ```
   Data source: Synthetic generation
   
   Topic: 一般対話および情報提供
   
   Number of samples: 50
   (より多くのサンプルはより信頼できるが時間がかかる)
   
   Languages: Japanese, English
   ```

   **Synthetic Generationとは？**
   - AIが自動で様々なテスト質問を生成
   - 実際の使用パターンをシミュレーション
   - 手動でテストケースを作成する必要なし

   **他のDataオプション**：
   - **Upload dataset**: CSV/JSONファイルのアップロード
   - **Use existing dataset**: 以前保存したデータセットを使用

6. **Criteriaの選択**

   評価基準を選択します：

   ```
   ☑ Groundedness (回答が事実に基づいているか)
   ☑ Relevance (質問と回答の関連性)
   ☑ Coherence (回答の一貫性)
   ☑ Fluency (回答の自然さ)
   ```

   ![Metrics選択 (Groundedness, Relevanceなど)](../assets/06-05-evaluation-metrics.png)

   各基準の詳細説明は以下のセクションを参照してください。

7. **Review**

   設定をレビューします：
   
   ![Review and create](../assets/06-06-evaluation-review.png)

   ```
   Target: ModelRouterAgent (Latest)
   Data: Synthetic (50 samples, Japanese/English)
   Criteria: Groundedness, Relevance, Coherence, Fluency
   Estimated time: ~10-15 minutes
   Estimated cost: $2-5 (サンプル数による)
   ```

8. **Submit**

   - すべての設定を確認した後、**Submit**ボタンをクリックします。
   - 評価がバックグラウンドで実行されます。
   - 進捗状況はEvaluationsページで確認できます。

   ![Evaluation Run](../assets/06-06-evaluation-run.png)

9. **Evaluation Result**

   ![Evaluation Result](../assets/06-06-evaluation-result.png)

   ![Evaluation Result](../assets/06-06-evaluation-result2.png)

   ![Evaluation Result](../assets/06-06-evaluation-result3.png)

   ![Evaluation Result](../assets/06-06-evaluation-result4.png)

   ![Evaluation Result](../assets/06-06-evaluation-result5.png)

   ![Evaluation Result](../assets/06-06-evaluation-result6.png)

### ✅ 確認事項

- 評価が「Running」状態であることを確認
- 予想完了時間を確認
- 必要に応じて他のエージェントやワークフローの評価も作成

---

## 評価基準の理解

### Foundry提供のEvaluator全リスト

Foundryは6つのカテゴリ、32個のEvaluatorを提供しています。

#### 🎯 一般品質 (General Purpose)

| Evaluator | 説明 |
|-----------|------|
| **CoherenceEvaluator** | レスポンスの論理的一貫性とフローを測定 |
| **FluencyEvaluator** | 自然言語の品質と可読性を測定 |
| **QAEvaluator** | Q&A総合評価 *(複合: Groundedness, Relevance, Coherence, Fluency, Similarity, F1Score)* |

#### 📊 テキスト類似度 (Textual Similarity)

| Evaluator | 説明 |
|-----------|------|
| **SimilarityEvaluator** | レスポンスと正解間の意味的類似度 |
| **F1ScoreEvaluator** | 精度と再現率の調和平均 |
| **BleuScoreEvaluator** | 機械翻訳品質 (n-gramベース) |
| **GleuScoreEvaluator** | 文レベルBLEU変形 |
| **RougeScoreEvaluator** | 要約品質 (n-gram再現率) |
| **MeteorScoreEvaluator** | 同義語/語幹考慮の翻訳評価 |

#### 🔍 RAG (Retrieval-Augmented Generation)

| Evaluator | 説明 |
|-----------|------|
| **RetrievalEvaluator** | 情報検索の効果性 |
| **DocumentRetrievalEvaluator** | 正解に対する検索精度 |
| **GroundednessEvaluator** | レスポンスがコンテキストと一致するか (1-5点) |
| **GroundednessProEvaluator** | 高度な根拠性評価 (Azure AI Content Safetyベース) |
| **RelevanceEvaluator** | レスポンスと質問の関連性 (1-5点) |
| **ResponseCompletenessEvaluator** | 正解に対するレスポンス完全性 |

#### 🤖 エージェント (Agentic)

| Evaluator | 説明 |
|-----------|------|
| **IntentResolutionEvaluator** | ユーザー意図把握の精度 |
| **TaskAdherenceEvaluator** | 識別されたタスクの実行度 |
| **ToolCallAccuracyEvaluator** | 正しいツール選択と呼び出し |

#### 🛡️ リスクと安全性 (Risk and Safety)

| Evaluator | 説明 |
|-----------|------|
| **ViolenceEvaluator** | 暴力的コンテンツの検出 |
| **SexualEvaluator** | 性的コンテンツの検出 |
| **SelfHarmEvaluator** | 自傷関連コンテンツの検出 |
| **HateUnfairnessEvaluator** | 嫌悪/差別コンテンツの検出 |
| **IndirectAttackEvaluator** | 間接的攻撃（脱獄試行など）の検出 |
| **ProtectedMaterialEvaluator** | 著作権保護素材の検出 |
| **UngroundedAttributesEvaluator** | 根拠のない主張の検出 |
| **CodeVulnerabilityEvaluator** | コードセキュリティ脆弱性の検出 |
| **ContentSafetyEvaluator** | 安全性総合評価 *(複合: Violence, Sexual, SelfHarm, HateUnfairness)* |

#### 🔧 Azure OpenAI Graders

| Evaluator | 説明 |
|-----------|------|
| **AzureOpenAILabelGrader** | ラベルベースの採点 |
| **AzureOpenAIStringCheckGrader** | 文字列検証採点 |
| **AzureOpenAITextSimilarityGrader** | テキスト類似度採点 |
| **AzureOpenAIGrader** | 汎用Azure OpenAI採点 |

---

### コア評価基準4つ

このワークショップでは最も多く使用される4つの評価基準を使用します。

| 基準 | 定義 | スコア基準 |
|------|------|----------|
| **Groundedness** (根拠性) | 回答が事実/コンテキストに基づいているか | 1=ハルシネーション, 5=事実ベース |
| **Relevance** (関連性) | 回答が質問と関連があるか | 1=無関係, 5=完璧な関連 |
| **Coherence** (一貫性) | 回答が論理的に構造化されているか | 1=混乱, 5=完璧な構造 |
| **Fluency** (流暢性) | 回答が文法的に自然か | 1=不自然, 5=完璧に自然 |

**各基準が重要な理由**：

| Groundedness | Relevance | Coherence | Fluency |
|--------------|-----------|-----------|---------|
| ユーザーの信頼確保 | ユーザー満足度向上 | 理解しやすい回答 | ユーザー体験向上 |
| 法的責任の最小化 | 効率的な情報伝達 | プロフェッショナルなイメージ | ブランドイメージ維持 |
| 虚偽情報の防止 | 対話フローの維持 | 信頼性向上 | 理解度向上 |

---

## 評価のベストプラクティス

| 項目 | 推奨事項 |
|------|----------|
| **サンプル数** | 開発: 10-20個 / テスト: 50-100個 / プロダクション: 200+個 |
| **テストシナリオ** | 一般・複雑・曖昧・多言語質問 + Edge cases |
| **評価周期** | 開発中: 各アップデート時 / デプロイ前: 必須 / デプロイ後: 週次/月次 |
| **基準点スコア** | Groundedness ≥4.0 / その他 ≥3.5 / Pass rate ≥80% |
| **Human Evaluation** | 自動評価と併用して新しい問題パターンを発見 |

---

## 📚 追加リソース

- [Azure AI Evaluation概要](https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/observability?view=foundry#what-are-evaluators)
- [FoundryポータルでのEvaluation実行](https://learn.microsoft.com/en-us/azure/ai-foundry/how-to/evaluate-generative-ai-app?view=foundry)
- [エージェント評価](https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/evaluation-evaluators/agent-evaluators?view=foundry)

---

## 次のステップ

エージェントとワークフローの品質を評価する方法を学びました！次はプロダクション環境でリソースを管理しモニタリングする方法を学習します：

➡️ **[07. Control Plane](./07-control-plane.md)**: Fleet管理、モニタリング、コンプライアンスなどを学習します。

---

[← 前へ: ワークフロー](./05-workflows.md) | [メインへ](./README.md) | [次へ: Control Plane →](./07-control-plane.md)
