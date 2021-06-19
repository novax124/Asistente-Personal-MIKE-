import googletrans
from googletrans import Translator

#print(googletrans.LANGUAGES)

text1 = "hello, how are you?"

text2 = "hola ¿Cómo estás?"

text3 = "hola, com estàs?"

translator = Translator()
"""
print(translator.detect(text1))
print(translator.detect(text2))
print(translator.detect(text3))
"""
#print("Translated  From Spanish : ", translator.translate(text2))

print("Translate ES to EN : ", translator.translate(text1, src = "en", dest = "es"))