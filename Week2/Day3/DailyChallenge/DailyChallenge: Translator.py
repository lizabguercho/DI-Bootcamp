import googletrans
print(googletrans.LANGUAGES)
from googletrans import Translator



translator = Translator()

french_words= ["Bonjour", "Au revoir", "Bienvenue", "A bientôt"] 

translated = translator.translate(french_words, src='fr', dest='en')

for trans in translated:
    print(f'{trans.origin} -> {trans.text}')


