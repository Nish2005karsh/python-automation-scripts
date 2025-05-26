import requests
import pyfiglet
from rich.console import Console
from rich.panel import Panel
from prompt_toolkit import prompt
from prompt_toolkit.completion import WordCompleter
console = Console()
# List of some example cities for autocomplete
cities = [
    "New York", "London", "Paris", "Tokyo", "Delhi",
    "Sydney", "Los Angeles", "Moscow", "Beijing", "Cairo","China", "Berlin", "Madrid", "Rome", "Toronto",
    "São Paulo", "Mexico City", "Istanbul", "Bangkok", "Buenos Aires", "Kuala Lumpur", "Singapore", "Dubai", "Seoul", "Hong Kong",
    "Amsterdam", "Barcelona", "Lisbon", "Athens", "Prague", "Vienna", "Stockholm", "Helsinki", "Oslo", "Copenhagen",
    "Brussels", "Zurich", "Geneva", "Dublin", "Edinburgh", "Belfast", "Glasgow", "Cardiff", "Warsaw", "Budapest",   "Riga", "Tallinn", "Vilnius", "Sofia", "Bucharest", "Belgrade", "Zagreb", "Ljubljana", "Sarajevo", "Podgorica",
    "Skopje", "Pristina", "Tirana", "Athens", "Valletta", "Monaco", "Andorra la Vella", "San Marino", "Vatican City",
]
completer = WordCompleter(cities, ignore_case=True)

def get_weather(city, api_key):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        
        return {
            "Temperature": f"{data['main']['temp']} °C",
            "Condition": data['weather'][0]['description'].title(),
            "Humidity": f"{data['main']['humidity']}%",
            "Wind Speed": f"{data['wind']['speed']} m/s"
        }
    except Exception as e:
        return None

def main():
    api_key = "22241afd6cdcad89fd343d045e478ecc"

    city = prompt("Enter city name: ", completer=completer)
    if not city:
        console.print("[red]No city entered. Exiting.[/red]")
        return

    ascii_banner = pyfiglet.figlet_format(city)
    console.print(ascii_banner, style="bold cyan")

    weather = get_weather(city, api_key)
    if weather:
        panel = Panel.fit(
            "\n".join(f"[bold]{k}:[/bold] {v}" for k, v in weather.items()),
            title=f"Weather for {city}",
            border_style="blue"
        )
        console.print(panel)
    else:
        console.print(f"[red]Could not retrieve weather data for '{city}'. Please check the city name.[/red]")

if __name__ == "__main__":
    main()



