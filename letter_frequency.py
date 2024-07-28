import math
from collections import Counter
from wordle_words import *

# Global Variables
global_words = None
global_letters = None
global_zero_letters = None
global_words_score = {}
_known_letters = set()


def initialize_global_variables():
  global global_words
  global global_letters
  global global_zero_letters

  global_words = get_words()
  global_letters = get_letters()
  global_zero_letters = global_letters.copy()


def calculate_letter_frequency():
  global global_letters
  global global_words

  for word in global_words:
    for letter in word:
      global_letters[letter] += 1


def calculate_words_score():
  global global_words_score

  global_words_score = {word: 0 for word in global_words}
  for word in global_words:
    for letter in set(word):
      global_words_score[word] += global_letters[letter]


def get_guess_word():
  global global_words_score
  guess_word = max(global_words_score, key=global_words_score.get)
  return guess_word


def remove_words(words, letter, index, state):
  match state:
    case "absent":
      return [word for word in words if letter not in word]

    case "present":
      _known_letters.add(letter)
      return [
        word for word in words
        if not (letter in word and word[index] == letter) and letter in word
      ]

    case "correct":
      _known_letters.add(letter)
      return [word for word in words if letter in word]
      #return [word for word in words if word[index] == letter] # Unomment for hard mode

