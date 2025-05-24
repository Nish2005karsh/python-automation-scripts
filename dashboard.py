import pyfiglet
from rich.console import Console
from rich.table import Table
# Initialize rich console
console = Console()
# Create ASCII art banner
ascii_banner = pyfiglet.figlet_format("CLI Dashboard")
console.print(f"[bold cyan]{ascii_banner}[/bold cyan]")
# Create a rich table
table = Table(title="📊 Task Overview", style="bold magenta")
table.add_column("Task", style="cyan", no_wrap=True)
table.add_column("Status", style="green")
table.add_column("Progress", justify="right", style="yellow")
# Add rows to the table
table.add_row("Data Sync", "✅ Complete", "100%")
table.add_row("Model Training", "⚙️ Running", "76%")
table.add_row("Report Generation", "⏳ Pending", "0%")
# Display the table
console.print(table)
