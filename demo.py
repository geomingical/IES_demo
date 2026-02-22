"""
Environmental Seismology AI Brainstorming Engine — Dataset Explorer

Displays dataset statistics, category breakdowns, and sample papers.
This is a data exploration tool, NOT a dialogue simulator.
To start real AI brainstorming, run: claude  or  gemini
"""

import json
import time
import random
from pathlib import Path
from collections import Counter
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich import box

console = Console()


def load_papers():
    """Load papers from JSON file."""
    paper_path = Path("envseis_selected_papers.json")
    if not paper_path.exists():
        console.print("[red]Error: envseis_selected_papers.json not found![/red]")
        console.print(
            "[dim]Make sure you're running this from the IES_demo directory.[/dim]"
        )
        return []
    with open(paper_path, "r", encoding="utf-8") as f:
        return json.load(f)


def show_header(num_papers):
    """Display the title and agent configuration."""
    console.clear()
    console.print()
    console.print(
        Panel(
            "[bold cyan]🌍 Environmental Seismology AI Brainstorming Engine[/bold cyan]\n\n"
            f"[white]Dataset:[/white] [green]{num_papers} Research Papers[/green] on geohazards & environmental seismology\n"
            "[white]Skill:[/white] [magenta]scientific-brainstorming[/magenta] (Cross-Domain Analogies, Assumption Reversal, Scale Shifting)\n"
            "[white]Source:[/white] [dim]envseis_selected_papers.json[/dim]",
            border_style="cyan",
            padding=(1, 2),
        )
    )

    # Agent comparison table — 4 agents (2 modes × 2 models)
    agent_table = Table(
        box=box.ROUNDED,
        show_header=True,
        header_style="bold white",
        title="[bold]Agent Configuration[/bold]  [dim](see agents.md for full definitions)[/dim]",
        title_style="white",
        padding=(0, 2),
    )
    agent_table.add_column("Mode", style="bold")
    agent_table.add_column("Persona", style="italic")
    agent_table.add_column("Model", style="dim")
    agent_table.add_column("Instruction", style="green")

    # General mode agents
    agent_table.add_row(
        "一般模式",
        "Associate Editor (5 yr)",
        "Claude (Opus 4.6)",
        "CLAUDE.md",
        style="dim",
    )
    agent_table.add_row(
        "一般模式",
        "Associate Editor (5 yr)",
        "Gemini (3 Pro)",
        "GEMINI.md",
        style="dim",
    )

    # Top-tier mode agents
    agent_table.add_row(
        "[bold cyan]Nature 模式[/bold cyan]",
        "[bold]🧠 Dr. Rigor[/bold] — Nature Geoscience",
        "Claude (Opus 4.6)",
        "CLAUDE.md",
    )
    agent_table.add_row(
        "[bold magenta]Science 模式[/bold magenta]",
        "[bold]🗣️  Dr. Narrative[/bold] — Science",
        "Gemini (3 Pro)",
        "GEMINI.md",
    )

    console.print(agent_table)
    console.print()

    # Key insight panel
    console.print(
        Panel(
            "[bold yellow]💡 Demo Concept:[/bold yellow]  Same Model + Same Data + [bold]Different Persona[/bold] → Dramatically Different Output Quality",
            border_style="yellow",
            padding=(0, 2),
        )
    )
    console.print()


def show_category_breakdown(papers):
    """Show how many papers per category."""

    cat_counter = Counter()
    for p in papers:
        for cat in p.get("categories", [p.get("category", "unknown")]):
            cat_counter[cat] += 1

    table = Table(
        box=box.SIMPLE_HEAVY,
        show_header=True,
        header_style="bold cyan",
        title="[bold]📊 Category Breakdown[/bold]",
        title_style="cyan",
        padding=(0, 2),
    )
    table.add_column("Category", style="bold")
    table.add_column("Papers", justify="right", style="green")
    table.add_column("", min_width=30)

    max_count = max(cat_counter.values()) if cat_counter else 1
    for cat, count in cat_counter.most_common():
        bar_len = int((count / max_count) * 25)
        bar = "█" * bar_len + "░" * (25 - bar_len)
        table.add_row(cat, str(count), f"[cyan]{bar}[/cyan]")

    console.print(table)
    console.print()


