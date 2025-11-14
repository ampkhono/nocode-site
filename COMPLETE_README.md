# 完全版 README — 教育用ノーコードクイズ／診断プラットフォーム

## 1. プロジェクト概要
本プロジェクトは、**教育者や文系の学生が自力でクイズ／診断教材を作成し、学習者の理解度を可視化できるノーコード・プラットフォーム**です。学科長から正式に引き継いだ案件として、授業用コンテンツを効率よく作り、理解度の個別最適化を実現することを目指します。

- **目的**: プログラミング不要で教材を設計し、学習者の解答データを活用した診断・フィードバックを提供すること。
- **意義**:
  - **理解度の可視化**: 正答率だけでなく、回答過程・分岐・スコアベクトルから多面的に学習状態を把握。
  - **個別最適化**: 分岐とスコアリングを組み合わせ、学習者に合ったルート・解説を提示。
  - **教材作成の効率化**: テンプレート／GUIエディタ／自動出力により、短時間で学習素材を量産。
- **背景**: 学科長から引き継いだ研究プロジェクトとして、教育実践と研究を両立するフラグシップ案件。

---

## 2. コアコンセプト（Vision / Philosophy）
- **「理解度とは何か？」を再定義**: 単純な正解率ではなく、概念理解・誤答傾向・思考経路を含む“理解構造”を重視。
- **理解構造にフォーカス**: 誤答パターンや思考の一貫性を計測し、概念ツリー上で“欠損”や“直感頼り”を可視化。
- **将来的な自動解説生成**: スコアリングベクトルと glossary.json を紐づけ、理解不足領域に合わせた解説を自動提供。
- **思考過程を評価**: 分岐・選択順序・YES/NOの連続的回答から、学習者の“思考プロファイル”を推定する。
- **AI連携を前提に設計**: すべてのデータをJSONで構造化し、概念モデルと自動解説エンジンに接続可能。

---

## 3. 全フェーズのロードマップ
| フェーズ | 目標 |
| --- | --- |
| **Phase 1: MVP** | プロジェクト作成、エディタでの問題作成、選択肢追加・正解設定・並び替え、JSON保存（editor.json / quiz.json）、Playerでの出題と採点 |
| **Phase 2: 診断エンジン基盤** | 分岐ロジック、N次元スコアリングベクトル、誤答パターン分類、回答ログ収集 |
| **Phase 3: 概念構造モデル** | 概念ツリー（Concept Graph）、一貫性チェック、直感回答／概念欠損の推定 |
| **Phase 4: Glossary機能** | プロジェクト単位の glossary.json、用語のCRUD、概念タグ付け・親子関係 |
| **Phase 5: 自動解説生成** | 回答結果から必要用語を推定 → glossary参照 → 個別化された解説ページを自動生成 |
| **Phase 6: 評価・可視化フェーズ** | 理解度分布、誤答傾向チャート、概念ツリー上の穴を可視化、学習者レポート自動生成 |
| **Phase 7: 学会レベル拡張** | IRT導入検討、認知負荷推定、適応学習アルゴリズム |

---

## 4. 機能一覧
- **Editor（ノーコードUI）**: ブロックベースのGUIで質問／診断ノード／結果ノードを作成。正誤判定や分岐設定も操作可能。
- **Player（学習者画面）**: ランダム化された回答順を提示し、診断ロジックに沿って進行。正誤フィードバックとスコア表示に対応。
- **Diagnostic Engine**: N次元スコアベクトル・分岐マップ・誤答パターンを解釈し、結果表示や今後の分析に利用。
- **Glossary DB**: Phase4で導入予定。用語辞書をJSONで管理し、解説生成や概念タグ付けに利用。
- **Concept Graph**: Phase3で導入予定。概念間の依存関係や理解度をマッピングし、学習の穴を表示。
- **Explanation Engine**: Phase5で導入予定。回答データ＋glossary＋concept graphから個別解説を自動生成。

---

## 5. JSON仕様
### ◆ quiz.json（MVP）
```jsonc
{
  "version": 2,
  "startNode": "q_0",
  "questions": [
    {
      "id": "q_0",
      "type": "question",
      "title": "導入クイズ",
      "question_text": "問いの本文",
      "enableGrading": true,
      "choices": [
        { "id": "a", "text": "選択肢A", "nextId": "q_1", "isCorrect": true },
        { "id": "b", "text": "選択肢B", "nextId": "r_fail", "isCorrect": false }
      ],
      "next": {},
      "concepts": ["intro.logic"]
    }
  ],
  "results": [
    { "id": "r_fail", "type": "result", "text": "もう一度！" }
  ]
}
```

