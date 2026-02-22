# 🌍 Environmental Seismology: Multi-Agent AI Brainstorming Demo

This repository demonstrates **Agentic AI for scientific research** — AI personas with distinct editorial philosophies brainstorm hypotheses over 190+ environmental seismology papers.

**Core demo concept:** Same Model + Same Data + **Different Persona** → Dramatically Different Output Quality.

No hardcoded dialogue. No fake simulations. **Real AI agents reasoning over real data.**

## 🤖 The Agents

> **Full agent definitions → [`agents.md`](agents.md)**

Each agent is built from: **Persona + Model + Skills + Instruction File**

| Mode | Persona | Model | Instruction |
|------|---------|-------|-------------|
| 一般模式 | Associate Editor (5 yr) | Claude (Opus 4.6) | `CLAUDE.md` |
| **Nature 模式** | 🧠 **Dr. Rigor** — *Nature Geoscience* (20+ yr) | Claude (Opus 4.6) | `CLAUDE.md` |
| 一般模式 | Associate Editor (5 yr) | Gemini (3 Pro) | `GEMINI.md` |
| **Science 模式** | 🗣️ **Dr. Narrative** — *Science* (20+ yr) | Gemini (3 Pro) | `GEMINI.md` |

**一般 Editor** suggests incremental improvements within established frameworks.

**Dr. Rigor** demands paradigm-shifting breakthroughs with rigorous physical mechanisms.

**Dr. Narrative** connects Earth data to planetary-scale crises and policy relevance.

## 🧠 The Skill: `scientific-brainstorming`

Both models share the same structured cognitive framework in their respective skill directories:

- `.claude/skills/scientific-brainstorming/` — loaded by Claude Code
- `.gemini/skills/scientific-brainstorming/` — loaded by Gemini CLI

The skill applies techniques like **Cross-Domain Analogies**, **Assumption Reversal**, **Scale Shifting**, and **SCAMPER/TRIZ** frameworks to push beyond summarization into genuine hypothesis generation.

## 📊 The Dataset

`envseis_selected_papers.json` contains **190+ curated research paper abstracts** covering:

- Landslides, debris flows, rockfalls
- Glacial hazards, slope stability
- Seismological methods, volcanic processes, erosion

Each paper includes: title, authors, year, journal, DOI, abstract, summary, categories, and citation count.

## 💻 Quick Start

### 1. Clone and explore the data

```bash
git clone https://github.com/geomingical/IES_demo.git
cd IES_demo
pip install -r requirements.txt
python demo.py
```

`demo.py` shows you the dataset: paper counts, category breakdowns, year distributions, sample abstracts, and all 4 agent configurations.

### 2. Launch multi-agent brainstorming

完整操作指南 → **[`DEMO_GUIDE.md`](DEMO_GUIDE.md)**

Two brainstorming plan documents for Antigravity:

| Plan | Participants | Output |
|------|-------------|--------|
| [`BRAINSTORM_PLAN_GENERAL.md`](BRAINSTORM_PLAN_GENERAL.md) | 兩位一般模式副編輯 | 5 個穩健可行的共識假說 |
| [`BRAINSTORM_PLAN_TOPEDITOR.md`](BRAINSTORM_PLAN_TOPEDITOR.md) | Dr. Rigor × Dr. Narrative | 5 個 paradigm-shifting 共識假說 |

Both plans use **free-form discussion** — Claude and Gemini debate until they reach consensus on 5 hypotheses.

Compare the output quality between General and Top-Tier modes — same models, same data, different personas.

### 3. See example output

Check `.archive/output_hypotheses.md` for a sample of what the agents produce.

## 📁 Repository Structure

```
IES_demo/
├── agents.md                          # ⭐ Agent definitions (4 agents, 2 modes × 2 models)
├── DEMO_GUIDE.md                      # 🎯 操作指南與展示流程
├── BRAINSTORM_PLAN_GENERAL.md         # 🗣️ Multi-Agent 辯論計劃書（一般模式）
├── BRAINSTORM_PLAN_TOPEDITOR.md       # 🔬 Multi-Agent 辯論計劃書（頂級模式）
├── CLAUDE.md                          # Claude instructions (General + Nature modes)
├── GEMINI.md                          # Gemini instructions (General + Science modes)
├── README.md                          # This file
├── demo.py                            # Dataset explorer (Rich terminal UI)
├── requirements.txt                   # Python dependencies (rich)
├── envseis_selected_papers.json       # 190+ research paper abstracts
├── .claude/
│   └── skills/
│       └── scientific-brainstorming/  # Brainstorming skill (Claude)
│           ├── SKILL.md
│           └── references/
├── .gemini/
│   └── skills/
│       └── scientific-brainstorming/  # Brainstorming skill (Gemini)
│           ├── SKILL.md
│           └── references/
└── .archive/                          # Previous versions & example output
```

## 🔧 Prerequisites

- **Python 3.8+** with `rich` library (for `demo.py`)
- **Claude Code** or **Gemini CLI** (for live brainstorming)
- **Antigravity** account (for managed workspace access)

## 📖 How It Works

This repo showcases the **agentic AI project structure**:

1. **Agent definitions** (`agents.md`) — define *who each AI is* (persona, model, skills)
2. **Instruction files** (`CLAUDE.md` / `GEMINI.md`) — tell each AI *what to do* (workflow, constraints, mode switching)
3. **Skills** (`.claude/skills/` / `.gemini/skills/`) — give the AI *structured cognitive frameworks*
4. **Data** (`envseis_selected_papers.json`) — the raw material the AI reasons over

When you launch `claude` or `gemini` in this directory, the CLI automatically reads the instruction file and discovers available skills. Switch between General and Top-Tier modes via your prompt.

## 🎓 Demo Flow (Suggested)

```
Step 1:  python demo.py                        → 展示資料集結構與 Agent 設定
Step 2:  打開 agents.md                         → 講解 Agent = Persona + Model + Skill + Instruction
Step 3:  展示 BRAINSTORM_PLAN_GENERAL.md        → 講解 Multi-Agent 計劃書結構
Step 4:  在 Antigravity 啟動一般模式辯論          → Claude × Gemini 自由討論 → 5 個共識假說
Step 5:  在 Antigravity 啟動頂級模式辯論          → Dr. Rigor × Dr. Narrative 自由辯論 → 5 個 paradigm-shifting 假說
Step 6:  比較兩次輸出                             → 💡 同模型同資料不同 Persona → 品質天差地別
```

> 完整操作指南 → [`DEMO_GUIDE.md`](DEMO_GUIDE.md)
> 一般模式計劃書 → [`BRAINSTORM_PLAN_GENERAL.md`](BRAINSTORM_PLAN_GENERAL.md)
> 頂級模式計劃書 → [`BRAINSTORM_PLAN_TOPEDITOR.md`](BRAINSTORM_PLAN_TOPEDITOR.md)

**Teaching takeaway:** Prompt Engineering isn't just "asking questions" — designing an Agent's persona, standards, and thinking framework fundamentally changes AI output quality.

---

*Built for the IES (Institute of Earth Sciences) Agentic AI Workshop. Created via the Antigravity Agentic AI Workspace.*