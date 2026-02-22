# 🎯 Demo 操作指南

> 本文件包含完整的現場展示流程與 **copy-paste ready** 提示詞。
> 聚焦領域：**Landslide（崩塌／山崩）**

---

## 展示流程總覽

```
Step 1:  python demo.py                        → 展示資料集結構與 Agent 設定
Step 2:  打開 agents.md                         → 講解 Agent = Persona + Model + Skill + Instruction
Step 3:  展示 BRAINSTORM_PLAN_GENERAL.md        → 講解 Multi-Agent 計劃書結構
Step 4:  在 Antigravity 啟動一般模式辯論          → Claude × Gemini 自由討論 → 5 個共識假說
Step 5:  在 Antigravity 啟動頂級模式辯論          → Dr. Rigor × Dr. Narrative 自由辯論 → 5 個 paradigm-shifting 假說
Step 6:  比較兩次輸出                             → 💡 同模型、同資料、不同 Persona → 品質天差地別
```

---

## Step 1 — 展示資料集

```bash
python demo.py
```

會看到：193 篇論文統計、分類分佈、年份分佈、期刊排名、範例摘要。

---

## Step 2 — 講解 Agent 架構

打開 `agents.md`，說明：

```
Agent = Persona（角色設定）+ Model（模型）+ Skill（認知框架）+ Instruction（指令檔）
```

| 模式 | Persona | Model | 指令檔 |
|------|---------|-------|--------|
| 一般模式 | 區域期刊副編輯（5 年） | Claude / Gemini | CLAUDE.md / GEMINI.md |
| 頂級模式 | Nature/Science 資深主編（20+ 年） | Claude / Gemini | CLAUDE.md / GEMINI.md |

重點提示：
- **同一個模型、同一份資料、不同的 Persona → 不同品質的輸出**
- Skill 提供結構化思考框架（Cross-Domain Analogies、Assumption Reversal 等）
- 指令檔 = 角色卡 + 模式切換 + 輸出格式

---

## Step 3 — 講解 Multi-Agent 計劃書

打開 `BRAINSTORM_PLAN_GENERAL.md`，說明：

- **兩份計劃書**：一般模式 vs 頂級模式
- **自由討論**：沒有回合限制，Agent 自由辯論直到共識
- **共識要求**：5 個假說必須雙方都同意
- 計劃書結構：Participants → Objective → Discussion Protocol → Consensus Criteria

---

## Step 4 — 一般模式 Multi-Agent 辯論

> 📄 完整計劃書：[`BRAINSTORM_PLAN_GENERAL.md`](BRAINSTORM_PLAN_GENERAL.md)

在 Antigravity 中使用 `BRAINSTORM_PLAN_GENERAL.md` 啟動 multi-agent session。

兩位一般模式副編輯（Claude + Gemini）會：
1. 各自讀取 landslide 論文並提出 5 個假說初稿
2. 互相評論、質疑、合併
3. 自由討論直到達成共識
4. 產出 5 個雙方同意的研究假說

**預期輸出風格：** 穩健、可行、漸進式改良。像兩位經驗豐富的 reviewer 在討論研究方向。

---

## Step 5 — 頂級模式 Multi-Agent 辯論

> 📄 完整計劃書：[`BRAINSTORM_PLAN_TOPEDITOR.md`](BRAINSTORM_PLAN_TOPEDITOR.md)

在 Antigravity 中使用 `BRAINSTORM_PLAN_TOPEDITOR.md` 啟動 multi-agent session。

Dr. Rigor (Nature) × Dr. Narrative (Science) 會：
1. 各自讀取 landslide 論文並提出 5 個 paradigm-shifting 假說初稿
2. Dr. Rigor 從物理機制角度審查；Dr. Narrative 從全球敘事角度審查
3. 自由辯論 — 交叉審查、合併昇華、淘汰弱者
4. 產出 5 個雙方同意的 paradigm-shifting 研究假說

**預期輸出風格：** 大膽、嚴謹、具突破性。兩位頂級主編的張力會逼出更強的假說。

---

## Step 6 — 對比與討論

展示重點：

| | 一般模式辯論 | 頂級模式辯論 |
|---|---|---|
| 參與者 | 兩位副編輯 | Dr. Rigor × Dr. Narrative |
| 假說等級 | 漸進式改良 | Paradigm-shifting |
| 方法論 | 標準方法延伸 | 跨領域方法突破 |
| 討論深度 | 溫和建設性 | 嚴謹交叉審查 |
| 共識標準 | 可行性、文獻支持 | 物理機制 + 全球敘事 |
| 品質等級 | 區域期刊 | Nature / Science |

**💡 Teaching Takeaways:**

> 1. **Persona matters** — 同一個模型、同一份資料，換一個角色設定，輸出品質天差地別。
> 2. **Multi-Agent > Single-Agent** — 兩個 Agent 辯論產出的假說，比單一 Agent 更全面、更嚴謹。
> 3. **Plan document = Orchestration** — 寫好計劃書，AI 就能自動執行複雜的多步驟工作流。

---

## 補充：文件導覽

| 文件 | 用途 |
|------|------|
| `agents.md` | 4 個 Agent 的完整定義 |
| `BRAINSTORM_PLAN_GENERAL.md` | 一般模式 Multi-Agent 辯論計劃書 |
| `BRAINSTORM_PLAN_TOPEDITOR.md` | 頂級模式 Multi-Agent 辯論計劃書 |
| `CLAUDE.md` | Claude 的指令檔（一般 + Nature 模式） |
| `GEMINI.md` | Gemini 的指令檔（一般 + Science 模式） |
| `.claude/skills/scientific-brainstorming/` | Claude 的 brainstorming skill |
| `.gemini/skills/scientific-brainstorming/` | Gemini 的 brainstorming skill |
| `envseis_selected_papers.json` | 193 篇環境地震學論文資料集 |
| `demo.py` | 資料集視覺化展示（Rich terminal UI） |
