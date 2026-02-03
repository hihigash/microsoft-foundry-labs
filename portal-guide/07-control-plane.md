# 07. Control Plane

このモジュールでは、Microsoft FoundryのControl Planeを通じてプロダクション環境のAIリソースを管理しモニタリングする方法を学習します。

## 📋 目次

- [Control Plane概要](#control-plane概要)
- [Fleet Overview](#fleet-overview)
- [Assets管理](#assets管理)
- [Complianceとセキュリティ](#complianceとセキュリティ)
- [Quota管理](#quota管理)
- [Admin機能](#admin機能)
- [まとめ](#まとめ)

## 🎯 学習目標

- Control Planeの役割と重要性を理解
- Fleet Overviewを通じた全体システムモニタリング
- Assets（エージェント、モデル、ツール）の管理方法
- コンプライアンスとセキュリティ設定の構成
- QuotaとRate Limitingの管理
- プロジェクトとユーザー権限の管理

## ⏱️ 予想所要時間

約10分

---

## Control Plane概要

### Control Planeとは？

Control PlaneはMicrosoft Foundryの中央管理センターで、すべてのAIリソースを統合管理しモニタリングします。

```
Control Plane = モニタリング + 管理 + セキュリティ + ガバナンス
```

### 主要機能領域

```
┌─────────────────────────────────────────┐
│         Control Plane                   │
├─────────────────────────────────────────┤
│ Fleet Overview   │ 全体システムダッシュボード  │
│ Assets          │ リソース管理              │
│ Compliance      │ セキュリティとポリシー     │
│ Quota           │ 割り当てと制限           │
│ Admin           │ プロジェクトと権限        │
└─────────────────────────────────────────┘
```

### なぜ重要か？

プロダクション環境で以下を保証します：
- 📊 **可視性**: すべてのリソースの状態とパフォーマンスを把握
- 🛡️ **セキュリティ**: 脆弱性と脅威の早期発見
- 💰 **コスト管理**: リソース使用量とコストの最適化
- ⚖️ **コンプライアンス**: 規制準拠状態のモニタリング
- 🚨 **アラート**: 問題発生時の即時対応

---

## Fleet Overview

Fleet Overviewはデプロイされたすべてのリソースの状態を一目で確認できるダッシュボードです。

### ダッシュボードへのアクセス

1. **Control Planeへ移動**

   - Foundryポータル右上メニューで**Operate**を選択します。
   
   ![Fleet Overviewダッシュボード](../assets/07-02-fleet-overview.png)

   ![Fleet Overviewダッシュボード](../assets/07-02-fleet-overview2.png)

### 主要メトリクス

#### 1. Running Agents

```
┌────────────────────────────────────┐
│  Running Agents: 5                 │
├────────────────────────────────────┤
│  Active:    4  ✓                   │
│  Warning:   1  ⚠                   │
│  Failed:    0  ✗                   │
└────────────────────────────────────┘

Agents:
- ModelRouterAgent       [Active]
- FileSearchAgent        [Active]
- WebSearchAgent         [Warning] (High latency)
- KnowledgeAgent         [Active]
- KnowledgeAgent2        [Active]
```

**Warning原因の把握**：
- 高いレスポンス時間（Latency）
- エラー率の増加
- 割り当て量の上限接近

#### 2. Agent Success Rate

```
┌────────────────────────────────────┐
│  Overall Success Rate: 96.5%       │
├────────────────────────────────────┤
│  Last 24 hours:                    │
│  ████████████████████░░  96.5%     │
│                                    │
│  Last 7 days trend:                │
│  ▁▂▃▄▅▆█▆▇█ ↗ Improving           │
└────────────────────────────────────┘

By Agent:
- ModelRouterAgent:    98.2% ✓
- FileSearchAgent:     97.5% ✓
- WebSearchAgent:      92.1% ⚠ (改善が必要)
- KnowledgeAgent:      98.8% ✓
- KnowledgeAgent2:     97.3% ✓
```

#### 3. Estimated Cost

```
┌────────────────────────────────────┐
│  Current Month Cost                │
├────────────────────────────────────┤
│  Total:        $245.30             │
│  Projected:    $350.00 (month-end) │
│                                    │
│  Breakdown:                        │
│  Models:       $180.50 (74%)       │
│  Search:       $ 45.20 (18%)       │
│  Storage:      $ 12.40 ( 5%)       │
│  Other:        $  7.20 ( 3%)       │
└────────────────────────────────────┘

Top Consumers:
1. gpt-4-1              $95.30
2. model-router         $65.20
3. text-embedding       $20.00
```

#### 4. Token Usage

```
┌────────────────────────────────────┐
│  Token Usage (24h)                 │
├────────────────────────────────────┤
│  Total:        1.2M tokens         │
│                                    │
│  Input:        800K (67%)          │
│  Output:       400K (33%)          │
│                                    │
│  Hourly Peak:  75K tokens/hour     │
│  Current:      52K tokens/hour     │
└────────────────────────────────────┘

Usage Trend:
Hour: 00  04  08  12  16  20  24
      ▁▁▁▃▅▇█▇▆▅▄▃▂▁
      (Peak: 午後4時)
```

#### 5. Active Alerts

```
┌────────────────────────────────────┐
│  Active Alerts: 2                  │
├────────────────────────────────────┤
│  ⚠ Warning (1)                     │
│    • WebSearchAgent high latency   │
│      Avg response: 8.5s (SLA: 5s)  │
│                                    │
│  ℹ Info (1)                        │
│    • Quota usage at 75%            │
│      gpt-4-1: 750K/1M TPM          │
└────────────────────────────────────┘
```

### ダッシュボードの活用

1. **日次チェック**
   - Success rateの確認
   - Active alertsの確認
   - Costの推移モニタリング

2. **週次レビュー**
   - パフォーマンストレンド分析
   - コスト最適化機会の把握
   - Quota計画

3. **月次計画**
   - キャパシティ計画
   - 予算調整
   - アーキテクチャ最適化

---

## Assets管理

Assetsセクションではデプロイされたすべてのリソースを管理できます。

### Agent管理

1. **Assetsへ移動**

   - Control Planeで**Assets**セクションをクリックします。

2. **Agent登録**

   - 外部エージェントを登録することもできます。
   
   ![Agent登録](../assets/07-08-register-agent.png)

3. **Agentリストの確認**

   ![Assets - Agents](../assets/07-10-assets-agents.png)

### Model管理

デプロイされたモデルの確認と管理：

![Assets - Models](../assets/07-11-assets-models.png)

### Tool管理

エージェントが使用可能なツールの管理：

![Assets - Tools](../assets/07-12-assets-tools.png)

---

## Complianceとセキュリティ

### Policy管理

組織のセキュリティポリシーを設定して適用します。

![Compliance - Policies](../assets/07-14-compliance-policies.png)

### Guardrails設定

AIの出力を制御するガードレールを構成します：

![Guardrails設定](../assets/07-15-guardrails-config.png)

- **Content filtering**: 不適切なコンテンツのフィルタリング
- **PII protection**: 個人情報保護
- **Output validation**: 出力検証ルール

### Security Posture

全体的なセキュリティ態勢を確認します：

![Security Posture](../assets/07-16-security-posture.png)

---

## Quota管理

### TPM (Tokens Per Minute) Quota

モデルごとのトークン使用量の制限を管理します：

![Quota - TPM](../assets/07-17-quota-tpm.png)

```
Model: gpt-5.1
Current Usage: 750,000 TPM
Quota Limit: 1,000,000 TPM
Usage: 75%
```

### PTU (Provisioned Throughput Units)

高スループット環境向けのプロビジョニング管理：

![Quota - PTU](../assets/07-19-quota-ptu.png)

### Quota増加リクエスト

Quotaの増加が必要な場合：
1. **Request increase**ボタンをクリック
2. 必要な容量と理由を入力
3. Azureサポートチームがレビュー

---

## Admin機能

### プロジェクト管理

複数のプロジェクトを管理する方法：

![Admin - Projects](../assets/07-20-admin-projects.png)

### AI Gateway

APIゲートウェイの設定と管理：

![AI Gateway](../assets/07-21-ai-gateway1.png)

![AI Gateway](../assets/07-21-ai-gateway2.png)

---

## まとめ

このワークショップを通じて、Microsoft Foundryの主要機能を体験しました：

### 学習した内容

✅ **環境設定**: Resource GroupとFoundryリソースの作成

✅ **モデル管理**: モデルのデプロイとModel Routerの構成

✅ **エージェント開発**: 各種エージェント（ModelRouter、FileSearch、WebSearch、Knowledge）の構築

✅ **Foundry IQ**: AI SearchとBlob Storageを活用したナレッジベース構築

✅ **ワークフロー**: Sequential、Group Chat、Human-in-loopワークフローの設計

✅ **評価**: エージェントパフォーマンスの体系的な評価

✅ **Control Plane**: プロダクション環境のモニタリングと管理

### 次のステップ

1. **コードベースの実習**: [code-guide](../code-guide/README.md)で自動化を学習
2. **プロダクション適用**: 学習した内容を実際のプロジェクトに適用
3. **継続的な学習**: ドキュメントとアップデートを定期的に確認

### リソースのクリーンアップ

実習が終了したら、不要なリソースを削除してコストを節約してください：

1. Azure Portalで`foundry` Resource Groupに移動
2. **Delete resource group**をクリック
3. Resource Group名を入力して確認

> ⚠️ **注意**: リソースの削除は取り消しできません。必要なデータはバックアップしてください。

---

## 📚 追加リソース

- [Microsoft Foundry Documentation](https://ai.azure.com/docs)
- [Azure AI Services Pricing](https://azure.microsoft.com/pricing/details/cognitive-services/)
- [Azure Security Best Practices](https://learn.microsoft.com/azure/security/fundamentals/best-practices-and-patterns)
- [Microsoft Foundry Community](https://techcommunity.microsoft.com/t5/azure-ai-foundry/bd-p/AzureAIFoundryBlog)

---

## 🎉 おめでとうございます！

Microsoft Foundryハンズオンワークショップを完了しました！

このワークショップで学んだ知識を活用して、より良いAIアプリケーションを構築してください。

---

[← 前へ: 評価](./06-evaluations.md) | [メインへ](./README.md)
