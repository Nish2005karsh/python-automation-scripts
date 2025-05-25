import pyfiglet
from rich.console import Console, Group
from rich.live import Live
from rich.panel import Panel
from rich.table import Table
from rich.text import Text
from rich.layout import Layout
from datetime import datetime
import psutil
import time
console = Console()
def make_header():
    banner = pyfiglet.figlet_format("CLI Dashboard", font="slant")
    return Panel(Text(banner, justify="center"), style="bold cyan")

def make_system_stats():
    cpu = psutil.cpu_percent()
    mem = psutil.virtual_memory().percent
    return Panel(f"[bold yellow]CPU:[/bold yellow] {cpu}%   [bold yellow]RAM:[/bold yellow] {mem}%", title="📊 Usage")

def make_task_table():
    table = Table.grid(expand=True)
    table.add_column(justify="left", style="cyan")
    table.add_column(justify="right", style="green")

    table.add_row("Data Sync", "✅ Complete")
    table.add_row("Model Training", "⚙️ Running")
    table.add_row("Report Generation", "⏳ Pending")
    return Panel(table, title="📋 Tasks")

def make_time_panel():
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return Panel(f"[bold magenta]Current Time:[/bold magenta] {now}", border_style="magenta")

def make_layout():
    layout = Layout()
    layout.split(
        Layout(name="header", size=3),
        Layout(name="body", ratio=2),
        Layout(name="footer", size=3),
    )
    layout["body"].split_row(
        Layout(name="left"),
        Layout(name="right")
    )
    return layout

with Live(console=console, refresh_per_second=1) as live:
    layout = make_layout()
    while True:
        layout["header"].update(make_header())
        layout["left"].update(make_system_stats())
        layout["right"].update(make_task_table())
        layout["footer"].update(make_time_panel())

        live.update(layout)
        time.sleep(1)
