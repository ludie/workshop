# by LCCL Coding Academy, www.LccLcoding.com
# for Shopee Code League 2020

print()

vowels = 'aeiouy'

def translate(word):
    word = word.lower()
    # Case: Word stars with vowel
    if word[0] in vowels:
        return word + 'ay'
    # Case: word starts with consonant sound
    else:
        # Iterate from the first character in
        # word, up to the first occurance of vowel
        for i in range(len(word)):
            # Case when there is a vowel
            if word[i] in vowels:
                return word[i:] + word[:i] + 'ay'
        # Case when there is no vowel in the word
        return word + 'ay'

s = input('Enter a sentence: ')
print(' '.join(translate(word) for word in s.split()))

print()