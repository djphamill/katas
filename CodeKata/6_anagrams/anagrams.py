def hash(word: str):
    return ''.join(sorted(word))

anagrams = {}

with open('input', 'r') as f:
    words = [word.strip('\n') for word in f.readlines()]

max_anagrams = []

for word in words:
    word_hashed = hash(word)
    if word_hashed in anagrams:
        anagrams[word_hashed].append(word)
    else:
        anagrams[word_hashed] = [word]

    if len(anagrams[word_hashed]) > len(max_anagrams):
        max_anagrams = anagrams[word_hashed]

with open('output', 'w') as f:
    for word in words:
        f.write(' '.join(anagrams[hash(word)]))
        f.write('\n')

print(f'done: max anagrams were {len(max_anagrams)}, for {max_anagrams}')
