from tabulate import tabulate
from deep_translator import GoogleTranslator


class TranslateClass(object):
    def __init__(self, word, lang):
        self.word = word
        self.lang = lang

    def __repr__(self):
        try:
            translated = GoogleTranslator(source='auto', target=self.lang).translate(self.word)
            data = [
                ['Language:', "Word/Sentence"],
                ['English', self.word],
                [self.lang, translated]
            ]
            table = str(tabulate(data, headers="firstrow", tablefmt="grid"))
            return table
        except Exception as e:
            return f"Error: {e}"


if __name__ == '__main__':
    translate = input('Enter Word/Sentence...')
    language = 'hi'  # Translates to Hindi
    print(TranslateClass(translate, language))
