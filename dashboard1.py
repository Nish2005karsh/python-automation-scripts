import pyfiglet
from rich.console import Console
from rich.table import Table
from rich.prompt import Prompt
import sys
console = Console()
tasks = []
def show_banner():
    ascii_banner = pyfiglet.figlet_format("Task Manager")
    console.print(f"[bold cyan]{ascii_banner}[/bold cyan]")
def show_menu():
    console.print("\n[bold yellow]Options:[/bold yellow]")
    console.print("[1] View Tasks")
    console.print("[2] Add Task")
    console.print("[3] Complete Task")
    console.print("[4] Delete Task")
    console.print("[5] Exit")
def display_tasks():
    if not tasks:
        console.print("[italic]No tasks available.[/italic]")
        return
    table = Table(title="📋 Your Tasks", show_lines=True)
    table.add_column("ID", style="dim")
    table.add_column("Task", style="cyan")
    table.add_column("Status", style="green")
    for idx, task in enumerate(tasks):
        table.add_row(str(idx), task["name"], task["status"])
    console.print(table)

def add_task():
    name = Prompt.ask("Enter task name")
    tasks.append({"name": name, "status": "Pending"})
    console.print("[green]Task added![/green]")

def complete_task():
    display_tasks()
    index = Prompt.ask("Enter task ID to complete")
    try:
        tasks[int(index)]["status"] = "✅ Completed"
        console.print("[green]Task marked as completed![/green]")
    except (IndexError, ValueError):
        console.print("[red]Invalid task ID![/red]")

def delete_task():
    display_tasks()
    index = Prompt.ask("Enter task ID to delete")
    try:
        deleted = tasks.pop(int(index))
        console.print(f"[red]Deleted:[/red] {deleted['name']}")
    except (IndexError, ValueError):
        console.print("[red]Invalid task ID![/red]")

def main():
    show_banner()
    while True:
        show_menu()
        choice = Prompt.ask("Choose an option", choices=["1", "2", "3", "4", "5"])
        if choice == "1":
            display_tasks()
        elif choice == "2":
            add_task()
        elif choice == "3":
            complete_task()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            console.print("[bold cyan]Goodbye! 👋[/bold cyan]")
            sys.exit()

if __name__ == "__main__":
    main()
