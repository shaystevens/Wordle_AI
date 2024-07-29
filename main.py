from play_wordle import *
import letter_frequency
from letter_frequency import *
import time

guesses = 0
correct_word = None

#time.sleep(0.5)
start_wordle()
initialize_global_variables()

start_time = time.time()
while guesses < 7:
  time.sleep(0.5)
  calculate_letter_frequency()
  calculate_words_score()

  guess_word = get_guess_word()
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

  for index in range(len(guess_word)):
    letter_frequency.global_words = remove_words(letter_frequency.global_words, guess_word[index], index, states[index])

  letter_frequency.global_words_score = {}
  letter_frequency.global_letters = letter_frequency.global_zero_letters.copy()

time.sleep(3)
exit_wordle()