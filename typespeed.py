import random
import time
from rich.console import Console
from rich.prompt import Prompt
from rich.text import Text

console = Console()
sentences = [
    "The quick brown fox jumps over the lazy dog.",
    "Python is an amazing programming language.",
    "Typing speed improves with daily practice.",
    "Focus on accuracy before increasing speed.",
    "Challenge yourself to be faster and better."
]
def calculate_wpm(start, end, typed_text):
    words = len(typed_text.split())
    elapsed_minutes = (end - start) / 60
    return round(words / elapsed_minutes) if elapsed_minutes > 0 else 0
def calculate_accuracy(original, typed):
    correct = sum(o == t for o, t in zip(original, typed))
    total = len(original)
    return round((correct / total) * 100) if total > 0 else 0
def highlight_text(original, typed):
    result = Text()
    for i, char in enumerate(original):
        if i < len(typed):
            if typed[i] == char:
                result.append(char, style="bold green")
            else:
                result.append(char, style="bold red")
        else:
            result.append(char, style="dim")
    return result
def main():
    console.clear()
    console.rule("[bold blue]Typing Speed Test")
    sentence = random.choice(sentences)
    console.print("\nType the following sentence:\n", style="bold yellow")
    console.print(sentence + "\n", style="italic cyan")

    input("Press Enter when ready to start...")
    console.clear()
    console.print(sentence + "\n", style="italic cyan")

    start_time = time.time()
    typed = Prompt.ask("\nStart typing")
    end_time = time.time()

    wpm = calculate_wpm(start_time, end_time, typed)
    accuracy = calculate_accuracy(sentence, typed)

    console.print("\n[bold underline]Results[/bold underline]")
    console.print(f"WPM: [bold green]{wpm}[/bold green]")
    console.print(f"Accuracy: [bold magenta]{accuracy}%[/bold magenta]")

    console.print("\n[bold]Comparison:[/bold]")
    console.print(highlight_text(sentence, typed))

if __name__ == "__main__":
    main()
