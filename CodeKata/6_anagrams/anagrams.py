from itertools import permutations


def find_anagrams(word: str):
    anagrams = []

    all_permutations_of_letters = [
        ''.join(group) for group in set(permutations(word, len(word)))]

    with open('dictionary', 'r') as f:
        checked_all_words = False
        while not checked_all_words:
            word = f.readline().strip('\n')
            if not word:
                checked_all_words = True
            if word in all_permutations_of_letters:
                anagrams.append(word)

    return anagrams
