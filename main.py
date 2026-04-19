import sys
import os
import time
from datetime import datetime
from rich.console import Console
from rich.panel import Panel
from rich.layout import Layout
from rich.table import Table
from rich.live import Live
from rich.text import Text
from rich.progress import Progress, SpinnerColumn, TextColumn
from rich.align import Align

from src.am_layer.orchestrator import ArtificialMind
from src.utils.logger import logger

console = Console()

def create_header():
    grid = Table.grid(expand=True)
    grid.add_column(justify="left", ratio=1)
    grid.add_column(justify="center", ratio=1)
    grid.add_column(justify="right", ratio=1)
    grid.add_row(
        "[bold cyan]HANIF-AI-OS v0.2[/bold cyan]",
        "[bold yellow]MISSION CONTROL CENTER[/bold yellow]",
        datetime.now().strftime("[bold white]%Y-%m-%d %H:%M:%S[/bold white]")
    )
    return Panel(grid, style="blue")

def create_sidebar():
    table = Table(show_header=False, box=None, padding=(0, 1))
    table.add_row("[cyan]SYSTEM:[/cyan]", "[green]ONLINE[/green]")
    table.add_row("[cyan]AI-LAYER:[/cyan]", "[green]STANDBY[/green]")
    table.add_row("[cyan]AC-LAYER:[/cyan]", "[green]SECURE[/green]")
    table.add_row("[cyan]D-LOGS:[/cyan]", "[yellow]SYNCED[/yellow]")
    table.add_row("-" * 15)
    table.add_row("[bold magenta]HANIF CORE[/bold magenta]")
    table.add_row("v0.2 STABLE")
    return Panel(table, title="[bold blue]Status[/bold blue]", border_style="blue")

def create_main_layout():
    layout = Layout()
    layout.split_column(
        Layout(name="header", size=3),
        Layout(name="body")
    )
    layout["body"].split_row(
        Layout(name="sidebar", size=25),
        Layout(name="main_console")
    )
    return layout

class HanifApp:
    def __init__(self):
        self.mind = ArtificialMind()
        self.history = []

    def run(self):
        layout = create_main_layout()
        layout["header"].update(create_header())
        layout["sidebar"].update(create_sidebar())
        
        # Display welcome
        welcome_text = Text("\nWelcome to Hanif AI Architecture.\nEnter your intent to begin the ethical synthesis loop.\n(Type 'exit' to shutdown)", justify="center", style="bold white")
        layout["main_console"].update(Align.center(Panel(welcome_text, title="Terminal", border_style="cyan")))

        console.clear()
        console.print(layout)

        while True:
            try:
                user_input = console.input(f"\n[bold green]Intent > [/bold green]").strip()
                
                if user_input.lower() in ['exit', 'quit', 'çıkış']:
                    console.print("[bold yellow]Initiating system shutdown...[/bold yellow]")
                    time.sleep(1)
                    break
                
                if not user_input:
                    continue

                # Run progress spinner for "AI Thinking"
                with Progress(
                    SpinnerColumn(),
                    TextColumn("[bold cyan]{task.description}"),
                    transient=True,
                ) as progress:
                    progress.add_task(description="Synthesizing Decision Loop...", total=None)
                    result = self.mind.process_request(user_input)
                
                meta = result['metadata']
                state = result['state']
                
                # Determine colors
                state_style = "bold green"
                if "RED" in state: state_style = "bold red"
                elif "YELLOW" in state: state_style = "bold yellow"

                # Decision Log Panel
                log_table = Table(show_header=True, header_style="bold blue", box=None)
                log_table.add_column("Metric", style="cyan")
                log_table.add_column("Value", style="white")
                log_table.add_row("Consensus State", f"[{state_style}]{state}[/{state_style}]")
                log_table.add_row("Overall AC Score", f"[magenta]{meta['ac_score']:.2f}[/magenta] (Target: >0.70)")
                
                # Add individual agent scores if available
                agent_scores = meta.get('agent_scores', {})
                if agent_scores:
                    log_table.add_row("-" * 15, "-" * 5)
                    for agent, data in agent_scores.items():
                        color = "green" if data['score'] >= 0.7 else "yellow" if data['score'] >= 0.4 else "red"
                        log_table.add_row(f"  > {agent.capitalize()} Score", f"[{color}]{data['score']:.2f}[/{color}]")
                    log_table.add_row("-" * 15, "-" * 5)

                log_table.add_row("AI Weight (α)", f"{meta['weights']['alpha']:.1f}")
                log_table.add_row("AC Weight (β)", f"[yellow]{meta['weights']['beta']:.2f}[/yellow]")
                
                decision_panel = Panel(
                    log_table, 
                    title="[bold cyan]Synthesis Results[/bold cyan]", 
                    border_style="cyan",
                    padding=(1, 2)
                )

                # Output Panel
                output_panel = Panel(
                    result['response'],
                    title=f"[bold white]Final Output[/bold white]",
                    border_style=state_style.split()[-1], # Use red/yellow/green from style
                    padding=(1, 2)
                )

                # Update Layout
                console.clear()
                layout["header"].update(create_header())
                # Render the panels sequentially for interaction
                console.print(layout["header"])
                console.print(decision_panel)
                console.print(output_panel)
                
            except KeyboardInterrupt:
                break
            except Exception as e:
                console.print(f"[bold red]CRITICAL SYSTEM ERROR: {str(e)}[/bold red]")
                logger.error(str(e))

if __name__ == "__main__":
    app = HanifApp()
    app.run()
