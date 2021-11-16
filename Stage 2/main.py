# Stage 2/7: Over the internet

# Theory

# User-Agent field in a request

# When you use requests library, you can pass headers arguments to
# the function get(). Headers are text data you send over HTTP that
# might contain information about a web browser or application you use
# to surf the web. Your program doesn't use any web browser as we
# usually do, but it still has to present itself as some kind of browser to
# be able to get the web pages. For this purpose, there's a 'User-
# Agent' field that forms a request.
# import requests

# headers = {'User-Agent': 'Mozilla/5.0'}
# page = requests.get(url, headers=headers)


# Think of it as a visit card that your program shows to the website
# before it can enter it. In introduces itself as a web browser to the
# website it's trying to get a page from; otherwise, the website might not
# allow the connection from something other than a browser.

# Selecting text data

# When you access a web pages, an important question is how to ge tthe
# data that you need in a readable form without HTML tags. The answer
# is CSS. You can access this text via CSS classes and tags. All you need is
# to go the web page, open your browser's Dev Tools, and find
# these elements in CSS code. You can get access to your browser's
# DevTools in three different ways:

# Keyboard: Ctrl + Shift + I, except
# - Internet Explorer and Edge: F12
# - macOs:  ⌘ + ⌥ + I

# Menu bar:
# - Firefox: Menu ➤ Web Developer ➤ Toggle Tools, or Tools ➤
#   Web Developer ➤ Toggle Tools
# - Chrome: More Tools ➤ Developer tools
# - Safari: Develop ➤ Show Web Inspector. If you can't see the
#   Develop menu, go to Safari ➤ Preferences ➤ Advanced, and
#   check the Show Develop menu in the menu bar checkbox.
# - Opera: Developer ➤ Developer tools

# Content menu: Press-and-hold/right-click an item on a web page (Ctrl-
# click on the Mac), and choose the option Inspect Element from the
# content menu that appears (an added bonus: this method highlights
# the code of the element you right-clicked.)

# After you're done with CSS, check it.

# Description

# At this stage, you'll be able to implement a real translator program!
# A great website called ReverseContent will help you to do that.
# ReversoContent is a multilinggual translator tool that allows seeing
# original phrases that should be translated and their equivalents in
# other languages in contexts (example sentences). That's a very
# useful feature since the meaning of the word depends greatly on
# the context. Hence, when you see a context, it's easier for you to
# choose the right translation.

# The goal of your program at this stage is to find translations and
# example sentences for a given word. The word can be either in
# French or in English, and the translation should be in the opposite
# language (that is, English or French, respectively).

# To understand how to do this, go to ReversoContext and type
# any word you want to translate. After receiving the result, pay
# attention to the address bar of your browser. You will see the URL,
# for example:

# http://context.reverso.net/translation/english-french/cheese

# Here you see the language-translation pair <<English-French>>, which
# represents the direction of translation, meaning that the translation
# is from English to French and not the other way around. After the
# last backslash, you can see the word being translated.

# Your goal is to make your program act as if it visits the website for
# you. To make it happen, tell your program to generate the correct
# URL with the word you type, determine the translation direction,
# and send the URL to the website.

# After getting to the needed page, the program should extract hte
# required data: translations and sentences with usage examples. In
# the screenshot below, translations are highlighted with blue, adn
# sentences for the target language are presented in a list in the right
# column.

# TODO
# At this stage, your program should:
# 1. Take an input specifying the target language(en if the
#    user wants to translate from French into English, or fr if
#    the user wants to translate from English into French).
# 2. Take an input specifying the word that should be translated.
# 3. Output the confirmation message in the format You
#    chose "..." as a language to translate "...".
# 4. Form a request and connect to ReversoContext.
# 5. Check the HTTP status of the response of the website to
#    your request. If teh status code is 200, you are good to
#    proceed! If not... Try again?
# 6. Output the response of the website to your request (200)
#    and OK message to show that the connection is successful
#    (so, the entire line should be 200 OK).
# 7. Output the line Tranlations.
# 8. Output a list with translations of the given word in the
#    target language: ['bonjour', 'salut'].
# 9. Output a list with examples of sentences featuring the given
#    word or any of its translations: ['Well, hello,
#    freedom fighters.', 'Et bien, bonjour
#    combattants de la liberté.']. Both the original
#    versions of the sentences and their translations should be
#    printed. You don't need to filter sentences in any way: just
#    print all the sentences that ReversoContext output for the
#    given language pair and the given word.

# Make sure you output exactly the sentences that ReversoContext
# shows initially on the page
# https://context.reverso.net/translation/{language_1}-{language_2}/{word}.
# Don't confound them with the sentences that the websites show when you
# click on the first translation equivalent.
# These sentences will not be accepted by tests.

# Also, please, make your program follows the described format
# of the output.

# Examples
# The greater-than symbol followed by a space ( > ) represents the
# user input. Note that it's not part of the input.

# Type "en" if you want to translate from French into
# English, or "fr" if you want to translate from English
# into French.
# > fr
# > Type the word you want to translate:
# > hello
# You chose "fr" as a language to translate "hello".
# 200 OK
# Translations
import requests

from bs4 import BeautifulSoup


class MultiOnlineTranslator:

    def __init__(self):
        self.language = None
        self.word = None
        self.headers = {'User-Agent': 'Mozilla/5.0'}
        self.url = 'https://context.reverso.net/translation/{}/{}'
        self.welcome_message = 'Type "en" if you want to translate from French ' \
                               'into English, or "fr" if you want to translate ' \
                               'from English into French: '
        self.translate_message = "Type the word you want to translate: "
        self.language_message = 'You chose "{}" as the language to translate "{}".'
        self.r = None
        self.soup = None

    def translations(self):
        example = []
        print("Translations")
        self.soup = BeautifulSoup(self.r.content, 'html.parser')
        # anchors = self.soup.find_all('a', {'class': 'dict'})
        # for a in anchors:
        #     if a.text != "":
        #         temp.append(a.text.strip())
        # print(temp)
        # print([a.text.strip() for a in self.soup.find_all('a', {'class': 'dict'})])
        print([a.text.strip() for a in self.soup.select("#translations-content > .translation")])
        # ex = self.soup.find_all('div', {'class': 'example'})
        # for e in ex:
        #     for ee in e.find_all('div', 'ltr'):
        #         example.append(ee.find('span', {'class': 'text'}).text.strip())
        # print(example)
        # print([e.text.strip() for e in self.soup.find_all('div', {'class': ['src', 'trg']})])
        print([a.text.strip() for a in self.soup.select('#examples-content > .example > .ltr')])

    def checker(self):
        while True:
            self.r = requests.get(self.url.format(self.language, self.word),
                                  headers=self.headers)
            if self.r.status_code == 200:
                break
        return str(self.r.status_code) + " OK"

    def ask(self):
        return input()

    def language_setter(self):
        return 'english-french' if self.language == 'fr' else 'french-english'

    def start(self):
        print(self.welcome_message)
        self.language = self.ask()
        self.language = self.language_setter()
        print(self.translate_message)
        self.word = self.ask()
        print(self.language_message.format(self.language, self.word))
        print(self.checker())
        self.translations()


def main():
    translator = MultiOnlineTranslator()
    translator.start()


if __name__ == '__main__':
    main()
