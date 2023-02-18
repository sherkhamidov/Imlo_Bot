from uzwords import words
from difflib import get_close_matches

def checkWord(word,words=words):
    word = word.lower()
    matches = set(get_close_matches(word, words))
    available = False

    if word in matches:
        available = True
        matches = word

    elif 'х' in word:
        word = word.replace('х', 'х')
        matches.update(get_close_matches(word, words))

    elif "x" in words:
        word = word.replace('x', 'x')
        matches.update(get_close_matches(word, words))

    return{'available': available, 'matches': matches}

if __name__ == '__main__':
    print(checkWord("хато"))
    print(checkWord("тарих"))
    print(checkWord("олма"))
    print(checkWord("мева"))