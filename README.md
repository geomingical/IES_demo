# Environmental Seismology: Multi-Agent Brainstorming Demo

This repository demonstrates the power of Agentic AI workflows in scientific research. By utilizing distinct AI personas (acting as Senior Editors at top-tier journals) and a structured brainstorming skill, this demo analyzes a dataset of 190+ Environmental Seismology papers to generate highly original, paradigm-shifting research hypotheses.

## Overview

The core objective is to showcase how Large Language Models (LLMs)—specifically Gemini 3.1 Pro and Claude Opus 4.6—can move beyond simple text summarization. By assigning them strict editorial standards and an interdisciplinary "scientific-brainstorming" framework, the agents interactively critique ideas, challenge assumptions, and synthesize massive datasets into actionable future research directions focusing on **Landslides, Debris Flows, and Slope Stability**.

## Repository Structure

### 📄 1. The Dataset
* **`envseis_selected_papers.json`**: The source material. A JSON file containing abstracts, titles, and metadata for recent papers in the field of Environmental Seismology.

### 🧠 2. The Core Skill
* **`skills/scientific-brainstorming/SKILL.md`**: The guiding framework for the AI agents. It forces the models to use techniques like *Cross-Domain Analogies*, *Scale Shifting*, and *Assumption Reversal* instead of generating generic summaries.

### 👥 3. Agent Personas (A/B Testing)
This project includes two sets of agent configurations to demonstrate how "System Prompts" dramatically alter AI output:
* **`agent_v1.md`**: Standard Senior Editors. Focuses on rigorous methodology and broad planetary narratives.
* **`agent.md`**: Elite 20+ Year Senior Editors at *Nature Geoscience* and *Science*. This persona is highly critical, rejects "incremental science," and demands textbook-rewriting paradigm shifts.

### ⚙️ 4. Execution Configuration
* **`Gemini.md` & `Claude.md`**: Documents detailing why these specific models were chosen (Gemini for massive context ingestion; Claude for high-fidelity logical critique).
* **`demo.py`**: The Antigravity Agentic AI Workspace configuration file. It defines the models, dataset, and skill dependencies to execute the multi-agent dialogue.

### 💡 5. Output Hypotheses
The results of the automated brainstorming sessions:
* **`output_hypotheses_v1.md`**: The output generated under the standard `agent_v1.md` persona. High quality, safe, and logical research topics.
* **`output_hypotheses.md`**: The output generated under the elite `agent.md` persona. Features radical, interdisciplinary, and high-impact ideas (e.g., *Thermodynamic Nucleation Precursors*, *Predictive SPH-Seismic Coupling*).

## How to Demo

This workspace is designed to be executed via an Agentic Engine (like Antigravity).

1. Review the `agent.md` and `skills/` folder to understand the constraints placed on the AI.
2. Observe how the agents interact and critique each other's ideas in the `Dialogue Transcript` section of the output files.
3. Compare `output_hypotheses_v1.md` with `output_hypotheses.md` to see the profound impact of altering an AI's persona (System Prompt) on its scientific ideation capabilities.

---
*Created via Antigravity Agentic AI Workspace.*
