from googletrans import Translator

# Initialize the Translator
translator = Translator()

# English text to be translated
text = "Hello, how are you?"

# Translate text from English to Hindi
translated = translator.translate(text, src='en', dest='hi')

# Print the translated text
print("Translated text:", translated.text)
