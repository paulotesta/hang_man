import random

WORD_OPTIONS = ('test', 'gata', 'computer', 'program')
NUM_OF_TRIES = 10


def main():
    initial_instructions()
    word = present_word(WORD_OPTIONS)
    tries = 0
    while tries < NUM_OF_TRIES:
        letter = get_letter()
        result = compare_letter(letter, word[0], word[1])
        draw_hangman(result)


def initial_instructions():
    print("Welcome to hangman!")
    print("Please type one letter at a time and try to spell the whole " +
          "word. You can guess wrong 10 times")
    return


def present_word(WORD_OPTIONS):
    word = random.choice(WORD_OPTIONS)
    print("Guess the word: ", end='')
    char_count = len(word)
    masked_word = "_ " * char_count
    print(masked_word)
    return word, masked_word


def get_letter():
    print("Plese type your guess:")
    guess = input()
    return guess


def compare_letter(letter, word, masked_word):
    i = 0
    for element in word:
        if letter == element:
            masked_word = draw_word(masked_word, letter, i)
        i = i + 1
    print(masked_word)


def draw_word(masked_word, letter, i):
    masked_word = masked_word[:i*2] + letter + masked_word[(i * 2) + 1:]

    return masked_word


def draw_hangman(result):
    pass


main()
