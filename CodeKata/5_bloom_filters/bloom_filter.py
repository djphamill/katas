from hashlib import md5

class Dictionary:

    def __init__(self, file_path: str):
        self.file_path = file_path

class SpellChecker:

    HASHERS = [md5]

    def __init__(self, dictionary: Dictionary):
        self.dictionary = dictionary
        self.bloom_filter = [0 ] * 10
        self.load_dictionary

    def load_dictionary(self):
        for hasher in self.HASHERS:
            for word in self.dictionary:
                bloom_filter[hasher(word)] = 1

    def is_word(self, word: str):
        return True

def main():
    # Get dictionary
    dictionary = Dictionary('/usr/shar/dict/words')
    
    # Load dictionary in to spell checker
    spell_checker = SpellChecker(dictionary)

    # enter loop, asking for words and checking spell checker
    has_finished = False
    while not has_finished:
        usr_input = input('Type a word that you wish to be checked, otherwise type * to exit: ')
        if usr_input != '*':
            is_word = spell_checker.is_word(usr_input)
            print(f'{usr_input} is {"not " if not is_word else ""}a word')
        else:
            has_finished = True


if __name__ == '__main__':
    main()
