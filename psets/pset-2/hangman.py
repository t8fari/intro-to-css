# Problem Set 2, hangman.py
# Name:
# Collaborators:
# Time spent:

import random
import string

# -----------------------------------
# HELPER CODE
# -----------------------------------

WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    returns: list, a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print(" ", len(wordlist), "words loaded.")
    return wordlist

def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)

    returns: a word from wordlist at random
    """
    return random.choice(wordlist)

# -----------------------------------
# END OF HELPER CODE
# -----------------------------------


# Load the list of words to be accessed from anywhere in the program
wordlist = load_words()

def has_player_won(secret_word, letters_guessed):
    """
    secret_word: string, the lowercase word the user is guessing
    letters_guessed: list (of lowercase letters), the letters that have been
        guessed so far

    returns: boolean, True if all the letters of secret_word are in letters_guessed,
        False otherwise
    """
    # Player wins if there is no secret word
    for c in secret_word:
        if c not in letters_guessed:
            return False
    return True


def get_word_progress(secret_word, letters_guessed):
    """
    secret_word: string, the lowercase word the user is guessing
    letters_guessed: list (of lowercase letters), the letters that have been
        guessed so far

    returns: string, comprised of letters and asterisks (*) that represents
        which letters in secret_word have not been guessed so far
    """
    word = ''
    for c in secret_word:
        if c in letters_guessed:
            word += c
        else:
            word += '*'
    return word


def get_available_letters(letters_guessed):
    """
    letters_guessed: list (of lowercase letters), the letters that have been
        guessed so far

    returns: string, comprised of letters that represents which
      letters have not yet been guessed. The letters should be returned in
      alphabetical order
    """
    return ''.join(c for c in string.ascii_lowercase if c not in letters_guessed)


def hangman(secret_word, with_help):
    """
    secret_word: string, the secret word to guess.
    with_help: boolean, this enables help functionality if true.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secret_word contains and how many guesses they start with.

    * The user should start with 10 guesses.

    * Before each round, you should display to the user how many guesses
      they have left and the letters that the user has not yet guessed.

    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a single letter (or help character '!'
      for with_help functionality)

    * If the user inputs an incorrect consonant, then the user loses ONE guess,
      while if the user inputs an incorrect vowel (a, e, i, o, u),
      then the user loses TWO guesses.

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the
      partially guessed word so far.

    -----------------------------------
    with_help functionality
    -----------------------------------
    * If the guess is the symbol !, you should reveal to the user one of the
      letters missing from the word at the cost of 3 guesses. If the user does
      not have 3 guesses remaining, print a warning message. Otherwise, add
      this letter to their guessed word and continue playing normally.

    Follows the other limitations detailed in the problem write-up.
    """
    print("Welcome to Hangman!")
    print(f"I am thinking of a word that is {len(secret_word)} letters long.")
    num_guesses = 10
    letters_guessed = []

    while not has_player_won(secret_word, letters_guessed):
        # game is over if there are no guesses left
        # or if the player guesses the secret word
        if num_guesses <= 0:
            break
        print("------------------")
        print(f"You have {num_guesses} guesses left.")
        print(f"Available letters: {get_available_letters(letters_guessed)}")
        guess = input("Please guess a letter: ").lower()
        if guess.isalpha() and len(guess)==1:
            # if the letter has already been guessed, alert the user
            if guess in letters_guessed:
                print("Oops! You've already guessed that letter:", end=' ')
            else:
              letters_guessed.append(guess)
              word_progress = get_word_progress(secret_word, letters_guessed)
              if guess in secret_word:
                  print("Good guess:", end=' ')
              else: # guess is not in secret_word
                  print("Oops! That letter is not in my word:", end=' ')
                  # subtract 1 from num_guesses if guess is a consonant
                  # else subtract 2
                  if guess not in 'aeiou':
                      num_guesses -= 1
                  else:
                      num_guesses -= 2
            print(word_progress)
        elif with_help and guess == '!':
            # if the user enters !, reveal one of the missing letters in the secret word at a cost of 3 guesses
            # if there are enough guesses left
            if num_guesses >= 3:
                random_letter = random.choice([x for x in secret_word if x not in letters_guessed])
                letters_guessed.append(random_letter)
                num_guesses -= 3
                print(f"Letter revealed: {random_letter}")
                print(get_word_progress(secret_word, letters_guessed))
            else:
                print(f"Oops! Not enough guesses left: {get_word_progress(secret_word, letters_guessed)}")
        else:
            print(f"Oops! That is not a valid letter. Please input a letter from the alphabet: {get_word_progress(secret_word, letters_guessed)}")
    # after the while loop ends, either because the user ran out of guesses or successfully guessed the secret word
    print("------------------")
    # if the user successfully guessed the secret word
    if has_player_won(secret_word, letters_guessed):
        print("Congratulations, you won!")
        total_score = (num_guesses+4*len(set(secret_word))) + (3*len(secret_word))
        print(f"Your total score for this game is: {total_score}")
    else:
        # the user ran out of guesses
        print(f"Sorry, your ran out of guesses. The word was {secret_word}.")



# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the lines to test

if __name__ == "__main__":
    # To test your game, uncomment the following three lines.

    secret_word = choose_word(wordlist)
    with_help = False
    hangman(secret_word, not with_help)

    # After you complete with_help functionality, change with_help to True
    # and try entering "!" as a guess!

    ###############

    # SUBMISSION INSTRUCTIONS
    # -----------------------
    # It doesn't matter if the lines above are commented in or not
    # when you submit your pset. However, please run ps2_student_tester.py
    # one more time before submitting to make sure all the tests pass.
    pass

