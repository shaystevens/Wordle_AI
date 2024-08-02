from wordle_words import *
from collections import defaultdict
import os
os.system('')

# Global Variables
global_words = None
global_letters = None
global_zero_letters = None
global_words_score = {}
global_known_letters = set()
global_normalised_letters = None
global_letter_weights = {}


def initialize_global_variables():
  """
  This function initializes the global variables of the letter_frequency module.

  """
  global global_words
  global global_letters
  global global_zero_letters
  global global_normalised_letters

  global_words = get_words()
  global_letters = get_letters()
  global_normalised_letters = global_letters.copy()
  global_zero_letters = global_letters.copy()


def calculate_letter_frequency():
  """
  This function calculates the letter frequency of the letters within the possible words.
  ALso normalises the letter frequnecy.

  """
  global global_letters
  global global_words
  global global_normalised_letters

  for word in global_words:
    for letter in word:
      global_letters[letter] += 1
  
  total_sum = sum(global_letters.values())
  global_normalised_letters = {key: value / total_sum for key, value in global_letters.items()}


def calculate_words_score():
  """
  This function calculates the weighted score of each word according to the formula.

  """
  global global_words_score

  global_words_score = {word: 0 for word in global_words}
  for word in global_words:
    for index in range(5):
      global_words_score[word] += global_normalised_letters[word[index]] * global_letter_weights[word[index]][index]
    
    global_words_score[word] *= len(set(word))


def get_guess_word():
  """
  This function gets the guess word by finding the word with the highest score.

  Returns:
  str: returns the guess word.
  """
  global global_words_score
  guess_word = max(global_words_score, key=global_words_score.get)
  return guess_word


def remove_words(words, letter, index, state):
  """
  This function removes words by a case basis depending on the letter and it's state.

  Returns:
  list: The words list after the words have been removed.
  """
  match state:
    case "absent":
      return [word for word in words if (letter not in word or letter in global_known_letters) and word[index] != letter]
    case "present":
      return [
        word for word in words
        if not (letter in word and word[index] == letter) and letter in word
      ]
    case "correct":
      return [word for word in words if word[index] == letter] 
      

def print_guess_word(word, states):
  """
  This function prints the guess word depending on each letter's state with ANSI.
  """
  BACKGROUND_GREEN = "\033[42m"
  BACKGROUND_YELLOW = "\033[43m"
  RESET = "\033[0m"

  for index in range(len(word)):
    colored_letter = ""
    match states[index]:
      case "correct":
        colored_letter += BACKGROUND_GREEN + word[index] + RESET
        print(colored_letter, end="")
      case "present":
        colored_letter += BACKGROUND_YELLOW + word[index] + RESET
        print(colored_letter, end="")
      case "absent":
        print(word[index], end="")

  print()


def calculate_index_weight(letter_dict=defaultdict(lambda: [0, 0, 0, 0, 0]), possible_solutions=None):
  """
  This function calculates the weighted index of each possible letter.
  """
  total_counts = defaultdict(int)

  for word in possible_solutions:
      for index, letter in enumerate(word):
          letter_dict[letter][index] += 1
          total_counts[letter] += 1
  
  global global_letter_weights
  for letter, counts in letter_dict.items():
      total = total_counts[letter]
      weights = [count / total for count in counts]
      global_letter_weights[letter] = weights