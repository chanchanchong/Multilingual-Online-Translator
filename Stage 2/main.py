# Stage 2/7: Over the internet

# Description
# The first step of this project is preparation for a convenient translation
# process. At this stage, there'll be only two available languages: English and
# French. The program should suggest to the user to choose the direction of
# the translation and the word to translate. Then the confirmation message
# should be printed.

# Objectives

# At this stage, your program should:
# 1. Output the welcoming message: Type "en" if you want to
#    translate from French into English, or "fr" if you
#    want to translate from English into French:
# 2. Take an input specifying the target language.
# 3. Output the message: Type the word you want to
#    translate:
# 4. Output the confirmation message in the format You chose
#    "language" as a language to translate "word".,
#    where language is either en or fr and word is the word
#    chosen by the user.

# Example

# The greater-than followed by a space ( > ) represents the user
# input. Note that it's not part of the input.

# Type "en" if you want to translate from French into English,
# or "fr" if you want to translate from English into French:
# > fr
# Type the word you want to translate:
# > hello
# You chose "fr" as the language to translate "hello" to.

# We don't really need this output to appear at the end. However, aside from
# keeping the user informed, it does something else: it's showing us if the
# arguments were successfully accepted by the function. Keep it in mind while
# proceeding from stage to stage!

class MultiOnlineTranslator:
    def __init__(self):
        self.welcome_message = 'Type "en" if you want to translate from French ' \
                               'into English, or "fr" if you want to translate ' \
                               'from English into French: '
        self.translate_message = "Type the word you want to translate: "
        self.language_message = 'You chose "{}" as the language to translate "{}" to.'
        self.language = None
        self.word = None

    def ask(self, message):
        return input(message)

    def start(self):
        self.language = self.ask(self.welcome_message)
        self.word = self.ask(self.translate_message)
        print(self.language_message.format(self.language, self.word))


def main():
    translator = MultiOnlineTranslator()
    translator.start()

if __name__ == '__main__':
    main()