from collections import defaultdict
from wordle_words import *
import time

start_time = time.time()
possible_solutions = get_words()

# Initialize the letter_dict with a list of 5 zeros for each letter
letter_dict = defaultdict(lambda: [0, 0, 0, 0, 0])

# Total occurrences of each letter
total_counts = defaultdict(int)

# Populate the letter_dict with index positions
for word in possible_solutions:
    for index, letter in enumerate(word):
        letter_dict[letter][index] += 1
        total_counts[letter] += 1

# Calculate weights
letter_weights = {}
for letter, counts in letter_dict.items():
    total = total_counts[letter]
    weights = [count / total for count in counts]
    letter_weights[letter] = weights

# Display the result
for letter, weights in sorted(letter_weights.items()):
    print(f"Letter '{letter}': {weights}")
    print(f"Letter '{letter}': {sum(weights)}")

end_time = time.time()
elapsed_time = end_time - start_time
print(f'Time Taken: {elapsed_time:.4f} seconds')

def calculate_index_weight(letter_dict=defaultdict(lambda: [0, 0, 0, 0, 0]), possible_solutions=None):
    total_counts = defaultdict(int)

    for word in possible_solutions:
        for index, letter in enumerate(word):
            letter_dict[letter][index] += 1
            total_counts[letter] += 1
    
    letter_weights = {}
    for letter, counts in letter_dict.items():
        total = total_counts[letter]
        weights = [count / total for count in counts]
        letter_weights[letter] = weights
    

