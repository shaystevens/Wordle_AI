import letter_frequency
import time
import argparse
from play_wordle import *
from letter_frequency import *


def main(hard_mode=False, quiet=False, start_word=None):
  guesses = 0
  
  initialize_global_variables()
  if start_word is not None and (len(start_word) != 5 or start_word not in letter_frequency.global_words):
    print("Invalid word. Try again.")
    exit(1)
  
  start_wordle(quiet)

  start_time = time.time()
  while guesses < 7:
    time.sleep(0.5)
    calculate_letter_frequency()
    calculate_words_score()
    guess_word = get_guess_word()

    if start_word is not None and guesses < 1:
      guess_word = start_word

    
    input_guess(guess_word)
    guesses += 1

    time.sleep(1.5)
    states = get_word_results(guesses)

    print_guess_word(guess_word, states)
    if all(state == "correct" for state in states):
      end_time = time.time()
      elapsed_time = end_time - start_time
      print(f"Solved with {guesses} {"guess" if guesses < 2 else "guesses"} in {elapsed_time:.2f} seconds.")
      break
    
    letter_frequency.global_known_letters = {letter for letter, state in zip(guess_word, states) if state == "correct"}
    for index in range(len(guess_word)):
      letter_frequency.global_words = remove_words(letter_frequency.global_words, guess_word[index], index, states[index], hard_mode)

    letter_frequency.global_words_score = {}
    letter_frequency.global_letters = letter_frequency.global_zero_letters.copy()

  time.sleep(3)
  exit_wordle()

if __name__ == "__main__":
  parser = argparse.ArgumentParser(description="This Python program is designed to solve the New York Times Wordle game\nby leveraging letter frequency analysis and automating user input through Selenium.")

  # Adding optional arguments
  parser.add_argument('--hard_mode', action='store_true', help='If set, enforces Wordle hard mode rules.')
  parser.add_argument('--quiet', action='store_true', help='Allows the program to simulate the game logic internally without opening a web browser.')
  parser.add_argument('--start_word', type=str, default=None, help='Choose starting word; defaults to a preset value if not specified.')

  # Parsing arguments
  args = parser.parse_args()

  # Running main with parsed arguments
  main(hard_mode=args.hard_mode, quiet=args.quiet, start_word=args.start_word)