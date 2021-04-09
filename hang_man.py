import random

WORD_OPTIONS = ('test', 'gata', 'computer', 'program')
NUM_OF_TRIES = 10
ALLOWED_CHAR = 'abcdefghijklmnopqrstuvwxyz'


def main():
    all_guesses = ''
    initial_instructions()
    word = present_word(WORD_OPTIONS)
    result = [0, 0]
    while result[0] < NUM_OF_TRIES:
        letter = get_letter()
        all_guesses = all_guesses + letter
        result = compare_letter(letter, all_guesses, word, result[0])
        if result[1] == word:
            winner(word)
            break


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
    return word


def get_letter():
    print("Plese type your guess, one letter at a time:")
    guess = input()

    while (len(guess) != 1 or guess.lower() not in ALLOWED_CHAR):
        print("Please only use Alphabetical characters, try again")
        print("Plese type your guess:")
        guess = input()

    return guess.lower()


def compare_letter(letter, all_guesses, word, tries):
    output = ''

    if letter not in word:
        tries = incorrect_guess(tries)

    for letter in word:
        if letter in all_guesses:
            output = output + letter
        else:
            output = output + '_ '

    print(output)

    return tries, output


def draw_hangman(image):
    if image == 1:
        print("  --------  ")
        return
    if image == 2:
        print("  --------  ")
        print("     O      ")
        return
    if image == 3:
        print("  --------  ")
        print("     O      ")
        print("     |      ")
        return
    if image == 4:
        print("  --------  ")
        print("     O      ")
        print("     |      ")
        print("    /       ")
        return
    if image == 5:
        print("  --------  ")
        print("     O      ")
        print("     |      ")
        print("    / \     ")
        return
    if image == 6:
        print("  --------  ")
        print("   \ O      ")
        print("     |      ")
        print("    / \     ")
        return
    if image == 7:
        print("  --------  ")
        print("   \ O /    ")
        print("     |      ")
        print("    / \     ")
        return
    if image == 8:
        print("  --------  ")
        print("   \ O /|   ")
        print("     |      ")
        print("    / \     ")
        return
    if image == 9:
        print("  --------  ")
        print("   \ O_|/   ")
        print("     |      ")
        print("    / \     ")
        return
    if image == 10:
        print("  --------  ")
        print("     O_|    ")
        print("    /|\     ")
        print("    / \     ")
        print("You Loose!")
        return


def incorrect_guess(tries):
    tries = tries + 1
    print("Guesses remaning: ", NUM_OF_TRIES - tries)
    draw_hangman(tries)
    return tries


def winner(word):
    print("Congratulations! You correctly guessed: ", word)
    return


main()
