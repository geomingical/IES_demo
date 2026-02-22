# 🗣️ Multi-Agent Brainstorming Plan — General Editor Mode

> **Antigravity Orchestration Plan**
> 兩位一般模式編輯針對 Landslide 領域進行自由討論，產出 5 個共識研究假說。

---

## Participants

| Agent | Model | Persona | Instruction File |
|-------|-------|---------|-----------------|
| **Editor A** | Claude (Opus 4.6) | 區域地球科學期刊副編輯（5 年經驗） | `CLAUDE.md` → 一般模式 |
| **Editor B** | Gemini (3 Pro) | 區域地球科學期刊副編輯（5 年經驗） | `GEMINI.md` → 一般模式 |

---

## Objective

兩位副編輯共同閱讀 `envseis_selected_papers.json` 中 **landslide 領域**的論文，透過自由討論，達成共識並產出 **5 個研究假說**。

---

## Data Source

- **File:** `envseis_selected_papers.json`
- **Filter:** `category` 包含 `"landslide"` 的論文
- **Paper count:** ~193 篇（含相關領域如 debris flow、slope stability）

---

## Discussion Protocol

### Phase 1 — Independent Reading & Initial Proposals

Each editor independently reads the landslide papers and proposes their initial set of 5 research hypotheses.

**Editor A (Claude，一般模式):**
```
用一般模式。讀取 envseis_selected_papers.json，只針對 landslide 領域的論文。請使用 scientific-brainstorming skill 的技巧（Cross-Domain Analogies、Assumption Reversal、Scale Shifting 等），提出你的 5 個研究假說初稿。每個假說需包含：研究方向、方法建議、相關文獻、可行性評估。
```

**Editor B (Gemini，一般模式):**
```
用一般模式。讀取 envseis_selected_papers.json，只針對 landslide 領域的論文。請使用 scientific-brainstorming skill 的技巧（Cross-Domain Analogies、Assumption Reversal、Scale Shifting 等），提出你的 5 個研究假說初稿。每個假說需包含：研究方向、方法建議、相關文獻、可行性評估。
```

### Phase 2 — Free-Form Discussion

Both editors can see each other's proposals. They engage in open discussion:

- **評論**對方的假說 — 指出優點、問題、改進空間
- **合併**重疊的想法 — 找到共同主題
- **挑戰**弱假說 — 要求更強的文獻支持或方法論
- **提出新想法** — 如果討論中冒出更好的假說
- **自由交流** — 沒有回合限制，直到雙方滿意為止

**討論引導提示（給 Antigravity）：**
```
請兩位 Editor 互相閱讀對方的假說，開始自由討論。可以質疑、合併、改進、或提出新的假說。目標是達成共識，產出 5 個雙方都同意的 landslide 研究假說。沒有回合限制，討論到雙方都滿意為止。
```

### Phase 3 — Consensus Output

When both editors agree, they produce the final 5 hypotheses in this format:

```markdown
## 共識假說 (Consensus Hypotheses)

### 假說 1: [標題]
**研究方向:** [1-2 句描述]
**方法建議:** [用什麼方法做]
**相關文獻:** [哪些論文支持這個方向]
**可行性:** [為什麼這個做得到]
**共識理由:** [為什麼兩位 editor 都同意這個假說]

### 假說 2: [標題]
...

### 假說 3: [標題]
...

### 假說 4: [標題]
...

### 假說 5: [標題]
...
```

---

## Consensus Criteria

- **Both editors explicitly agree** on each hypothesis
- Each hypothesis has **support from the dataset** (cited papers)
- Each hypothesis is **methodologically feasible** with current technology
- The 5 hypotheses should cover **diverse aspects** of landslide research (not 5 variations of the same idea)

---

## Expected Outcome

5 個穩健、可行、漸進式改良的 landslide 研究假說。品質等級：區域期刊可發表。

---

## Notes for Antigravity

- 兩位 Agent 都使用**一般模式** — 不要切換到 Nature/Science 模式
- 討論語言：中英文混用皆可
- 如果討論陷入僵局，可提醒 Agents 回顧資料集尋找新靈感
- 最終輸出必須是**雙方同意**的版本
