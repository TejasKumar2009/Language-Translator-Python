import googletrans

from_lang = input("Enter the language from translate : ")
to_lang = input("Enter the language to translate : ")
sentence = input("Enter the word or sentence you want to translate : ")

from_lang.lower()
to_lang.lower()

for key, value in googletrans.LANGUAGES.items():
   if value == from_lang:
      from_lang_code = value
   if value == to_lang:
      to_lang_code = value

translator = googletrans.Translator()
trans1 = translator.translate(sentence, src=from_lang_code, dest=to_lang_code)
text = trans1.text
print(f"Text Translated from {from_lang} to {to_lang}")
print(f"In {from_lang} : {sentence}")
print(f"In {to_lang} : {text}")
