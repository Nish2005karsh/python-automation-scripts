import requests
res = requests.get("https://zenquotes.io/api/random")
quote = res.json()[0]['q'] + " —" + res.json()[0]['a']
print(quote)
