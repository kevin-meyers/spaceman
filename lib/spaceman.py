import random
import re


def load_word():
    '''
    A function that reads a text file of words and randomly selects one to use as the secret word from the list.
    Returns:
                 string: The secret word to be used in the spaceman guessing game
    '''
    with open('../data/words.txt', 'r') as f:
        words_list = f.read().split(' ')

    return random.choice(words_list)


def is_word_guessed(secret_word, letters_guessed):
    '''
    A function that checks if all the letters of the secret word have been guessed.
    Args:
        secret_word (string): the random word the user is trying to guess.
        letters_guessed (list of strings): list of letters that have been guessed so far.
    Returns:
        bool: True only if all the letters of secret_word are in letters_guessed, False otherwise
        '''
    for letter in secret_word:
        if letter not in letters_guessed:
            return False

    return True


def get_guessed_word(secret_word, letters_guessed):
    '''
    A function that is used to get a string showing the letters guessed so far in the secret word and underscores for letters that have not been guessed yet.
    Args:
        secret_word (string): the random word the user is trying to guess.
        letters_guessed (list of strings): list of letters that have been guessed so far.
    Returns:
        string: letters and underscores.  For letters in the word that the user has guessed correctly, the string should contain the letter at the correct position.  For letters in the word that the user has not yet guessed, shown an _ (underscore) instead.
    '''

    return re.sub(f'[^{"".join(letters_guessed)}]', '_', secret_word)


def is_guess_in_word(guess, secret_word):
    '''
    A function to check if the guessed letter is in the secret word
    Args:
        guess (string): The letter the player guessed this round
        secret_word (string): The secret word
    Returns:
        bool: True if the guess is in the secret_word, False otherwise
    '''

    return guess in secret_word


def is_guess_valid(guess, letters_guessed):
    '''


    '''
    if guess in letters_guessed:
        print('You\'ve already guessed that!')
        return False

    return guess.isalpha() and len(guess) == 1 


def spaceman(secret_word):
    '''
    A function that controls the game of spaceman. Will start spaceman in the command line.
    Args:
      secret_word (string): the secret word to guess.
    '''
    letters_guessed = []
    num_fails = len(secret_word)
    while not is_word_guessed(secret_word, letters_guessed):
            # TODO: show the player information about the game according to the project spec

        guess = input('Guess a letter! ')

        if not is_guess_valid(guess, letters_guessed):
            print('Invalid guess')
            continue
        else:
            letters_guessed.append(guess)

        if is_guess_in_word(guess, secret_word):
            print(f'Good work! You still have {num_fails} remaining')

        else:
            num_fails -= 1

            if num_fails <= 0:
                break

            print(f'That was incorrect, now you only have {num_fails} remaining')
        print(f'The current progress is {get_guessed_word(secret_word, letters_guessed)}')



    if num_fails < 0:
        print('You lose!')

    else:
        print('You won!')

    print(f'The word is: {secret_word}')


if __name__ == '__main__':
    play = True
    while play:
        spaceman(load_word())
        play = input('Do you want to play again? y/any').lower() == 'y'
