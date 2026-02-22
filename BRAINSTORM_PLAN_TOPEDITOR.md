# 🔬 Multi-Agent Brainstorming Plan — Top-Tier Editor Mode

> **Antigravity Orchestration Plan**
> Dr. Rigor (Nature) × Dr. Narrative (Science) 針對 Landslide 領域進行頂級編輯辯論，產出 5 個共識研究假說。

---

## Participants

| Agent | Model | Persona | Instruction File |
|-------|-------|---------|-----------------|
| **Dr. Rigor** | Claude (Opus 4.6) | *Nature Geoscience* 資深主編（20+ 年） | `CLAUDE.md` → Nature 模式 |
| **Dr. Narrative** | Gemini (3 Pro) | *Science* 資深主編（20+ 年） | `GEMINI.md` → Science 模式 |

---

## Objective

兩位世界級期刊主編共同閱讀 `envseis_selected_papers.json` 中 **landslide 領域**的論文，透過自由辯論，達成共識並產出 **5 個 paradigm-shifting 研究假說**。

兩位主編有截然不同的哲學：
- **Dr. Rigor** 要求嚴謹的物理機制和教科書級突破
- **Dr. Narrative** 要求全球敘事和政策衝擊力

最終假說必須**同時滿足兩位主編的標準**。

---

## Data Source

- **File:** `envseis_selected_papers.json`
- **Filter:** `category` 包含 `"landslide"` 的論文
- **Paper count:** ~193 篇（含相關領域如 debris flow、slope stability）

---

## Discussion Protocol

### Phase 1 — Independent Reading & Initial Proposals

Each editor independently reads the landslide papers and proposes their initial set of 5 paradigm-shifting hypotheses.

**Dr. Rigor (Claude，Nature 模式):**
```
切換 Nature 模式。讀取 envseis_selected_papers.json，只針對 landslide 領域的論文。請使用 scientific-brainstorming skill，提出你的 5 個 paradigm-shifting 研究假說初稿。要求：(1) 每個假說必須挑戰現有範式 (2) 必須有嚴謹的物理機制 (3) 必須能根本性改寫教科書。不要漸進式科學，要突破性的。
```

**Dr. Narrative (Gemini，Science 模式):**
```
切換 Science 模式。讀取 envseis_selected_papers.json，只針對 landslide 領域的論文。請使用 scientific-brainstorming skill，提出你的 5 個 paradigm-shifting 研究假說初稿。要求：(1) 每個假說必須能引起全球關注 (2) 必須連結到行星尺度的氣候危機 (3) 必須有社會政策意義。要能登 Science 封面的等級。
```

### Phase 2 — Free-Form Debate

Both editors can see each other's proposals. They engage in open, rigorous debate:

- **互相挑戰** — Dr. Rigor 質疑物理機制的嚴謹性；Dr. Narrative 質疑全球影響力
- **交叉審查** — 每個假說必須同時通過「Nature 標準」和「Science 標準」
- **合併與昇華** — 將雙方最強的想法融合為更高層次的假說
- **淘汰弱者** — 無法同時滿足兩位主編的假說直接淘汰
- **自由辯論** — 沒有回合限制，直到雙方都認為假說達到頂級期刊水準

**辯論引導提示（給 Antigravity）：**
```
請 Dr. Rigor 和 Dr. Narrative 互相閱讀對方的假說，開始自由辯論。Dr. Rigor 從物理機制和方法論突破的角度評審；Dr. Narrative 從全球敘事和社會衝擊的角度評審。每個假說必須同時通過兩位主編的標準才能進入最終名單。目標：5 個雙方都同意的 paradigm-shifting landslide 研究假說。沒有回合限制，辯論到雙方都滿意為止。
```

### Phase 3 — Consensus Output

When both editors agree, they produce the final 5 hypotheses in this format:

```markdown
## Paradigm-Shifting Consensus Hypotheses

### Hypothesis 1: [Title]
**Core Concept:** [1-2 sentences — the breakthrough idea]
**Methodological Breakthrough:** [What changes in how we do science]
**Physical Mechanism:** [Dr. Rigor's stamp — rigorous mechanistic basis]
**Global Narrative:** [Dr. Narrative's stamp — why the world should care]
**Key Evidence from Dataset:** [Which papers support or motivate this]
**Testability:** [First experiment to validate]
**Societal Impact:** [Policy implications and civilizational significance]
**Consensus Note:** [Why both editors agree this is paradigm-shifting]

### Hypothesis 2: [Title]
...

### Hypothesis 3: [Title]
...

### Hypothesis 4: [Title]
...

### Hypothesis 5: [Title]
...
```

---

## Consensus Criteria

- **Both editors explicitly agree** — Dr. Rigor confirms physical rigor; Dr. Narrative confirms global impact
- Each hypothesis must be **paradigm-shifting** — not incremental improvements
- Each hypothesis must have a **testable physical mechanism** (Nature standard)
- Each hypothesis must have **civilizational or policy relevance** (Science standard)
- The 5 hypotheses should cover **diverse aspects** of landslide research
- Quality level: **publishable as lead article in Nature or Science**

---

## Expected Outcome

5 個 paradigm-shifting 的 landslide 研究假說，同時具備：
- 🧠 嚴謹的物理機制（Nature 標準）
- 🌍 全球敘事與政策衝擊力（Science 標準）
- 📊 來自資料集的文獻支持
- 🔬 可實驗驗證的預測

品質等級：Nature / Science 等級。

---

## Notes for Antigravity

- Claude 使用 **Nature 模式**（Dr. Rigor）；Gemini 使用 **Science 模式**（Dr. Narrative）
- 兩位主編有不同的評審哲學 — 這是 **feature, not bug** — 張力會產出更強的假說
- 討論語言：中英文混用皆可
- 如果辯論陷入僵局（某假說一方堅持另一方反對），可建議 Agents 修改假說而非放棄
- 最終輸出必須是**雙方同意**的版本 — 任何一方不同意則不列入
