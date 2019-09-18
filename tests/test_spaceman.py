import sys
sys.path.append('../')

from lib import spaceman

def test_load_word():
	word = spaceman.load_word()
	assert type(word) == str
	assert len(word) >= 1
	assert word.isalpha()

def test_is_word_guessed():
	assert spaceman.is_word_guessed('alpha', ['a', 'l', 'p', 'h'])
	assert not spaceman.is_word_guessed('beta', ['b', 'e', 'a', 'l'])

def test_get_guessed_word():
	assert spaceman.get_guessed_word('gamma', ['g', 'm']) == 'g_mm_'
	assert spaceman.get_guessed_word('delta', ['c']) == '_____'

def test_is_guess_in_word():
	assert spaceman.is_guess_in_word('e', 'epsilon')
	assert not spaceman.is_guess_in_word('b', 'zeta')

def test_is_guess_valid():
	assert spaceman.is_guess_valid('c', [])
	assert not spaceman.is_guess_valid('c', ['c'])
	assert not spaceman.is_guess_valid('ab', [])
	assert not spaceman.is_guess_valid('$', [])
	assert not spaceman.is_guess_valid('7', [])

if __name__ == '__main__':
	test_load_word()
	test_is_word_guessed()
	test_get_guessed_word()
	test_is_guess_in_word()
	test_is_guess_valid()
