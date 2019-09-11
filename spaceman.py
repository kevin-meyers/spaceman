import random
import re

def load_word():
    '''
    A function that reads a text file of words and randomly selects one to use as the secret word from the list.
    Returns:
		 string: The secret word to be used in the spaceman guessing game
    '''
    with open('words.txt', 'r') as f:
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
    # TODO: Loop through the letters in the secret_word and check if a letter is not in lettersGuessed
	
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

	return re.sub(f'[^{"".join(guessed)}]', '_', word)



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


def is_guess_valid(guess):
	'''


	'''
	return guess.isalpha() and len(guess) == 1


def spaceman(secret_word):
    '''
    A function that controls the game of spaceman. Will start spaceman in the command line.
    Args:
      secret_word (string): the secret word to guess.
    '''
	letters_guessed = []

	while not is_word_guessed(secret_word, letters_guessed):
    #TODO: show the player information about the game according to the project spec

		guess = input('Guess a letter! ')


    #TODO: Ask the player to guess one letter per round and check that it is only one letter

	if not is_guess_valid(guess):
		print('Invalid guess')
		continue
	
	else:
		letters_guessed.append(guess)
    #TODO: Check if the guessed letter is in the secret or not and give the player feedback

	if is_guess_in_word(guess, secret_word):
		return get_guessed_word()

    #TODO: show the guessed word so far

    #TODO: check if the game has been won or lost






#These function calls that will start the game
secret_word = load_word()
spaceman(load_word())