### ◆ diagnostic_question.json（Phase2〜）
```jsonc
{
  "id": "dq_1",
  "type": "diagnostic_question",
  "question_text": "理解スタイルを教えてください",
  "question_type": "single_choice",
  "choices": [
    { "id": "deep", "text": "じっくり考える" },
    { "id": "fast", "text": "直感で選ぶ" }
  ],
  "scoring": [
    { "choice_id": "deep", "vector": { "logic": 2, "emotion": -1 } },
    { "choice_id": "fast", "vector": { "logic": -1, "emotion": 2 } }
  ],
  "next": {
    "deep": "dq_followup1",
    "fast": "dq_followup2",
    "default": "dq_followup1"
  },
  "concepts": ["meta.cognition"]
}
```

### ◆ glossary.json（Phase4）
```jsonc
{
  "terms": [
    {
      "id": "concept.logic_tree",
      "name": "論理ツリー",
      "definition": "複雑な問題を分解する思考モデル",
      "parent": "concept.analysis",
      "tags": ["analysis", "problem-solving"]
    }
  ]
}
```

### ◆ concept_graph.json（Phase3）
```jsonc
{
  "nodes": [
    { "id": "concept.analysis", "label": "分析力", "prerequisites": [] },
    { "id": "concept.logic_tree", "label": "論理ツリー", "prerequisites": ["concept.analysis"] }
  ],
  "edges": [
    { "from": "concept.analysis", "to": "concept.logic_tree", "weight": 0.8 }
  ],
  "consistency_rules": [
    { "id": "rule_01", "description": "論理ツリーの得点が高い場合、分析力も一定以上であるべき" }
  ]
}
```

**共通フィールド例**
- `id`, `type`, `question_text`
- `choices[]`: `id`, `text`, `nextId`, `isCorrect`
- `scoring.vector`: `{ "logic": number, "emotion": number, ... }`
- `next`: `{ "choice_id": "node_id", "default": "fallback" }`
- `concepts`: 紐づく概念IDを配列で保持

---

## 6. フォルダ構成（将来構想を含む）
```
/src
  /editor        # ノーコードUI（React/TypeScript想定）
  /player        # 学習者用画面・診断ロジック
  /diagnostic    # スコアリング・分岐エンジン
  /glossary      # 用語集管理モジュール
  /concepts      # 概念ツリー／一貫性チェック
/projects
  /{project_id}
    editor.json
    quiz.json
    glossary.json
    concept_graph.json
/docs
  roadmap.md
  architecture.md
```

---

## 7. アーキテクチャ設計
- **四層構造**
  - **Editor Layer**: ブロックベースUIでJSONを編集。ノーコード操作。
  - **Player Layer**: 学習者向け画面。分岐・スコアリング・正誤判定を実行。
  - **Engine Layer**: Diagnostic Engine / Explanation Engine / Concept Graph 判定。
  - **Storage Layer**: JSONファイル（MVP）、将来的にはDBやクラウドストレージも想定。
- **設計思想**
  - ブロックベースUI・JSONデータ駆動により、AIや外部ツールとの連携が容易。
  - 後述フェーズでAI統合（自動解説生成、適応学習）を前提としたAPI設計。

---

## 8. 技術スタック（現段階の想定）
- フロントエンド: **React + TypeScript**（仮）
- バックエンド: **Node.js/Express**（仮）
- データ保存: **JSONファイル**（MVP） → LocalStorage / IndexedDB（ブラウザ）
- 将来的なクラウド環境: Firebase / Supabase / 実験用DB（未決定）
- テスト: Jest / Cypress（予定）

---

## 9. 今後の拡張メモ（開発者向け）
- **モジュール分割**: Editor・Player・Engineを独立したパッケージに。層ごとの責務を厳密化。
- **セキュリティ**: MVPではシンプルなローカル利用を想定。ユーザー認証／アクセス制御はPhase6以降。
- **AI連携**: 回答ログ→自動解析→解説生成を想定。LLM API／学術用モデルとの連携を検討。
- **クラウドDB**: 需要に応じてJSONをNoSQL/Graph DBへ移行する拡張性を確保。
- **可観測性**: Phase6以降で学習者レポートや可視化を導入する際、ログ構造・イベント追跡を整備。

---

## 10. 参考操作フロー（MVP）
1. `editor.html` を開く（ローカルでOK）。
2. 「テンプレ読み込み」からクイズ／診断のベースをロード。
3. 質問ブロックを編集し、正誤判定・分岐をGUIで設定。
4. 「👁️ プレビュー」で実行確認。回答順序は自動でランダム化。
5. JSON（quiz.json / editor.json）を保存し、プロジェクトフォルダに配置。
6. Playerアプリに読み込ませれば、学習者向け画面が利用可能。

---

本READMEは、MVPから研究レベルの拡張までを一貫して説明するための「完全版」です。今後の開発・研究にあたっては、各フェーズのロードマップとJSON仕様を基点に、概念モデルやAI機能の実装を進めてください。招聘予定の教育現場・研究機関への共有資料としてもそのまま利用可能です。*** End Patch***