def show_year_distribution(papers):
    """Show year distribution of papers."""
    year_counter = Counter(p.get("year", 0) for p in papers)

    table = Table(
        box=box.SIMPLE_HEAVY,
        show_header=True,
        header_style="bold yellow",
        title="[bold]📅 Year Distribution[/bold]",
        title_style="yellow",
        padding=(0, 2),
    )
    table.add_column("Year", style="bold")
    table.add_column("Papers", justify="right", style="green")
    table.add_column("", min_width=30)

    max_count = max(year_counter.values()) if year_counter else 1
    for year in sorted(year_counter.keys()):
        count = year_counter[year]
        bar_len = int((count / max_count) * 25)
        bar = "█" * bar_len + "░" * (25 - bar_len)
        table.add_row(str(year), str(count), f"[yellow]{bar}[/yellow]")

    console.print(table)
    console.print()


def show_top_journals(papers, n=8):
    """Show top journals by paper count."""
    journal_counter = Counter(p.get("journal", "Unknown") for p in papers)

    table = Table(
        box=box.SIMPLE_HEAVY,
        show_header=True,
        header_style="bold green",
        title="[bold]📰 Top Journals[/bold]",
        title_style="green",
        padding=(0, 2),
    )
    table.add_column("#", style="dim", justify="right")
    table.add_column("Journal", style="bold")
    table.add_column("Papers", justify="right", style="green")

    for i, (journal, count) in enumerate(journal_counter.most_common(n), 1):
        table.add_row(str(i), journal, str(count))

    console.print(table)
    console.print()


def show_sample_papers(papers, n=4):
    """Display a sample of paper abstracts."""
    console.print("[bold white]📄 Sample Papers from the Dataset[/bold white]\n")

    by_cat = {}
    for p in papers:
        cat = p.get("category", "unknown")
        by_cat.setdefault(cat, []).append(p)

    samples = []
    cats = list(by_cat.keys())
    random.shuffle(cats)
    for cat in cats:
        if len(samples) >= n:
            break
        paper = random.choice(by_cat[cat])
        samples.append(paper)

    for paper in samples:
        title = paper.get("title", "Untitled")
        authors = ", ".join(paper.get("authors", [])[:3])
        if len(paper.get("authors", [])) > 3:
            authors += " et al."
        year = paper.get("year", "")
        journal = paper.get("journal", "")
        categories = ", ".join(paper.get("categories", []))
        abstract = paper.get("abstract", "No abstract available.")
        if len(abstract) > 300:
            abstract = abstract[:297] + "..."

        content = (
            f"[bold]{title}[/bold]\n"
            f"[italic dim]{authors} ({year}) — {journal}[/italic dim]\n"
            f"[magenta]Categories: {categories}[/magenta]\n\n"
            f"{abstract}"
        )

        console.print(Panel(content, border_style="blue", padding=(1, 2), width=100))

    console.print()


def show_next_steps():
    """Show how to start real AI brainstorming."""
    console.print(
        Panel(
            "[bold white]🚀 Ready to Brainstorm![/bold white]\n\n"
            "完整操作指南 → [bold cyan]DEMO_GUIDE.md[/bold cyan]\n\n"
            "Multi-Agent 辯論計劃書：\n\n"
            "  [bold cyan]BRAINSTORM_PLAN_GENERAL.md[/bold cyan]    →  一般模式：Claude × Gemini 副編輯討論 → 5 個共識假說\n"
            "  [bold magenta]BRAINSTORM_PLAN_TOPEDITOR.md[/bold magenta]  →  頂級模式：Dr. Rigor × Dr. Narrative 辯論 → 5 個 paradigm-shifting 假說\n\n"
            "[bold yellow]💡 Same model, same data, different persona → different quality[/bold yellow]\n\n"
            "[dim]Agent 定義 → agents.md｜指令檔 → CLAUDE.md / GEMINI.md｜操作指南 → DEMO_GUIDE.md[/dim]",
            border_style="green",
            title="[bold green]Next Steps[/bold green]",
            padding=(1, 2),
        )
    )


if __name__ == "__main__":
    try:
        papers = load_papers()
        if not papers:
            raise SystemExit(1)

        num_papers = len(papers)

        show_header(num_papers)
        time.sleep(0.5)

        show_category_breakdown(papers)
        time.sleep(0.3)

        show_year_distribution(papers)
        time.sleep(0.3)

        show_top_journals(papers)
        time.sleep(0.3)

        show_sample_papers(papers)

        show_next_steps()

    except KeyboardInterrupt:
        console.print("\n[red]Demo interrupted.[/red]")
