import pyfiglet
from tqdm import tqdm
from rich.console import Console
from rich.progress import track
import time
# ---------- 1. ASCII Art ----------
ascii_banner = pyfiglet.figlet_format("Nishkarsh!")
print(ascii_banner)
# ---------- 2. TQDM Progress Bar ----------
print("\n[1] Loading with tqdm:")
for _ in tqdm(range(50), desc="Loading..."):
    time.sleep(0.02)
# ---------- 3. Rich Progress Bar ----------
console = Console()
print("\n[2] Fancy Progress with Rich:")
for step in track(range(10), description="Processing tasks..."):
    time.sleep(0.1)
# ---------- 4. Rich Spinner / Status ----------
print("\n[3] Animated Spinner with Rich:")
with console.status("[bold green]Finalizing magic..."):
    time.sleep(2)

console.print("\n[bold cyan]All done! Your terminal is now beautiful. 🌈[/bold cyan]")

