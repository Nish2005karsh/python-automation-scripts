import nltk
nltk.download('punkt')
from nltk.tokenize import sent_tokenize
text = input("Paste your text:\n")
sentences = sent_tokenize(text)
print("\n".join(sentences[:3]))
